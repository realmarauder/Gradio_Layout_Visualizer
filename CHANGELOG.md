# Changelog

All notable changes to Gradio Layout Visualizer will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

#### 🚀 Automation Features (Phase 1B)
- **Auto-Browser-Open** - Browser automatically opens when visualizer starts
  - Enabled by default for local development
  - `--no-browser` flag to disable
  - `inbrowser=True` parameter in launch()
  - Saves 5-10 seconds per session

- **Desktop Shortcuts Installer** - One-click launch from desktop/start menu
  - Cross-platform support (Windows, macOS, Linux)
  - `--install-shortcuts` CLI command
  - Standalone installer module
  - Automatic Python executable detection
  - Creates desktop and start menu entries

- **Automated UI Testing with Playwright** - Comprehensive test suite
  - Test suite for enhanced controls
  - Responsive design tests (mobile, tablet, desktop)
  - Accessibility tests (keyboard navigation, ARIA labels)
  - Cross-browser compatibility
  - CI/CD ready
  - Test runner script (`run_tests.py`)
  - pytest configuration

#### ✨ Enhanced Parameter Controls (Phase 1A)
- **Enhanced Parameter Controls** - Major UX improvement over original Gradio Sketch
  - Color picker for color parameters (e.g., `color`, `bg_color`, `border_color`)
  - Toggle switches for boolean parameters (e.g., `visible`, `interactive`, `show_label`)
  - Sliders for numeric parameters with known ranges (e.g., `lines`, `height`, `scale`)
  - Number inputs for generic numeric parameters
  - Dropdowns for enum/literal type parameters
  - Smart parameter type detection based on parameter names and type annotations
  - Appropriate event handlers per control type (change vs blur/submit)

- **Test Infrastructure**
  - `test_visualizer.py` - Test script to launch the enhanced visualizer
  - Example apps in `examples/` directory
  - Example README with usage instructions
  - `tests/` directory with Playwright UI tests
  - `conftest.py` - Pytest fixtures and server management
  - `pytest.ini` - Pytest configuration
  - `run_tests.py` - Test runner with browser installation

- **Documentation**
  - Comprehensive ROADMAP.md with 12-week enhancement plan
  - Enhanced README with features and quick start guide
  - Examples documentation
  - `docs/ENHANCED_CONTROLS.md` - Detailed guide for parameter controls
  - `docs/AUTOMATION_FEATURES.md` - Complete automation documentation

### Changed
- Updated parameter configuration UI message from generic Python syntax to "Enhanced Controls"
- Import paths updated to use `gradio_layout_visualizer` package instead of `gradio.sketch`
- CLI now auto-opens browser by default (can be disabled with `--no-browser`)
- Test script and examples now auto-open browser for better UX
- README updated with automation features prominently displayed
- requirements.txt updated with testing and desktop integration dependencies

### Technical Details
- New module: `enhanced_controls.py` with smart parameter detection
- Functions: `get_param_type_info()`, `create_enhanced_control()`, `format_value_for_storage()`
- Parameter mappings for 20+ common Gradio component parameters
- Type-aware control rendering system

## [0.1.0] - 2025-11-20

### Added
- Initial project setup forked from Gradio Sketch
- Core sketch functionality (run.py, utils.py, sketchbox.py)
- Frontend components (Svelte sketchbox UI)
- CLI entry point (`gradio-visualizer` command)
- Python package setup (setup.py, requirements.txt)
- Project structure with designated directories for templates and themes

### Features from Original Gradio Sketch
- Visual component editing and placement
- Layout management (rows/columns with nesting)
- Event listener configuration
- AI-powered code generation using Qwen LLM
- Deploy to HuggingFace Spaces integration
- Save & render workflow
- Code export functionality
