# Automation Features

Gradio Layout Visualizer includes three major automation features to remove friction and make the tool as seamless as possible.

---

## 🚀 1. Auto-Browser-Open

### What It Does
Automatically opens your web browser when the visualizer starts - no more manual link clicking!

### Why It Matters
**Before:**
1. Run `gradio-visualizer`
2. Wait for server to start
3. Look for the URL in terminal output
4. Right-click the URL
5. Select "Open in browser"
6. Switch to browser window

**After:**
1. Run `gradio-visualizer`
2. Browser opens automatically ✨

### Usage

**Enabled by default:**
```bash
gradio-visualizer
# Browser opens automatically at http://localhost:7860
```

**Disable if needed:**
```bash
gradio-visualizer --no-browser
# Server runs, but browser doesn't open
```

**In Python code:**
```python
from gradio_layout_visualizer.sketch.run import create

demo = create("app.py", "app.json")
demo.launch(
    inbrowser=True,  # Auto-open browser (default)
    port=7860
)
```

### Use Cases
- ✅ **Local development** - Instant visual feedback
- ✅ **Quick testing** - Faster iteration cycles
- ✅ **Demos** - Smoother presentation flow
- ❌ **Server deployment** - Use `--no-browser`
- ❌ **Headless environments** - Use `--no-browser`

---

## 🖥️ 2. Desktop Shortcuts

### What It Does
Creates desktop shortcuts and start menu entries so you can launch the visualizer without remembering commands or file paths.

### Why It Matters
**Before:**
```bash
# Have to remember:
cd /path/to/projects/Gradio_Layout_Visualizer
source venv/bin/activate  # or equivalent
gradio-visualizer
```

**After:**
1. Double-click desktop icon 🖱️
2. That's it!

### Installation

**One-time setup:**
```bash
gradio-visualizer --install-shortcuts
```

**Or using Python:**
```bash
python -m gradio_layout_visualizer.install_shortcuts
```

**Output:**
```
🎨 Creating desktop shortcuts for Gradio Layout Visualizer...
✅ Desktop shortcut created successfully!
   📁 Desktop: /Users/you/Desktop
   📁 Start Menu: /Users/you/Library/Application Support/...

🚀 You can now launch Gradio Layout Visualizer from:
   • Desktop shortcut
   • Start menu / Applications folder
   • Or command line: gradio-visualizer
```

### Platform Support

#### Windows
- Desktop: `C:\Users\YourName\Desktop\Gradio Layout Visualizer.lnk`
- Start Menu: `C:\Users\YourName\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Gradio Layout Visualizer.lnk`

#### macOS
- Desktop: `/Users/YourName/Desktop/Gradio Layout Visualizer`
- Applications: `/Applications/Gradio Layout Visualizer.app`

#### Linux
- Desktop: `/home/yourname/Desktop/Gradio Layout Visualizer.desktop`
- Applications: `/home/yourname/.local/share/applications/Gradio Layout Visualizer.desktop`

### Removal

**Uninstall shortcuts:**
```bash
python -m gradio_layout_visualizer.install_shortcuts --remove
```

### Technical Details
- Uses `pyshortcuts` for cross-platform compatibility
- Automatically finds Python executable and script paths
- Creates proper file associations
- Terminal window opens to show output (can be configured)

---

## 🧪 3. Automated UI Testing with Playwright

### What It Does
Provides comprehensive UI/UX testing to ensure the enhanced controls and interface work correctly across browsers.

### Why It Matters
- ✅ **Catch regressions** - Ensure new features don't break existing ones
- ✅ **Cross-browser testing** - Works on Chrome, Firefox, Safari
- ✅ **Visual validation** - Test actual user interactions
- ✅ **CI/CD ready** - Automate testing in pipelines
- ✅ **Accessibility checks** - Ensure keyboard navigation works

### Quick Start

**Run all tests:**
```bash
python run_tests.py
```

**Run specific test file:**
```bash
pytest tests/test_ui_enhanced_controls.py
```

