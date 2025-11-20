"""Desktop shortcut installer for Gradio Layout Visualizer

Creates desktop shortcuts and start menu entries for easy access to the tool.
Works cross-platform: Windows, macOS, Linux.
"""

import os
import sys
import platform
from pathlib import Path


def create_shortcuts():
    """Create desktop shortcuts for the visualizer"""
    try:
        from pyshortcuts import make_shortcut
    except ImportError:
        print("❌ pyshortcuts not installed. Installing now...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyshortcuts"])
        from pyshortcuts import make_shortcut

    # Get the path to the CLI script
    cli_path = Path(__file__).parent / "cli.py"
    python_exe = sys.executable

    # Determine icon path (if we add one later)
    icon_path = Path(__file__).parent / "assets" / "icon.ico"
    if not icon_path.exists():
        icon_path = None

    print("🎨 Creating desktop shortcuts for Gradio Layout Visualizer...")

    # Create desktop shortcut
    try:
        make_shortcut(
            script=f'"{python_exe}" "{cli_path}"',
            name="Gradio Layout Visualizer",
            description="Visual builder for Gradio apps with enhanced controls",
            icon=str(icon_path) if icon_path else None,
            terminal=True,  # Keep terminal open to see output
            desktop=True,
            startmenu=True,
        )
        print("✅ Desktop shortcut created successfully!")

        # Show where shortcuts were created
        system = platform.system()
        if system == "Windows":
            desktop = Path.home() / "Desktop"
            startmenu = Path.home() / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs"
            print(f"   📁 Desktop: {desktop}")
            print(f"   📁 Start Menu: {startmenu}")
        elif system == "Darwin":  # macOS
            desktop = Path.home() / "Desktop"
            applications = Path("/Applications")
            print(f"   📁 Desktop: {desktop}")
            print(f"   📁 Applications: {applications}")
        else:  # Linux
            desktop = Path.home() / "Desktop"
            applications = Path.home() / ".local" / "share" / "applications"
            print(f"   📁 Desktop: {desktop}")
            print(f"   📁 Applications: {applications}")

        print("\n🚀 You can now launch Gradio Layout Visualizer from:")
        print("   • Desktop shortcut")
        print("   • Start menu / Applications folder")
        print("   • Or command line: gradio-visualizer")

        return True

    except Exception as e:
        print(f"❌ Error creating shortcuts: {e}")
        print("   You can still use the CLI command: gradio-visualizer")
        return False


def remove_shortcuts():
    """Remove desktop shortcuts"""
    try:
        from pyshortcuts import make_shortcut
        make_shortcut(
            script="dummy",
            name="Gradio Layout Visualizer",
            desktop=True,
            startmenu=True,
        )
        print("✅ Shortcuts removed successfully!")
        return True
    except Exception as e:
        print(f"❌ Error removing shortcuts: {e}")
        return False


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Install or remove desktop shortcuts for Gradio Layout Visualizer"
    )
    parser.add_argument(
        "--remove",
        action="store_true",
        help="Remove shortcuts instead of creating them",
    )

    args = parser.parse_args()

    if args.remove:
        remove_shortcuts()
    else:
        create_shortcuts()
