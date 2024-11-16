import os
from colorama import Fore
import catalogue

class CatalogueManager:
    def __init__(self):
        self.catalogues = {}  # Dictionary to store loaded catalogues: {filename: root}
        self.active_catalogue = None  # Currently selected catalogue for operations
        self.active_catalogue_name = None

    def scan_for_catalogues(self):
        """Scan current directory for .cat files and load them"""
        try:
            print(f"{Fore.CYAN}Scanning for catalogue files...")
            cat_files = [f for f in os.listdir('.') if f.endswith('.cat')]
            
            if not cat_files:
                print(f"{Fore.YELLOW}No .cat files found in current directory")
                return False
                
            print(f"{Fore.GREEN}Found {len(cat_files)} catalogue files:")
            for file in cat_files:
                print(f"{Fore.WHITE}Loading: {file}")
                root = catalogue.load_catalogue(file)
                if root is not None:
                    self.catalogues[file] = root
                    
            if self.catalogues:
                print(f"{Fore.GREEN}Successfully loaded {len(self.catalogues)} catalogues")
                # Set first catalogue as active if none is selected
                if not self.active_catalogue:
                    self.set_active_catalogue(next(iter(self.catalogues.keys())))
                return True
            return False
            
        except Exception as e:
            print(f"{Fore.RED}Error scanning for catalogues: {e}")
            return False

    def load_single_catalogue(self, filename):
        """Load a single catalogue file"""
        root = catalogue.load_catalogue(filename)
        if root is not None:
            self.catalogues[filename] = root
            self.set_active_catalogue(filename)
            return True
        return False

    def set_active_catalogue(self, filename):
        """Set the active catalogue for operations"""
        if filename in self.catalogues:
            self.active_catalogue = self.catalogues[filename]
            self.active_catalogue_name = filename
            print(f"{Fore.GREEN}Active catalogue set to: {filename}")
            return True
        print(f"{Fore.RED}Catalogue {filename} not found")
        return False

    def list_loaded_catalogues(self):
        """Display all loaded catalogues"""
        if not self.catalogues:
            print(f"{Fore.YELLOW}No catalogues loaded")
            return
            
        print(f"\n{Fore.CYAN}Loaded Catalogues:")
        print(f"{Fore.CYAN}=" * 40)
        for idx, filename in enumerate(self.catalogues.keys(), 1):
            prefix = "* " if filename == self.active_catalogue_name else "  "
            print(f"{Fore.WHITE}{prefix}{idx}. {filename}")
        print(f"{Fore.CYAN}=" * 40)
        print(f"{Fore.YELLOW}* indicates active catalogue")

    def get_active_catalogue(self):
        """Return currently active catalogue root and name"""
        return self.active_catalogue, self.active_catalogue_name
