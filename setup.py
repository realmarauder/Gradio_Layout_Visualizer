from setuptools import setup, find_packages

setup(
    name="gradio-layout-visualizer",
    version="0.1.0",
    description="An enhanced visual builder for Gradio with Avada-like capabilities",
    author="Gradio Layout Visualizer Team",
    packages=find_packages(),
    install_requires=[
        "gradio>=5.0.0",
        "huggingface-hub>=0.20.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "gradio-visualizer=gradio_layout_visualizer.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
