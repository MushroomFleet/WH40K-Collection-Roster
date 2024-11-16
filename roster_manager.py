import os
from colorama import Fore
import json
from input_handlers import get_user_input

class RosterManager:
    def __init__(self):
        self.available_rosters = {}  # Dictionary to store found roster filenames and their total points
        self.active_roster = {}
        self.active_roster_name = None

    def scan_for_rosters(self):
        """Scan current directory for .json roster files"""
        try:
            print(f"{Fore.CYAN}Scanning for roster files...")
            roster_files = [f for f in os.listdir('.') if f.endswith('.json')]
            
            if not roster_files:
                print(f"{Fore.YELLOW}No roster files found in current directory")
                return False
                
            print(f"{Fore.GREEN}Found {len(roster_files)} roster files:")
            for file in roster_files:
                try:
                    with open(file, 'r') as f:
                        roster_data = json.load(f)
                        total_points = sum(
                            details["points_per_unit"] * details["quantity"]
                            for details in roster_data.values()
                        )
                        self.available_rosters[file] = total_points
                        print(f"{Fore.WHITE}{file} ({total_points} points)")
                except Exception as e:
                    print(f"{Fore.RED}Error loading {file}: {e}")
                    
            return bool(self.available_rosters)
            
        except Exception as e:
            print(f"{Fore.RED}Error scanning for rosters: {e}")
            return False

    def load_roster(self, filename: str) -> bool:
        """Load a roster from file"""
        try:
            with open(filename, 'r') as f:
                self.active_roster = json.load(f)
                self.active_roster_name = filename
                total_points = sum(
                    details["points_per_unit"] * details["quantity"]
                    for details in self.active_roster.values()
                )
                print(f"{Fore.GREEN}Loaded roster: {filename} ({total_points} points)")
                return True
        except FileNotFoundError:
            print(f"{Fore.YELLOW}No existing roster found: {filename}")
            self.active_roster = {}
            self.active_roster_name = filename
            return True
        except json.JSONDecodeError:
            print(f"{Fore.RED}Error: Invalid roster file")
            return False
        except Exception as e:
            print(f"{Fore.RED}Error loading roster: {e}")
            return False

    def save_roster(self, filename: str = None) -> bool:
        """Save current roster to file"""
        if not filename:
            filename = self.active_roster_name
            
        if not filename:
            print(f"{Fore.YELLOW}No filename specified")
            return False
            
        try:
            # Check if file exists
            if os.path.exists(filename):
                response = get_user_input(
                    f"{Fore.YELLOW}File {filename} already exists. Overwrite? (y/n): "
                ).lower()
                if response != 'y':
                    print(f"{Fore.YELLOW}Save cancelled")
                    return False
            
            with open(filename, 'w') as f:
                json.dump(self.active_roster, f, indent=2)
            print(f"{Fore.GREEN}Saved roster to: {filename}")
            self.active_roster_name = filename
            
            # Update available rosters list
            total_points = sum(
                details["points_per_unit"] * details["quantity"]
                for details in self.active_roster.values()
            )
            self.available_rosters[filename] = total_points
            
            return True
        except Exception as e:
            print(f"{Fore.RED}Error saving roster: {e}")
            return False

    def list_available_rosters(self):
        """Display all available roster files"""
        if not self.available_rosters:
            print(f"{Fore.YELLOW}No roster files found")
            return
            
        print(f"\n{Fore.CYAN}Available Rosters:")
        print(f"{Fore.CYAN}=" * 40)
        for idx, (filename, points) in enumerate(self.available_rosters.items(), 1):
            prefix = "* " if filename == self.active_roster_name else "  "
            print(f"{Fore.WHITE}{prefix}{idx}. {filename} ({points} points)")
        print(f"{Fore.CYAN}=" * 40)
        print(f"{Fore.YELLOW}* indicates active roster")

    def get_active_roster(self):
        """Return currently active roster and name"""
        return self.active_roster, self.active_roster_name
