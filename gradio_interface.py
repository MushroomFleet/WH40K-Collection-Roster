import gradio as gr
import os
from catalogue_manager import CatalogueManager
from roster_manager import RosterManager
from units import list_available_units, get_unit_points
from roster import add_unit_to_roster, remove_unit_from_roster, calculate_total_points

class GradioArmyManager:
    def __init__(self):
        self.cat_manager = CatalogueManager()
        self.roster_manager = RosterManager()
        
    def scan_catalogues(self):
        """Scan for and load catalogue files"""
        success = self.cat_manager.scan_for_catalogues()
        if success:
            catalogues = list(self.cat_manager.catalogues.keys())
            return gr.Dropdown(choices=catalogues, value=catalogues[0], visible=True), \
                   f"Found {len(catalogues)} catalogues"
        return gr.Dropdown(visible=False), "No catalogues found"
        
    def scan_rosters(self):
        """Scan for roster files"""
        success = self.roster_manager.scan_for_rosters()
        if success:
            rosters = list(self.roster_manager.available_rosters.keys())
            return gr.Dropdown(choices=rosters, visible=True), \
                   f"Found {len(rosters)} rosters"
        return gr.Dropdown(visible=False), "No rosters found"
        
    def load_catalogue(self, catalogue_name):
        """Load selected catalogue and return available units"""
        if not catalogue_name:
            return [], "Please select a catalogue"
            
        success = self.cat_manager.set_active_catalogue(catalogue_name)
        if not success:
            return [], f"Failed to load catalogue: {catalogue_name}"
            
        root, _ = self.cat_manager.get_active_catalogue()
        units = list_available_units(root)
        if not units:
            return [], "No units found in catalogue"
            
        unit_list = [f"{unit.get('name')} ({get_unit_points(unit)} pts)" for unit in units]
        return unit_list, f"Loaded {len(unit_list)} units from {catalogue_name}"
        
    def load_roster(self, roster_name):
        """Load selected roster"""
        if not roster_name:
            return "Please select a roster", ""
            
        success = self.roster_manager.load_roster(roster_name)
        if not success:
            return f"Failed to load roster: {roster_name}", ""
            
        roster, _ = self.roster_manager.get_active_roster()
        roster_text = self.format_roster(roster)
        return f"Loaded roster: {roster_name}", roster_text
        
    def format_roster(self, roster):
        """Format roster for display"""
        if not roster:
            return "Roster is empty"
            
        lines = []
        total_points = calculate_total_points(roster)
        
        for unit, details in roster.items():
            points = details["points_per_unit"] * details["quantity"]
            lines.append(f"{unit} x{details['quantity']} ({points} pts)")
            if details.get("wargear"):
                for gear in details["wargear"]:
                    lines.append(f"  - {gear}")
                    
        lines.append(f"\nTotal Points: {total_points}")
        return "\n".join(lines)
        
    def add_unit(self, unit_selection, quantity):
        """Add selected unit to roster"""
        if not unit_selection:
            return "Please select a unit", ""
            
        if not quantity or quantity < 1:
            return "Please enter a valid quantity", ""
        
        try:
            # Handle unit_selection whether it's a list or string
            if isinstance(unit_selection, list):
                unit_selection = unit_selection[0]  # Take first selection if multiple
            
            # Extract unit name and points from selection string
            # Format: "Unit Name (XX pts)"
            unit_name = unit_selection.split(" (")[0]
            points = int(unit_selection.split("(")[1].split(" ")[0])
            
            roster, _ = self.roster_manager.get_active_roster()
            add_unit_to_roster(roster, unit_name, points, quantity)
            
            return f"Added {quantity}x {unit_name}", self.format_roster(roster)
        except Exception as e:
            return f"Error adding unit: {str(e)}", ""
        
    def save_current_roster(self, filename):
        """Save current roster to file"""
        if not filename:
            return "Please enter a filename"
            
        if not filename.endswith('.json'):
            filename += '.json'
            
        success = self.roster_manager.save_roster(filename)
        if success:
            return f"Saved roster to {filename}"
        return "Failed to save roster"

    def remove_unit(self, unit_selection, quantity=1):
        """Remove unit from roster"""
        if not unit_selection:
            return "Please select a unit to remove", ""
            
        try:
            roster, _ = self.roster_manager.get_active_roster()
            if not roster:
                return "Roster is empty", ""
                
            # Find unit in roster
            units = list(roster.keys())
            if unit_selection not in units:
                return f"Unit {unit_selection} not found in roster", ""
                
            # Remove unit
            remove_unit_from_roster(roster, units.index(unit_selection) + 1)
            return f"Removed {quantity}x {unit_selection}", self.format_roster(roster)
        except Exception as e:
            return f"Error removing unit: {str(e)}", ""

