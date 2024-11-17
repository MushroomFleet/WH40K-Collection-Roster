# Warhammer 40K Army Roster Manager

A tool for managing Warhammer 40K army rosters using .cat files. Compatible with 10th Edition Battlescribe/Battleforge catalogue files. Now featuring both command-line and web-based interfaces.
<br/>
https://www.youtube.com/watch?v=PDtfCmV-lnc
![Army Roster Manager Demo](https://raw.githubusercontent.com/MushroomFleet/WH40K-Collection-Roster/main/demo-images/Gradio-Version.png)


## Web Interface Instructions

The project now includes a web-based user interface powered by Gradio, making it easier to manage your army rosters.

1. Launch the Web Interface:
   ```
   Double-click run_web.bat
   ```
   This will open the interface in your default web browser.

2. Using the Web Interface:

   a. Catalogue Management Tab:
   - Click "Scan for Catalogues" to find available .cat files
   - Select a catalogue from the dropdown
   - Click "Load Selected Catalogue" to load the units
   - You can preview available units in this tab
   - Units are displayed with their point costs

   b. Roster Management Tab:
   - Click "Scan for Rosters" to find saved rosters
   - Select and load an existing roster, or start fresh
   - Use the "Select Unit to Add" dropdown to choose units
   - Set quantity and click "Add Unit" to add to your roster
   - Use the "Select Unit to Remove" dropdown to choose units to remove
   - Remove units using the "Remove Unit" button
   - Save your roster by entering a filename and clicking "Save Roster"
   - Enable "Allow Overwrite" checkbox to update existing rosters

3. Features:
   - Real-time point calculations
   - Unit quantity management
   - Easy unit selection via dropdowns
   - Automatic roster updates
   - Local-only operation for security
   - Automatic file type handling (.cat and .json)
   - User-friendly unit removal via dropdown
   - Detailed unit information in dropdowns (including quantities and points)
   - Overwrite protection for saved rosters

4. Security Note:
   - The web interface runs locally only (127.0.0.1)
   - No external connections are made
   - Your data remains on your computer
<br/>
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
   b. Double-click run_web.bat for the web interface
   c. Double-click run.bat for the command-line interface
   ```

## Catalogue Files (.cat)

The program requires Warhammer 40K 10th Edition .cat files to function. These files contain the unit data for each faction.

You can find compatible .cat files here:
https://github.com/MushroomFleet/wh40k-10e (MIRROR)
https://github.com/BSData/wh40k-10e/tree/main (AUTHOR)

## Quick Start Guide

1. Place .cat files in the program directory
2. Run the program using run_web.bat for the web interface
3. The program automatically scans for:
   - .cat files (faction catalogues)
   - .json files (saved rosters)
4. Use the interface tabs to manage catalogues and rosters

## Main Features

### Catalogue Management
- Automatic scanning for .cat files
- Load multiple catalogues simultaneously
- Switch between different faction catalogues
- View all loaded catalogues with point costs
- Individual catalogue loading option
- Unit preview functionality

### Roster Management
- Automatic scanning for saved rosters
- Create new rosters
- Load existing rosters
- Save rosters with overwrite protection
- View all available rosters with points values
- Add units with quantities via dropdown
- Remove units via dropdown selection
- Track total roster points
- Automatic roster updates

### Unit Management
- List all available units from current catalogue
- Display unit point costs
- Add units with quantities
- Remove units through dropdown selection
- Automatic points calculation
- Track unit quantities
- Format unit display with points and quantities

### Interface Features
- Web-based Gradio interface
- Command-line interface option
- Two main tabs: Catalogue and Roster Management
- Dropdown-based unit selection
- Real-time roster updates
- Clear status messages
- Point cost tracking
- Quantity management
- File overwrite protection

## Files Structure

- `main.py` - Command-line interface
- `gradio_interface.py` - Web interface
- `catalogue_manager.py` - Catalogue file management
- `roster_manager.py` - Roster file management
- `input_handlers.py` - User input handling
- `display.py` - Menu and display functions
- `catalogue.py` - Catalogue parsing operations
- `roster.py` - Roster operations
- `units.py` - Unit handling functions
- `requirements.txt` - Python package requirements
- `install.bat` - Installation script
- `run.bat` - Command-line launcher
- `run_web.bat` - Web interface launcher

## Display Features
- Color-coded command-line interface
- Clean web interface design
- Active catalogue and roster always displayed
- Points values shown for all rosters and units
- Unit quantities and points in roster view
- Clear status messages and error handling
- Dropdown-based unit selection and removal

## Saved Data
- Rosters are saved as .json files
- Automatic backup before overwriting
- Points values stored with units
- Unit quantities tracked
- Roster total points calculated
- File overwrite protection

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
   - Check web browser compatibility

## Support

For issues:
1. Check error messages
2. Verify file locations
3. Confirm Python version
4. Check file permissions
5. Validate .cat file format
6. Ensure web browser is up to date

## Future Development
- Unit wargear selection
- Army composition rules
- Export to different formats
- Command-line arguments
- Detachment handling
- Points limit validation
- Battalion structure support
- Enhanced user interface features
- Batch unit operations
- Advanced filtering options

## Contributing
Contributions welcome! Please feel free to submit pull requests.

## License
[Your chosen license goes here]

## Acknowledgments
- Created for Warhammer 40K 10th Edition
- Compatible with Battlescribe/Battleforge .cat format
- Thanks to the community for testing and feedback
- Built with Gradio for web interface

---
Last Updated: November 2024
