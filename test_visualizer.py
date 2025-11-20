"""Test script for Gradio Layout Visualizer with enhanced controls"""

import os
import sys

# Add the package to path for testing
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gradio_layout_visualizer.sketch.run import create

if __name__ == "__main__":
    # Create test files
    app_file = "test_app.py"
    config_file = "test_app.json"

    print("🎨 Starting Gradio Layout Visualizer Test...")
    print(f"📝 App file: {app_file}")
    print(f"⚙️  Config file: {config_file}")
    print("\n✨ Try the enhanced controls:")
    print("  - Color parameters now use color pickers")
    print("  - Boolean parameters use toggle switches")
    print("  - Numeric parameters with known ranges use sliders")
    print("  - Enum/choice parameters use dropdowns")
    print("\n🚀 Starting demo...\n")

    demo = create(app_file, config_file)
    demo.launch(
        share=False,
        inbrowser=True,  # Auto-open browser for convenience
        quiet=False,
    )
