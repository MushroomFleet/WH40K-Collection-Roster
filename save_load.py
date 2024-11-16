import json
from colorama import Fore
import os

def save_roster(roster: dict, filename: str):
    """Save roster to JSON file"""
    if not filename:
        print(f"{Fore.YELLOW}No file specified, returning to main menu")
        return
        
    try:
        with open(filename, 'w') as f:
            json.dump(roster, f, indent=2)
        print(f"{Fore.GREEN}Saved roster to: {filename}")
    except Exception as e:
        print(f"{Fore.RED}Error saving roster: {e}")

def load_roster(filename: str):
    """Load roster from JSON file"""
    if not filename:
        print(f"{Fore.YELLOW}No file specified, returning to main menu")
        return {}
        
    try:
        with open(filename, 'r') as f:
            roster = json.load(f)
        print(f"{Fore.GREEN}Loaded roster: {filename}")
        return roster
    except FileNotFoundError:
        print(f"{Fore.YELLOW}No existing roster found, starting new")
        return {}
    except json.JSONDecodeError:
        print(f"{Fore.RED}Error: Invalid roster file")
        return {}
    except Exception as e:
        print(f"{Fore.RED}Error loading roster: {e}")
        return {}
