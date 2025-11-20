# Examples

This directory contains example Gradio apps that demonstrate common patterns and use cases for the Layout Visualizer.

## Available Examples

### `simple_chatbot.py`
A basic chatbot interface demonstrating:
- Chatbot component with message type
- Text input field
- Button event handlers

## How to Use Examples

### Option 1: Run Directly
```bash
python examples/simple_chatbot.py
```

### Option 2: Open in Visual Builder
```bash
gradio-visualizer examples/simple_chatbot.py
```

This will open the app in the enhanced visual builder where you can:
- ✨ See enhanced controls (color pickers, sliders, toggles)
- 🎨 Modify component properties visually
- 🔄 Save and render to see changes
- 📤 Deploy to HuggingFace Spaces

## Creating Your Own Examples

1. Create a new `.py` file in this directory
2. Write a standard Gradio app using `gr.Blocks()`
3. Open it with `gradio-visualizer your_file.py`
4. Use the visual builder to enhance it!

## Tips

- **Color Properties**: Now use color pickers instead of typing hex codes
- **Boolean Properties**: Toggle switches for true/false values
- **Numeric Ranges**: Sliders for properties like `lines`, `height`, `width`
- **Choices**: Dropdowns for enum-type parameters

Happy building! 🚀
