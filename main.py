from colorama import init, Fore
from input_handlers import get_user_input, get_numeric_input
from display import show_main_menu, show_catalogue_menu, show_roster_menu
import roster
import units
from catalogue_manager import CatalogueManager
from roster_manager import RosterManager
import os

def handle_catalogue_menu(cat_manager):
    """Handle catalogue management menu options"""
    while True:
        choice = show_catalogue_menu()
        
        if choice == '1':
            cat_manager.scan_for_catalogues()
        
        elif choice == '2':
            cat_file = get_user_input(f"{Fore.WHITE}Enter catalogue filename: ")
            cat_manager.load_single_catalogue(cat_file)
        
        elif choice == '3':
            cat_manager.list_loaded_catalogues()
        
        elif choice == '4':
            cat_manager.list_loaded_catalogues()
            cat_num = get_numeric_input(f"{Fore.WHITE}Enter catalogue number: ")
            if cat_num is not None:
                filenames = list(cat_manager.catalogues.keys())
                if 1 <= cat_num <= len(filenames):
                    cat_manager.set_active_catalogue(filenames[cat_num - 1])
                else:
                    print(f"{Fore.RED}Invalid catalogue number")
        
        elif choice == '5':
            break

def handle_roster_menu(roster_manager):
    """Handle roster management menu options"""
    while True:
        choice = show_roster_menu()
        
        if choice == '1':
            roster_manager.scan_for_rosters()
            
        elif choice == '2':
            roster_manager.list_available_rosters()
            
        elif choice == '3':
            roster_manager.list_available_rosters()
            roster_num = get_numeric_input(f"{Fore.WHITE}Enter roster number (or press Enter to cancel): ")
            if roster_num is not None:
                filenames = list(roster_manager.available_rosters.keys())
                if 1 <= roster_num <= len(filenames):
                    roster_manager.load_roster(filenames[roster_num - 1])
                else:
                    print(f"{Fore.RED}Invalid roster number")
                    
        elif choice == '4':
            roster_manager.save_roster()
            
        elif choice == '5':
            filename = get_user_input(f"{Fore.WHITE}Enter new roster filename: ")
            if filename:
                roster_manager.active_roster = {}
                roster_manager.active_roster_name = filename
                print(f"{Fore.GREEN}Created new roster: {filename}")
                
        elif choice == '6':
            break

def main():
    init(autoreset=True)
    cat_manager = CatalogueManager()
    roster_manager = RosterManager()
    
    # Initial scans
    cat_manager.scan_for_catalogues()
    roster_manager.scan_for_rosters()
    
    while True:
        try:
            cat_root, cat_name = cat_manager.get_active_catalogue()
            current_roster, roster_name = roster_manager.get_active_roster()
            
            choice = show_main_menu(roster_name, cat_name)
            
            if not choice:
                continue
                
            if choice == '1':
                handle_catalogue_menu(cat_manager)
                
            elif choice == '2':
                handle_roster_menu(roster_manager)
                
            elif choice == '3':
                if not cat_root:
                    print(f"{Fore.RED}Please load a catalogue first")
                    continue
                units.list_available_units(cat_root)
                
            elif choice == '4':
                if not cat_root:
                    print(f"{Fore.RED}Please load a catalogue first")
                    continue
                    
                available_units = units.list_available_units(cat_root)
                if not available_units:
                    continue
                    
                unit_num = get_numeric_input(f"{Fore.WHITE}Enter unit number (or press Enter to cancel): ")
                if unit_num is None:
                    continue
                    
                if 1 <= unit_num <= len(available_units):
                    quantity = get_numeric_input(f"{Fore.WHITE}Enter quantity (or press Enter to cancel): ")
                    if quantity is None:
                        continue
                    
                    unit = available_units[unit_num-1]
                    unit_name = unit.get('name')
                    points = units.get_unit_points(unit)
                    roster.add_unit_to_roster(roster_manager.active_roster, unit_name, points, quantity)
                else:
                    print(f"{Fore.RED}Invalid unit number")
                    
            elif choice == '5':
                if not current_roster:
                    print(f"{Fore.RED}Roster is empty")
                    continue
                    
                roster.print_roster(current_roster, roster_name, cat_name)
                unit_num = get_numeric_input(f"{Fore.WHITE}Enter unit number to remove (or press Enter to cancel): ")
                if unit_num is not None:
                    roster.remove_unit_from_roster(current_roster, unit_num)
                
            elif choice == '6':
                roster.print_roster(current_roster, roster_name, cat_name)
                
            elif choice == '7':
                print(f"{Fore.YELLOW}Goodbye!")
                break
            else:
                print(f"{Fore.YELLOW}Invalid option, please try again")
                
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}")
            print(f"{Fore.YELLOW}Returning to main menu")
            continue

if __name__ == "__main__":
    main()