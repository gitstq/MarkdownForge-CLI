#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MarkdownForge-CLI Setup Script
"""

from setuptools import setup, find_packages
from pathlib import Path

# 读取README
readme_path = Path(__file__).parent / "README.md"
long_description = ""
if readme_path.exists():
    long_description = readme_path.read_text(encoding='utf-8')

setup(
    name="markdownforge-cli",
    version="1.0.0",
    author="gitstq",
    author_email="",
    description="轻量级终端Markdown文档智能生成与优化引擎",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gitstq/MarkdownForge-CLI",
    py_modules=["markdownforge"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Processing :: Markup",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "markdownforge=markdownforge:main",
            "mdforge=markdownforge:main",
        ],
    },
    keywords="markdown documentation generator cli tool code-to-doc",
    project_urls={
        "Bug Reports": "https://github.com/gitstq/MarkdownForge-CLI/issues",
        "Source": "https://github.com/gitstq/MarkdownForge-CLI",
    },
)
