from colorama import Fore
from input_handlers import get_numeric_input

def print_roster(roster: dict, roster_name: str = None, catalogue_name: str = None):
    """Display the current roster and total points"""
    if not roster:
        print(f"{Fore.YELLOW}Roster is empty")
        return
        
    try:
        total_points = calculate_total_points(roster)
        
        # Display header with roster and catalogue info
        print(f"\n{Fore.CYAN}Current Roster: {Fore.WHITE}{roster_name or 'Unsaved'}")
        if catalogue_name:
            print(f"{Fore.CYAN}Using Catalogue: {Fore.WHITE}{catalogue_name}")
        print(f"{Fore.CYAN}=" * 40)
        
        # Print units with index numbers for removal
        for idx, (unit, details) in enumerate(roster.items(), 1):
            points = details["points_per_unit"] * details["quantity"]
            print(f"{Fore.WHITE}{idx}. {unit} x{details['quantity']} ({points} pts)")
            if details.get("wargear"):
                for gear in details["wargear"]:
                    print(f"{Fore.YELLOW}  - {gear}")
                
        print(f"{Fore.CYAN}=" * 40)
        print(f"{Fore.GREEN}Total Points: {total_points}")
    except Exception as e:
        print(f"{Fore.RED}Error displaying roster: {e}")

def calculate_total_points(roster: dict) -> int:
    """Calculate total points for the current roster"""
    try:
        return sum(
            details["points_per_unit"] * details["quantity"]
            for details in roster.values()
        )
    except Exception as e:
        print(f"{Fore.RED}Error calculating points: {e}")
        return 0

def add_unit_to_roster(roster: dict, unit_name: str, points: int, quantity: int = 1):
    """Add a unit to the roster"""
    if not unit_name:
        return
        
    try:
        if unit_name not in roster:
            roster[unit_name] = {
                "quantity": 0,
                "points_per_unit": points,
                "wargear": []
            }
        
        roster[unit_name]["quantity"] += quantity
        print(f"{Fore.GREEN}Added {quantity}x {unit_name}")
    except Exception as e:
        print(f"{Fore.RED}Error adding unit: {e}")

def remove_unit_from_roster(roster: dict, unit_idx: int) -> bool:
    """Remove a unit from the roster"""
    try:
        if not roster:
            print(f"{Fore.YELLOW}Roster is empty")
            return False
            
        # Convert roster to list for indexed access
        units = list(roster.items())
        
        if unit_idx < 1 or unit_idx > len(units):
            print(f"{Fore.RED}Invalid unit number")
            return False
            
        unit_name, details = units[unit_idx - 1]
        
        # Get quantity to remove
        current_qty = details["quantity"]
        remove_qty = get_numeric_input(
            f"{Fore.WHITE}Enter quantity to remove (max {current_qty}): ",
            min_val=1,
            max_val=current_qty
        )
        
        if remove_qty is None:
            return False
            
        # Update or remove the unit
        if remove_qty >= current_qty:
            del roster[unit_name]
            print(f"{Fore.GREEN}Removed all {unit_name} from roster")
        else:
            roster[unit_name]["quantity"] -= remove_qty
            print(f"{Fore.GREEN}Removed {remove_qty}x {unit_name}")
            
        return True
    except Exception as e:
        print(f"{Fore.RED}Error removing unit: {e}")
        return False