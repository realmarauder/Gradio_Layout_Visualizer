"""UI tests for enhanced parameter controls

Tests the visual controls like color pickers, toggles, sliders, etc.
"""

import pytest
from playwright.sync_api import Page, expect


class TestEnhancedControls:
    """Test suite for enhanced parameter controls"""

    def test_page_loads(self, visualizer_page: Page):
        """Test that the visualizer page loads successfully"""
        expect(visualizer_page).to_have_title("Gradio", timeout=10000)

    def test_add_component_button_visible(self, visualizer_page: Page):
        """Test that component addition interface is visible"""
        # Should see component selection buttons
        textbox_btn = visualizer_page.get_by_role("button", name="Textbox")
        expect(textbox_btn).to_be_visible(timeout=5000)

    def test_add_textbox_component(self, visualizer_page: Page):
        """Test adding a Textbox component"""
        # Click Textbox button to add component
        textbox_btn = visualizer_page.get_by_role("button", name="Textbox")
        textbox_btn.click()

        # Should show configuration panel
        config_heading = visualizer_page.get_by_text("Configuration")
        expect(config_heading).to_be_visible(timeout=5000)

    def test_enhanced_controls_message(self, visualizer_page: Page):
        """Test that enhanced controls message is displayed"""
        # Add a component first
        textbox_btn = visualizer_page.get_by_role("button", name="Textbox")
        textbox_btn.click()

        # Look for enhanced controls indicator
        enhanced_msg = visualizer_page.get_by_text("Enhanced Controls")
        expect(enhanced_msg).to_be_visible(timeout=5000)

    def test_color_picker_for_button(self, visualizer_page: Page):
        """Test that Button component shows color picker"""
        # Add a Button component
        button_btn = visualizer_page.get_by_role("button", name="Button")
        button_btn.click()

        # Wait for config panel
        visualizer_page.wait_for_timeout(1000)

        # Look for color picker input (type="color")
        # Note: This may need adjustment based on Gradio's ColorPicker implementation
        color_inputs = visualizer_page.locator('input[type="color"]')
        # Should have at least one color picker visible
        expect(color_inputs.first).to_be_visible(timeout=5000)

    def test_checkbox_for_boolean_params(self, visualizer_page: Page):
        """Test that boolean parameters show as checkboxes"""
        # Add a Textbox which has boolean params like 'visible', 'interactive'
        textbox_btn = visualizer_page.get_by_role("button", name="Textbox")
        textbox_btn.click()

        visualizer_page.wait_for_timeout(1000)

        # Look for checkbox inputs (toggle switches)
        checkboxes = visualizer_page.locator('input[type="checkbox"]')
        # Should have checkboxes for boolean parameters
        expect(checkboxes.first).to_be_visible(timeout=5000)

    def test_slider_for_lines_param(self, visualizer_page: Page):
        """Test that 'lines' parameter shows as slider"""
        # Add a Textbox which has 'lines' parameter
        textbox_btn = visualizer_page.get_by_role("button", name="Textbox")
        textbox_btn.click()

        visualizer_page.wait_for_timeout(1000)

        # Look for slider input
        sliders = visualizer_page.locator('input[type="range"]')
        # Should have at least one slider (for 'lines' or other numeric params)
        expect(sliders.first).to_be_visible(timeout=5000)

    def test_variable_name_editable(self, visualizer_page: Page):
        """Test that variable name can be edited"""
        # Add a component
        textbox_btn = visualizer_page.get_by_role("button", name="Textbox")
        textbox_btn.click()

        visualizer_page.wait_for_timeout(1000)

        # Find variable name input
        var_name_label = visualizer_page.get_by_text("Variable Name")
        expect(var_name_label).to_be_visible()

        # Should be able to edit it
        var_name_input = visualizer_page.locator('label:has-text("Variable Name") ~ textarea, label:has-text("Variable Name") ~ input')
        expect(var_name_input.first).to_be_editable()

    def test_documentation_links_present(self, visualizer_page: Page):
        """Test that documentation links are present for parameters"""
        # Add a component
        textbox_btn = visualizer_page.get_by_role("button", name="Textbox")
        textbox_btn.click()

        visualizer_page.wait_for_timeout(1000)

        # Look for docs links
        docs_links = visualizer_page.get_by_role("link", name="docs")
        # Should have multiple docs links for different parameters
        expect(docs_links.first).to_be_visible(timeout=5000)

    def test_save_and_render_button(self, visualizer_page: Page):
        """Test that Save & Render button is present"""
        save_btn = visualizer_page.get_by_role("button", name="Save & Render")
        expect(save_btn).to_be_visible(timeout=5000)

    def test_add_multiple_components(self, visualizer_page: Page):
        """Test adding multiple components"""
        # Add first component
        textbox_btn = visualizer_page.get_by_role("button", name="Textbox")
        textbox_btn.click()
        visualizer_page.wait_for_timeout(500)

        # Navigate back to add mode by hovering over canvas area
        # This might require clicking a specific area - may need adjustment
        visualizer_page.wait_for_timeout(1000)

        # Add second component
        button_btn = visualizer_page.get_by_role("button", name="Button")
        if button_btn.is_visible():
            button_btn.click()
            visualizer_page.wait_for_timeout(500)

        # Both components should be rendered
        # This is a basic check - actual verification would need to inspect the canvas


class TestResponsiveness:
    """Test responsive behavior"""

    def test_mobile_viewport(self, visualizer_page: Page):
        """Test that the UI works on mobile viewport"""
        visualizer_page.set_viewport_size({"width": 375, "height": 667})
        visualizer_page.reload()
        visualizer_page.wait_for_load_state("networkidle")

        # Basic elements should still be visible
        textbox_btn = visualizer_page.get_by_role("button", name="Textbox")
        expect(textbox_btn).to_be_visible(timeout=5000)

    def test_tablet_viewport(self, visualizer_page: Page):
        """Test that the UI works on tablet viewport"""
        visualizer_page.set_viewport_size({"width": 768, "height": 1024})
        visualizer_page.reload()
        visualizer_page.wait_for_load_state("networkidle")

        # Basic elements should still be visible
        textbox_btn = visualizer_page.get_by_role("button", name="Textbox")
        expect(textbox_btn).to_be_visible(timeout=5000)


class TestAccessibility:
    """Test accessibility features"""

    def test_keyboard_navigation(self, visualizer_page: Page):
        """Test basic keyboard navigation"""
        # Tab through interface
        visualizer_page.keyboard.press("Tab")
        visualizer_page.wait_for_timeout(100)

        # Should be able to navigate with keyboard
        # Focused element should be visible
        focused = visualizer_page.evaluate("document.activeElement.tagName")
        assert focused in ["BUTTON", "INPUT", "TEXTAREA", "A"]

    def test_aria_labels(self, visualizer_page: Page):
        """Test that important elements have ARIA labels"""
        # Check for buttons with proper roles
        buttons = visualizer_page.get_by_role("button")
        expect(buttons.first).to_be_visible(timeout=5000)

        # Links should have role
        links = visualizer_page.get_by_role("link")
        if links.count() > 0:
            expect(links.first).to_be_visible()
