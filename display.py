from colorama import Fore
from input_handlers import get_user_input

def show_main_menu(roster_name: str = None, catalogue_name: str = None):
    """Display main menu and get user choice"""
    print(f"\n{Fore.CYAN}Main Menu:")
    if catalogue_name:
        print(f"{Fore.WHITE}Current Catalogue: {catalogue_name}")
    if roster_name:
        print(f"{Fore.WHITE}Current Roster: {roster_name}")
    print(f"{Fore.CYAN}=" * 40)
    
    print(f"{Fore.WHITE}1. Catalogue Management")
    print(f"{Fore.WHITE}2. Roster Management")
    print(f"{Fore.WHITE}3. List Available Units")
    print(f"{Fore.WHITE}4. Add Unit")
    print(f"{Fore.WHITE}5. Remove Unit")
    print(f"{Fore.WHITE}6. View Current Roster")
    print(f"{Fore.WHITE}7. Exit")
    return get_user_input(f"{Fore.GREEN}Select option (1-7): ")

def show_catalogue_menu():
    """Display catalogue management menu"""
    print(f"\n{Fore.CYAN}Catalogue Management:")
    print(f"{Fore.CYAN}=" * 40)
    print(f"{Fore.WHITE}1. Scan and Load All Catalogues")
    print(f"{Fore.WHITE}2. Load Single Catalogue")
    print(f"{Fore.WHITE}3. List Loaded Catalogues")
    print(f"{Fore.WHITE}4. Switch Active Catalogue")
    print(f"{Fore.WHITE}5. Return to Main Menu")
    return get_user_input(f"{Fore.GREEN}Select option (1-5): ")

def show_roster_menu():
    """Display roster management menu"""
    print(f"\n{Fore.CYAN}Roster Management:")
    print(f"{Fore.CYAN}=" * 40)
    print(f"{Fore.WHITE}1. Scan for Roster Files")
    print(f"{Fore.WHITE}2. List Available Rosters")
    print(f"{Fore.WHITE}3. Load Roster")
    print(f"{Fore.WHITE}4. Save Current Roster")
    print(f"{Fore.WHITE}5. Create New Roster")
    print(f"{Fore.WHITE}6. Return to Main Menu")
    return get_user_input(f"{Fore.GREEN}Select option (1-6): ")