def create_interface():
    manager = GradioArmyManager()
    
    with gr.Blocks(title="Warhammer 40K Army Manager") as interface:
        gr.Markdown("# Warhammer 40K Army Manager")
        
        # Store available units for both tabs
        available_units = gr.State([])
        
        with gr.Tab("Catalogue Management"):
            scan_cat_btn = gr.Button("Scan for Catalogues")
            cat_dropdown = gr.Dropdown(label="Select Catalogue", visible=False)
            cat_status = gr.Textbox(label="Status", interactive=False)
            load_cat_btn = gr.Button("Load Selected Catalogue")
            unit_list_preview = gr.Dropdown(
                label="Preview Available Units",
                visible=False,
                multiselect=False
            )
            
            scan_cat_btn.click(
                fn=manager.scan_catalogues,
                outputs=[cat_dropdown, cat_status]
            )
            
            # Update both unit lists when loading catalogue
            load_cat_btn.click(
                fn=manager.load_catalogue,
                inputs=cat_dropdown,
                outputs=[unit_list_preview, cat_status]
            ).then(
                lambda x: x,  # Pass through the unit list
                inputs=[unit_list_preview],
                outputs=[available_units]
            )
            
        with gr.Tab("Roster Management"):
            with gr.Row():
                with gr.Column():
                    scan_roster_btn = gr.Button("Scan for Rosters")
                    roster_dropdown = gr.Dropdown(
                        label="Select Roster",
                        visible=False,
                        multiselect=False
                    )
                    load_roster_btn = gr.Button("Load Selected Roster")
                    roster_status = gr.Textbox(label="Status", interactive=False)
                    
                with gr.Column():
                    roster_display = gr.Textbox(
                        label="Current Roster",
                        interactive=False,
                        lines=10
                    )
                    
            # Unit Addition Section
            with gr.Row():
                add_unit_dropdown = gr.Dropdown(
                    label="Select Unit to Add",
                    choices=[],
                    multiselect=False
                )
                quantity_input = gr.Number(
                    label="Quantity",
                    value=1,
                    minimum=1,
                    step=1
                )
                add_unit_btn = gr.Button("Add Unit")
                
            with gr.Row():
                save_name = gr.Textbox(label="Save Filename")
                save_btn = gr.Button("Save Roster")
                save_status = gr.Textbox(label="Save Status", interactive=False)

            # Unit Removal Section
            with gr.Row():
                remove_unit_dropdown = gr.Dropdown(
                    label="Select Unit to Remove",
                    multiselect=False
                )
                remove_btn = gr.Button("Remove Unit")
                
            # Update add_unit_dropdown when catalogue is loaded
            available_units.change(
                lambda x: gr.Dropdown(choices=x),
                inputs=[available_units],
                outputs=[add_unit_dropdown]
            )
                
            scan_roster_btn.click(
                fn=manager.scan_rosters,
                outputs=[roster_dropdown, roster_status]
            )
            
            load_roster_btn.click(
                fn=manager.load_roster,
                inputs=roster_dropdown,
                outputs=[roster_status, roster_display]
            )
            
            add_unit_btn.click(
                fn=manager.add_unit,
                inputs=[add_unit_dropdown, quantity_input],
                outputs=[roster_status, roster_display]
            )
            
            save_btn.click(
                fn=manager.save_current_roster,
                inputs=save_name,
                outputs=save_status
            )

            remove_btn.click(
                fn=manager.remove_unit,
                inputs=[remove_unit_dropdown, quantity_input],
                outputs=[roster_status, roster_display]
            )
            
    return interface

if __name__ == "__main__":
    interface = create_interface()
    interface.launch(
        server_name="127.0.0.1",  # Only allow local connections
        share=False,              # Disable sharing/tunneling
        show_error=True,          # Show detailed errors for debugging
        inbrowser=True           # Auto-open in default browser
    )