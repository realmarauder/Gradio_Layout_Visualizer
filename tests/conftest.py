"""Pytest configuration and fixtures for UI testing"""

import pytest
import subprocess
import time
import socket
from pathlib import Path


def is_port_in_use(port: int) -> bool:
    """Check if a port is already in use"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0


@pytest.fixture(scope="session")
def test_port():
    """Find an available port for testing"""
    port = 7861
    while is_port_in_use(port) and port < 7900:
        port += 1
    return port


@pytest.fixture(scope="session")
def visualizer_server(test_port):
    """Start the visualizer server for testing"""
    # Create a test app file
    test_dir = Path(__file__).parent
    test_app = test_dir / "test_app.py"
    test_config = test_dir / "test_app.json"

    # Start the server in background
    process = subprocess.Popen(
        [
            "python",
            "-m",
            "gradio_layout_visualizer.cli",
            str(test_app),
            "--port",
            str(test_port),
            "--no-browser",  # Don't open browser during tests
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Wait for server to start
    max_wait = 30  # seconds
    start_time = time.time()
    while time.time() - start_time < max_wait:
        if is_port_in_use(test_port):
            break
        time.sleep(0.5)
    else:
        process.kill()
        raise RuntimeError(f"Server failed to start on port {test_port}")

    yield f"http://localhost:{test_port}"

    # Cleanup
    process.terminate()
    process.wait(timeout=5)


@pytest.fixture
def visualizer_page(page, visualizer_server):
    """Navigate to the visualizer page"""
    page.goto(visualizer_server)
    page.wait_for_load_state("networkidle")
    return page
