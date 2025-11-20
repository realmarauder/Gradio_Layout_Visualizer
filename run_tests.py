#!/usr/bin/env python
"""Test runner for Gradio Layout Visualizer

Runs UI tests with Playwright and displays results.
"""

import subprocess
import sys
import os


def install_playwright_browsers():
    """Install Playwright browsers if not already installed"""
    print("📦 Checking Playwright browsers...")
    try:
        result = subprocess.run(
            ["playwright", "install", "chromium"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("✅ Playwright browsers ready")
        else:
            print("⚠️  Warning: Playwright browser installation may have issues")
            print(result.stderr)
    except FileNotFoundError:
        print("❌ Playwright not installed. Installing now...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "playwright"])
        subprocess.check_call(["playwright", "install", "chromium"])


def run_tests(args=None):
    """Run the test suite"""
    print("🎨 Gradio Layout Visualizer - Test Suite")
    print("=" * 60)

    # Install browsers if needed
    install_playwright_browsers()

    # Prepare pytest arguments
    pytest_args = ["pytest"]

    if args:
        pytest_args.extend(args)
    else:
        # Default: run all tests with detailed output
        pytest_args.extend(["-v", "--tb=short"])

    print(f"\n🧪 Running: {' '.join(pytest_args)}\n")

    # Run tests
    result = subprocess.run(pytest_args)

    # Summary
    print("\n" + "=" * 60)
    if result.returncode == 0:
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed")
        print(f"   Exit code: {result.returncode}")

    return result.returncode


if __name__ == "__main__":
    # Pass through command line arguments to pytest
    exit_code = run_tests(sys.argv[1:])
    sys.exit(exit_code)
