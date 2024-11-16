import xml.etree.ElementTree as ET
from colorama import Fore
import os

def load_catalogue(cat_file: str):
    """Load and parse a .cat file"""
    if not cat_file:
        print(f"{Fore.YELLOW}No file specified, returning to main menu")
        return None
        
    if not os.path.exists(cat_file):
        print(f"{Fore.RED}Error: Catalogue file '{cat_file}' not found")
        return None
        
    try:
        # Register the namespace
        ET.register_namespace('', "http://www.battlescribe.net/schema/catalogueSchema")
        
        # Parse the file
        tree = ET.parse(cat_file)
        root = tree.getroot()
        
        # Strip the namespace for easier searching
        for elem in root.iter():
            if '}' in elem.tag:
                elem.tag = elem.tag.split('}', 1)[1]
                
        print(f"{Fore.GREEN}Loaded catalogue: {cat_file}")
        return root
    except ET.ParseError as e:
        print(f"{Fore.RED}Error: Invalid catalogue file")
        print(f"{Fore.RED}Parse error details: {str(e)}")
        return None
    except Exception as e:
        print(f"{Fore.RED}Error loading catalogue: {e}")
        print(f"{Fore.RED}Exception details:", str(e))
        return None