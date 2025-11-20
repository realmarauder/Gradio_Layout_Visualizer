"""Enhanced parameter controls for better UX in component configuration"""

import inspect
from typing import Any, Callable, get_args, get_origin
import gradio as gr


# Common color parameter names
COLOR_PARAMS = {
    "color", "bg_color", "background_color", "text_color", "border_color",
    "fill_color", "accent_color", "primary_color", "secondary_color"
}

# Common boolean parameter names
BOOLEAN_PARAMS = {
    "visible", "interactive", "show_label", "show_copy_button", "container",
    "scale", "min_width", "rtl", "show_download_button", "show_share_button",
    "show_progress", "autoplay", "loop", "mirror_webcam", "include_audio"
}

# Parameters that should use sliders (with common ranges)
SLIDER_PARAMS = {
    "lines": (1, 20, 1),
    "max_lines": (1, 50, 1),
    "min_lines": (1, 20, 1),
    "height": (50, 1000, 10),
    "width": (50, 1000, 10),
    "scale": (0, 10, 1),
    "min_width": (0, 1000, 10),
    "every": (0.1, 60, 0.1),
    "maximum": (1, 1000, 1),
    "minimum": (0, 100, 1),
    "step": (0.01, 10, 0.01),
    "max_choices": (1, 20, 1),
    "min_choices": (1, 10, 1),
    "columns": (1, 12, 1),
    "rows": (1, 20, 1),
}


def get_param_type_info(component_class: type, param_name: str) -> dict[str, Any]:
    """
    Analyze a parameter and return information about its type and recommended control.

    Returns:
        dict with keys:
            - control_type: "color", "slider", "toggle", "dropdown", "textbox"
            - options: Additional options for the control (e.g., min/max for slider)
            - default: Default value if available
    """
    sig = inspect.signature(component_class.__init__)

    if param_name not in sig.parameters:
        return {"control_type": "textbox", "options": {}}

    param = sig.parameters[param_name]
    annotation = param.annotation
    default_value = param.default if param.default is not inspect.Parameter.empty else None

    # Check for color parameters
    if param_name.lower() in COLOR_PARAMS or "color" in param_name.lower():
        return {
            "control_type": "color",
            "options": {},
            "default": default_value
        }

    # Check annotation for bool type
    if annotation is bool or (get_origin(annotation) is type(None) and bool in get_args(annotation)):
        return {
            "control_type": "toggle",
            "options": {},
            "default": default_value if default_value is not None else False
        }

    # Check for known boolean parameters by name
    if param_name.lower() in BOOLEAN_PARAMS:
        return {
            "control_type": "toggle",
            "options": {},
            "default": default_value if default_value is not None else True
        }

    # Check annotation for int or float (numeric)
    if annotation in (int, float) or (get_origin(annotation) is type(None) and (int in get_args(annotation) or float in get_args(annotation))):
        # Check if we have predefined slider ranges
        if param_name in SLIDER_PARAMS:
            range_info = SLIDER_PARAMS[param_name]
            if range_info:
                min_val, max_val, step = range_info
                return {
                    "control_type": "slider",
                    "options": {"minimum": min_val, "maximum": max_val, "step": step},
                    "default": default_value if default_value is not None else min_val
                }

        # Generic numeric input
        return {
            "control_type": "number",
            "options": {},
            "default": default_value
        }

    # Check for literal/enum types (dropdown)
    origin = get_origin(annotation)
    if hasattr(annotation, "__args__"):
        args = get_args(annotation)
        # Check if it's a Literal type or similar
        if all(isinstance(arg, str) for arg in args):
            return {
                "control_type": "dropdown",
                "options": {"choices": list(args)},
                "default": default_value if default_value else args[0] if args else None
            }

    # Check for list types (could use tags input in future)
    if annotation is list or (origin is list):
        return {
            "control_type": "textbox",
            "options": {"placeholder": '["item1", "item2"]'},
            "default": default_value
        }

    # Default to textbox
    return {
        "control_type": "textbox",
        "options": {},
        "default": default_value
    }


def create_enhanced_control(
    param_name: str,
    param_info: dict[str, Any],
    current_value: Any,
    component_name: str
) -> gr.Component:
    """
    Create an enhanced control component based on parameter type.

    Args:
        param_name: Name of the parameter
        param_info: Info dict from get_param_type_info
        current_value: Current value of the parameter
        component_name: Name of the component (for docs link)

    Returns:
        Gradio component for controlling the parameter
    """
    control_type = param_info["control_type"]
    options = param_info["options"]

    # Documentation link
    doc_link = f"https://www.gradio.app/docs/gradio/{component_name.lower()}#param-{component_name.lower()}-{param_name.lower().replace('_', '-')}"
    info_text = f"<a href='{doc_link}' target='_blank'>docs</a>"

    # Determine display value
    if current_value == "":
        display_value = param_info.get("default", "")
    else:
        display_value = current_value

    if control_type == "color":
        # Color picker
        color_value = display_value if isinstance(display_value, str) else "#000000"
        return gr.ColorPicker(
            value=color_value,
            label=param_name,
            info=info_text
        )

    elif control_type == "toggle":
        # Toggle switch for boolean
        bool_value = display_value
        if isinstance(display_value, str):
            bool_value = display_value.lower() == "true"
        elif not isinstance(display_value, bool):
            bool_value = param_info.get("default", False)

        return gr.Checkbox(
            value=bool_value,
            label=param_name,
            info=info_text
        )

    elif control_type == "slider":
        # Slider for numeric with known range
        numeric_value = display_value
        if isinstance(display_value, str):
            try:
                numeric_value = float(display_value)
            except (ValueError, TypeError):
                numeric_value = options.get("minimum", 0)

        return gr.Slider(
            minimum=options["minimum"],
            maximum=options["maximum"],
            step=options["step"],
            value=numeric_value,
            label=param_name,
            info=info_text
        )

    elif control_type == "number":
        # Number input
        numeric_value = display_value
        if isinstance(display_value, str) and display_value:
            try:
                numeric_value = float(display_value)
            except (ValueError, TypeError):
                numeric_value = None

        return gr.Number(
            value=numeric_value,
            label=param_name,
            info=info_text
        )

    elif control_type == "dropdown":
        # Dropdown for enum/literal types
        choices = options.get("choices", [])
        return gr.Dropdown(
            choices=choices,
            value=display_value if display_value in choices else None,
            label=param_name,
            info=info_text,
            allow_custom_value=True
        )

    else:
        # Default textbox with helpful placeholder
        placeholder = options.get("placeholder", 'e.g. "value", 5, True, or ["list"]')
        return gr.Textbox(
            value=str(display_value) if display_value else "",
            label=param_name,
            info=info_text,
            placeholder=placeholder
        )


def format_value_for_storage(value: Any, control_type: str) -> str:
    """
    Format a value from an enhanced control for storage in the component kwargs.

    Args:
        value: The value from the control
        control_type: Type of control that produced the value

    Returns:
        Formatted string value for storage
    """
    if control_type == "color":
        return str(value) if value else ""

    elif control_type == "toggle":
        return str(value) if isinstance(value, bool) else ""

    elif control_type in ("slider", "number"):
        return str(value) if value is not None else ""

    elif control_type == "dropdown":
        return str(value) if value else ""

    else:
        return str(value) if value else ""
