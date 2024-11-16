from colorama import Fore
import xml.etree.ElementTree as ET

def list_available_units(root):
    """List all available units from the catalogue"""
    try:
        # Get the sharedSelectionEntries section
        shared_entries_section = root.find("sharedSelectionEntries")
        if not shared_entries_section:
            print(f"{Fore.YELLOW}No sharedSelectionEntries section found")
            return None
            
        # Find all unit and model entries
        units = []
        for entry in shared_entries_section:
            if entry.tag == 'selectionEntry':
                entry_type = entry.get('type')
                if entry_type in ['unit', 'model']:
                    # Check if hidden
                    hidden = entry.get('hidden', 'false').lower() == 'true'
                    if not hidden:
                        units.append(entry)

        if not units:
            print(f"{Fore.YELLOW}No units found in catalogue")
            return None
            
        print(f"\n{Fore.CYAN}Available Units:")
        print(f"{Fore.CYAN}=" * 40)
        
        # Sort units by name
        units.sort(key=lambda x: x.get('name', ''))
        
        # Display units
        for i, unit in enumerate(units, 1):
            name = unit.get('name', 'Unknown')
            
            # Find points cost
            points = "?"
            costs = unit.find(".//costs")
            if costs is not None:
                for cost in costs.findall('cost'):
                    if cost.get('name') == 'pts':
                        points = cost.get('value', '?')
                        break
            
            print(f"{Fore.WHITE}{i}. {name} ({points} pts)")
        
        print(f"\n{Fore.CYAN}Total units available: {len(units)}")
        return units
        
    except Exception as e:
        print(f"{Fore.RED}Error listing units: {e}")
        print(f"{Fore.RED}Exception details:", str(e))
        return None

def get_unit_points(unit):
    """Get points cost for a unit"""
    try:
        costs = unit.find(".//costs")
        if costs is not None:
            for cost in costs.findall('cost'):
                if cost.get('name') == 'pts':
                    return int(cost.get('value', 0))
        return 0
    except Exception:
        return 0