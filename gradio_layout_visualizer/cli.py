"""Command-line interface for Gradio Layout Visualizer"""

import argparse
import os
from gradio_layout_visualizer.sketch.run import create


def main():
    parser = argparse.ArgumentParser(
        description="Gradio Layout Visualizer - Enhanced visual builder for Gradio apps"
    )
    parser.add_argument(
        "file",
        nargs="?",
        default="app.py",
        help="Path to the Gradio app file (default: app.py)",
    )
    parser.add_argument(
        "--config",
        default="app.json",
        help="Path to the config file (default: app.json)",
    )
    parser.add_argument(
        "--share",
        action="store_true",
        help="Create a public share link",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=7860,
        help="Port to run the server on (default: 7860)",
    )
    parser.add_argument(
        "--install-shortcuts",
        action="store_true",
        help="Install desktop shortcuts and exit",
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Don't automatically open browser",
    )

    args = parser.parse_args()

    # Handle shortcut installation
    if args.install_shortcuts:
        from gradio_layout_visualizer.install_shortcuts import create_shortcuts
        create_shortcuts()
        return

    # Ensure file paths are absolute
    app_file = os.path.abspath(args.file)
    config_file = os.path.abspath(args.config)

    print(f"🎨 Starting Gradio Layout Visualizer...")
    print(f"📝 App file: {app_file}")
    print(f"⚙️  Config file: {config_file}")

    # Auto-open browser unless disabled
    inbrowser = not args.no_browser

    demo = create(app_file, config_file)
    demo.launch(
        share=args.share,
        server_port=args.port,
        inbrowser=inbrowser,  # Automatically open browser
        quiet=False,  # Show startup messages
    )


if __name__ == "__main__":
    main()