**Run with headed browser (see what's happening):**
```bash
pytest tests/test_ui_enhanced_controls.py --headed
```

**Run specific test:**
```bash
pytest tests/test_ui_enhanced_controls.py::TestEnhancedControls::test_color_picker_for_button
```

### Test Coverage

#### Enhanced Controls Tests (`test_ui_enhanced_controls.py`)

**Basic Functionality:**
- ✅ Page loads successfully
- ✅ Component addition buttons visible
- ✅ Components can be added
- ✅ Configuration panel appears

**Enhanced Controls:**
- ✅ Color pickers appear for color parameters
- ✅ Checkboxes/toggles appear for boolean parameters
- ✅ Sliders appear for numeric parameters with ranges
- ✅ Documentation links are present

**User Experience:**
- ✅ Variable names are editable
- ✅ Save & Render button works
- ✅ Multiple components can be added

**Responsiveness:**
- ✅ Mobile viewport (375x667)
- ✅ Tablet viewport (768x1024)
- ✅ Desktop viewport (1920x1080)

**Accessibility:**
- ✅ Keyboard navigation works
- ✅ ARIA labels present
- ✅ Focus management

### Test Architecture

```
tests/
├── __init__.py
├── conftest.py                      # Pytest configuration & fixtures
├── test_app.py                      # Minimal app for testing
└── test_ui_enhanced_controls.py     # UI tests for controls
```

**Key Fixtures:**
```python
@pytest.fixture
def visualizer_server():
    """Starts the visualizer server for testing"""
    # Automatically starts server on available port
    # Waits for server to be ready
    # Cleans up after tests

@pytest.fixture
def visualizer_page(page, visualizer_server):
    """Navigates to visualizer and waits for load"""
    # Returns Playwright Page object ready for testing
```

### Writing New Tests

**Example test:**
```python
def test_new_feature(visualizer_page: Page):
    """Test description"""
    # Add component
    visualizer_page.get_by_role("button", name="Textbox").click()

    # Wait for UI update
    visualizer_page.wait_for_timeout(1000)

    # Check expected element
    element = visualizer_page.get_by_text("Expected Text")
    expect(element).to_be_visible()
```

### CI/CD Integration

**GitHub Actions example:**
```yaml
name: UI Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -e .
          playwright install chromium
      - name: Run tests
        run: python run_tests.py
```

### Debugging Tests

**Run with browser visible:**
```bash
pytest tests/ --headed
```

**Run with slow motion:**
```bash
pytest tests/ --headed --slowmo 1000
```

**Take screenshots on failure:**
```bash
pytest tests/ --screenshot on-failure
```

**Use Playwright Inspector:**
```bash
PWDEBUG=1 pytest tests/test_ui_enhanced_controls.py::test_name
```

---

## 🎯 Combined Workflow

All three features work together for the ultimate seamless experience:

### Typical User Journey

**First Time Setup:**
```bash
# 1. Clone and install
git clone https://github.com/yourname/Gradio_Layout_Visualizer.git
cd Gradio_Layout_Visualizer
pip install -e .

# 2. Create desktop shortcuts (one-time)
gradio-visualizer --install-shortcuts
```

**Daily Usage:**
```bash
# Option 1: Double-click desktop shortcut
# 🖱️ Click → Browser opens automatically → Start building!

# Option 2: Command line
gradio-visualizer my_app.py
# Browser opens automatically → Start building!
```

**Development:**
```bash
# Make changes to the code

# Run tests to verify everything works
python run_tests.py

# Launch to test manually (browser opens automatically)
gradio-visualizer
```

### Automation Levels

| Feature | Manual | Semi-Automated | Fully Automated |
|---------|--------|----------------|-----------------|
| **Launch App** | Open terminal, cd, activate venv, run command | Run command | Double-click icon |
| **Open Browser** | Copy URL, paste in browser | Click link | Opens automatically |
| **Testing** | Manual clicking | Automated UI tests | CI/CD pipeline |

---

## 🔧 Configuration

### Environment Variables

```bash
# Disable auto-browser-open globally
export GRADIO_INBROWSER=false

# Custom browser
export BROWSER=/path/to/browser
```

### Python Configuration

```python
# In your code
demo.launch(
    inbrowser=True,        # Auto-open browser
    share=False,           # Don't create share link
    server_port=7860,      # Custom port
    quiet=False,          # Show startup messages
)
```

---

## 📊 Performance Impact

### Auto-Browser-Open
- **Startup time:** +0.5-1.5 seconds (browser launch)
- **Memory:** +100-300MB (browser process)
- **Benefits:** Saves 5-10 seconds per session of manual URL opening

### Desktop Shortcuts
- **Installation time:** ~2 seconds (one-time)
- **Disk space:** <1KB per shortcut
- **Benefits:** Saves 10-30 seconds per session of navigation/commands

### UI Testing
- **Initial setup:** ~30 seconds (browser installation)
- **Per test run:** ~10-60 seconds (depending on test count)
- **Benefits:** Catches bugs before users encounter them

---

## 🐛 Troubleshooting

### Auto-Browser-Open Not Working

**Issue:** Browser doesn't open automatically

**Solutions:**
```bash
# Check if running in headless environment
echo $DISPLAY  # Linux: should show :0 or similar

# Try manual browser specification
BROWSER=firefox gradio-visualizer

# Check Gradio version
pip show gradio  # Should be >= 5.0.0
```

### Desktop Shortcuts Not Working

**Issue:** Shortcuts don't launch the app

**Solutions:**
```bash
# Reinstall shortcuts
gradio-visualizer --install-shortcuts

# Check if pyshortcuts is installed
pip show pyshortcuts

# Manually verify Python path in shortcut
# Open shortcut properties and check the command
```

### UI Tests Failing

**Issue:** Playwright tests fail

**Solutions:**
```bash
# Reinstall browsers
playwright install chromium

# Update dependencies
pip install --upgrade playwright pytest-playwright

# Run with debug output
pytest tests/ -v --tb=long

# Check if port is available
lsof -i :7861  # Should be empty
```

---

## 🚀 Future Enhancements

### Planned Features
- 🎯 **Smart port detection** - Auto-find available port if default is taken
- 🔄 **Auto-reload on file changes** - Hot reload for faster development
- 📸 **Screenshot automation** - Auto-capture screenshots for documentation
- 🎨 **Custom browser profiles** - Use specific browser configurations
- 🔒 **Secure defaults** - Auto-configure security settings

---

## 📚 Related Documentation

- [Enhanced Controls](./ENHANCED_CONTROLS.md) - Visual parameter controls
- [README](../README.md) - Project overview
- [ROADMAP](../ROADMAP.md) - Development roadmap
- [CHANGELOG](../CHANGELOG.md) - Version history

---

## 💡 Philosophy

These automation features embody our core principle:

> **"Users shouldn't have to think about the tool - it should just work."**

Every friction point removed is a better experience delivered. 🎯
