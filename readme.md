# Warhammer 40K Army Roster Manager

A command-line tool for managing Warhammer 40K army rosters using .cat files. Compatible with 10th Edition Battlescribe/Battleforge catalogue files.
<br/>
![Army Roster Manager Demo](https://raw.githubusercontent.com/MushroomFleet/WH40K-Collection-Roster/main/demo-images/example-tracker-display.png)


## Setup Instructions

1. Requirements:
   - Python 3.6 or higher
   - Windows OS (for .bat files)

2. Installation:
   ```
   a. Clone or download this repository
   b. Double-click install.bat
   c. Wait for the installation to complete
   ```

3. Running the Program:
   ```
   a. Place your .cat files in the same directory as the program
   b. Double-click run.bat
   ```

## Catalogue Files (.cat)

The program requires Warhammer 40K 10th Edition .cat files to function. These files contain the unit data for each faction.

You can find compatible .cat files here:
https://github.com/MushroomFleet/wh40k-10e (MIRROR)
https://github.com/BSData/wh40k-10e/tree/main (AUTHOR)

## Quick Start Guide

1. Place .cat files in the program directory
2. Run the program using run.bat
3. The program automatically scans for:
   - .cat files (faction catalogues)
   - .json files (saved rosters)
4. Select options from the menu to manage your army roster

## Main Features

### Catalogue Management
- Automatic scanning for .cat files
- Load multiple catalogues simultaneously
- Switch between different faction catalogues
- View all loaded catalogues
- Individual catalogue loading option

### Roster Management
- Automatic scanning for saved rosters
- Create new rosters
- Load existing rosters
- Save rosters with overwrite protection
- View all available rosters with points values
- Add/remove units with quantities
- Track total roster points

### Unit Management
- List all available units from current catalogue
- Add units with quantities
- Remove units or reduce quantities
- Automatic points calculation
- Track wargear options

## Menu System

1. Main Menu:
   - Catalogue Management
   - Roster Management
   - List Available Units
   - Add Unit
   - Remove Unit
   - View Current Roster

2. Catalogue Management:
   - Scan and Load All Catalogues
   - Load Single Catalogue
   - List Loaded Catalogues
   - Switch Active Catalogue

3. Roster Management:
   - Scan for Roster Files
   - List Available Rosters
   - Load Roster
   - Save Current Roster
   - Create New Roster

## Files Structure

- `main.py` - Main program file
- `catalogue_manager.py` - Catalogue file management
- `roster_manager.py` - Roster file management
- `input_handlers.py` - User input handling
- `display.py` - Menu and display functions
- `catalogue.py` - Catalogue parsing operations
- `roster.py` - Roster operations
- `units.py` - Unit handling functions
- `requirements.txt` - Python package requirements
- `install.bat` - Installation script
- `run.bat` - Program launcher

## Display Features
- Color-coded interface for better readability
- Active catalogue and roster always displayed
- Points values shown for all rosters
- Unit quantities and points in roster view
- Clear status messages and error handling

## Saved Data
- Rosters are saved as .json files
- Automatic backup before overwriting
- Points values stored with units
- Unit quantities tracked
- Wargear options preserved

## Troubleshooting

1. Installation Issues:
   - Verify Python installation (3.6+)
   - Run install.bat as administrator if needed
   - Check PATH environment variable

2. Catalogue Loading:
   - Ensure .cat files are in program directory
   - Verify .cat files are 10th Edition format
   - Check file permissions

3. Roster Management:
   - Verify write permissions for .json files
   - Check disk space for saves
   - Ensure roster files aren't open elsewhere

4. General Issues:
   - Check console for error messages
   - Verify all required files present
   - Confirm .cat file compatibility

## Support

For issues:
1. Check error messages
2. Verify file locations
3. Confirm Python version
4. Check file permissions
5. Validate .cat file format

## Future Development
- Unit wargear selection
- Army composition rules
- Export to different formats
- Command-line arguments
- Detachment handling
- Points limit validation
- Battalion structure support

## Contributing
Contributions welcome! Please feel free to submit pull requests.

## License
[Your chosen license goes here]

## Acknowledgments
- Created for Warhammer 40K 10th Edition
- Compatible with Battlescribe/Battleforge .cat format
- Thanks to the community for testing and feedback

---
Last Updated: November 2024
