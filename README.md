# Gradio Layout Visualizer

An enhanced visual builder for Gradio with Avada-like capabilities, featuring drag-and-drop, templates, advanced styling controls, and real-time preview.

## 🌟 Features

### ✨ Enhanced from Gradio Sketch
- ✅ **Enhanced Parameter Controls** - Color pickers, sliders, toggles instead of text inputs
- ✅ **Auto-Browser-Open** - Browser opens automatically when you start the app
- ✅ **Desktop Shortcuts** - One-click launch from desktop or start menu
- ✅ **Automated UI Testing** - Comprehensive Playwright tests for quality assurance
- 🚧 **Drag-and-Drop Interface** - Intuitive component placement (coming soon)
- 🚧 **Template Library** - Pre-built layouts for common ML use cases (coming soon)
- 🚧 **Real-time Preview** - See changes instantly as you build (coming soon)
- 🚧 **Component Themes** - Pre-styled component sets (coming soon)

### From Original Gradio Sketch
- ✅ Visual component editing
- ✅ Layout management (rows/columns)
- ✅ Event listener configuration
- ✅ AI-powered code generation
- ✅ Deploy to HuggingFace Spaces
- ✅ Save & render workflow

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/realmarauder/Gradio_Layout_Visualizer.git
cd Gradio_Layout_Visualizer

# Install dependencies
pip install -e .
```

### Create Desktop Shortcuts (Recommended)

```bash
# One-time setup - creates desktop and start menu shortcuts
gradio-visualizer --install-shortcuts

# After setup, just double-click the desktop icon to launch!
```

### Usage

```bash
# Start the visual builder (browser opens automatically!)
gradio-visualizer

# Or specify a custom app file
gradio-visualizer my_app.py

# Share publicly
gradio-visualizer --share

# Disable auto-browser-open if needed
gradio-visualizer --no-browser

# Custom port
gradio-visualizer --port 8080
```

### Run Tests

```bash
# Run automated UI tests
python run_tests.py

# Run specific tests
pytest tests/test_ui_enhanced_controls.py

# Watch tests run in browser
pytest tests/ --headed
```

## 📚 Documentation

### Basic Workflow

1. **Add Components** - Click the "+" buttons to place components
2. **Configure** - Click the edit icon (✎) to configure component properties
3. **Add Functions** - Create event handlers with AI-powered code generation
4. **Save & Render** - Preview your app in action
5. **Deploy** - Push directly to HuggingFace Spaces

### Project Structure

```
gradio_layout_visualizer/
├── sketch/              # Core builder logic
│   ├── run.py          # Main application
│   ├── utils.py        # AI code generation
│   └── sketchbox.py    # Component wrapper
├── frontend/           # Frontend components
│   └── sketchbox/      # Interactive overlay UI
├── templates/          # Pre-built templates (coming soon)
└── themes/            # Theme definitions (coming soon)
```

## 🎯 Roadmap

### Phase 1: Enhanced UX (In Progress)
- [ ] Improve component placement UX
- [ ] Add live preview mode
- [ ] Enhanced styling controls

### Phase 2: Templates & Themes
- [ ] Template library system
- [ ] Pre-built templates (chat, image processing, dashboards)
- [ ] Theme system
- [ ] Component style presets

### Phase 3: Advanced Features
- [ ] True drag-and-drop
- [ ] Responsive design tools
- [ ] Component library
- [ ] Export options

## 🤝 Contributing

Contributions are welcome! This project is an enhancement of Gradio's sketch feature.

## 📝 License

Based on Gradio's original sketch implementation. See Gradio's license for details.

## 🙏 Credits

Built on top of [Gradio](https://github.com/gradio-app/gradio) by the Gradio team.
Enhanced with Avada-like capabilities for a more polished visual building experience.
