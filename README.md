<div align="center">

# 🚀 MarkdownForge-CLI

**轻量级终端Markdown文档智能生成与优化引擎**

*Lightweight Terminal Markdown Document Intelligent Generation & Optimization Engine*

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Zero-Dependencies-orange)](requirements.txt)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)]()

[简体中文](#-简体中文) | [繁體中文](#-繁體中文) | [English](#-english)

</div>

---

## 📖 简体中文

### 🎉 项目介绍

**MarkdownForge-CLI** 是一款专为开发者打造的轻量级终端工具，能够智能地将代码文件转换为结构清晰的Markdown文档，并提供文档格式化、质量分析等一站式解决方案。

#### 💡 核心痛点
- 📚 代码文档化耗时费力，维护困难
- 🎨 Markdown格式不统一，可读性差
- 📊 缺乏文档质量评估手段
- 🔧 批量处理代码文档效率低下

#### ✨ 自研差异化亮点
- **零依赖设计** - 纯Python标准库实现，无需安装任何第三方包
- **多语言支持** - 支持Python、JavaScript、TypeScript、Java、Go、Rust等主流语言
- **智能解析** - 自动识别类、函数、方法等代码元素
- **质量评分** - 提供可读性和结构评分，帮助优化文档
- **批量处理** - 支持整个目录的批量转换和格式化

### ✨ 核心特性

| 特性 | 描述 | 状态 |
|------|------|------|
| 📝 **代码转文档** | 自动从代码生成Markdown文档 | ✅ |
| 🎨 **文档格式化** | 规范化Markdown格式，统一风格 | ✅ |
| 📊 **质量分析** | 可读性评分、结构分析 | ✅ |
| 📁 **批量处理** | 支持目录递归处理 | ✅ |
| 🌐 **多语言** | Python/JS/TS/Java/Go/Rust等 | ✅ |
| ⚡ **零依赖** | 纯标准库实现 | ✅ |

### 🚀 快速开始

#### 环境要求
- **Python**: 3.7 或更高版本
- **操作系统**: Windows / macOS / Linux

#### 安装步骤

**方式一：直接下载使用（推荐）**
```bash
# 克隆仓库
git clone https://github.com/gitstq/MarkdownForge-CLI.git
cd MarkdownForge-CLI

# 直接使用
python markdownforge.py --help
```

**方式二：安装到系统**
```bash
# 安装
pip install .

# 使用命令
markdownforge --help
```

#### 基本使用

```bash
# 将代码文件转换为Markdown文档
python markdownforge.py generate example.py -o docs/example.md

# 格式化Markdown文档
python markdownforge.py format README.md

# 分析Markdown文档质量
python markdownforge.py analyze README.md

# 批量处理整个目录
python markdownforge.py batch ./src --recursive
```

### 📖 详细使用指南

#### 1️⃣ 代码转文档 (generate)

```bash
# 基本用法
markdownforge generate code.py

# 指定输出文件
markdownforge generate code.py -o documentation.md

# 显示详细统计
markdownforge generate code.py --stats
```

**支持的文件类型：**
- Python (`.py`)
- JavaScript (`.js`)
- TypeScript (`.ts`)
- Java (`.java`)
- Go (`.go`)
- Rust (`.rs`)
- C/C++ (`.c`, `.cpp`)
- Markdown (`.md`)

#### 2️⃣ 文档格式化 (format)

```bash
# 格式化并覆盖原文件
markdownforge format README.md

# 格式化并保存到新文件
markdownforge format README.md -o README_formatted.md
```

**格式化功能：**
- 统一标题格式（`# Title`）
- 规范化列表符号
- 优化链接和图片格式
- 清理多余空行

#### 3️⃣ 文档分析 (analyze)

```bash
# 标准输出
markdownforge analyze README.md

# JSON格式输出
markdownforge analyze README.md --json
```

**分析指标：**
- 总行数、标题数、代码块数
- 链接数、图片数、表格数
- 可读性评分（0-10）
- 结构评分（0-10）

#### 4️⃣ 批量处理 (batch)

```bash
# 处理当前目录
markdownforge batch .

# 递归处理子目录
markdownforge batch ./src --recursive

# 指定文件类型
markdownforge batch ./src -e .py .js .md

# 指定输出目录
markdownforge batch ./src -o ./docs
```

### 💡 设计思路与迭代规划

#### 🎯 设计理念
1. **简洁至上** - 零依赖，开箱即用
2. **开发者优先** - 针对代码文档化场景深度优化
3. **可扩展性** - 模块化设计，易于添加新语言支持

#### 🗺️ 迭代路线图

| 版本 | 功能 | 预计时间 |
|------|------|----------|
| v1.1.0 | 支持更多语言（Ruby、PHP、Swift） | 2025-Q3 |
| v1.2.0 | 添加文档模板系统 | 2025-Q3 |
| v1.3.0 | 集成AI智能摘要 | 2025-Q4 |
| v2.0.0 | Web界面版本 | 2026-Q1 |

#### 🤝 贡献方向
- 添加新的编程语言支持
- 优化文档模板
- 改进分析算法
- 翻译文档

### 📦 打包与部署指南

#### 作为Python包安装

```bash
# 安装
pip install .

# 卸载
pip uninstall markdownforge-cli
```

#### 打包为可执行文件

```bash
# 安装PyInstaller
pip install pyinstaller

# 打包
pyinstaller --onefile markdownforge.py --name markdownforge

# 可执行文件位于 dist/markdownforge
```

#### 系统级安装（Linux/macOS）

```bash
# 复制到系统路径
sudo cp markdownforge.py /usr/local/bin/markdownforge
sudo chmod +x /usr/local/bin/markdownforge

# 现在可以直接使用
markdownforge --help
```

### 🤝 贡献指南

#### 提交PR
1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 推送分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

#### 提交规范
- `feat:` 新功能
- `fix:` 修复问题
- `docs:` 文档更新
- `refactor:` 代码重构
- `test:` 测试相关

### 📄 开源协议

本项目采用 [MIT](LICENSE) 协议开源。

---

## 📖 繁體中文

### 🎉 專案介紹

**MarkdownForge-CLI** 是一款專為開發者打造的輕量級終端工具，能夠智能地將程式碼檔案轉換為結構清晰的Markdown文件，並提供文件格式化、品質分析等一站式解決方案。

#### 💡 核心痛點
- 📚 程式碼文件化耗時費力，維護困難
- 🎨 Markdown格式不統一，可讀性差
- 📊 缺乏文件品質評估手段
- 🔧 批次處理程式碼文件效率低下

#### ✨ 自研差異化亮點
- **零依賴設計** - 純Python標準庫實現，無需安裝任何第三方套件
- **多語言支援** - 支援Python、JavaScript、TypeScript、Java、Go、Rust等主流語言
- **智能解析** - 自動識別類別、函數、方法等程式碼元素
- **品質評分** - 提供可讀性和結構評分，幫助優化文件
- **批次處理** - 支援整個目錄的批次轉換和格式化

### ✨ 核心特性

| 特性 | 描述 | 狀態 |
|------|------|------|
| 📝 **程式碼轉文件** | 自動從程式碼生成Markdown文件 | ✅ |
| 🎨 **文件格式化** | 規範化Markdown格式，統一風格 | ✅ |
| 📊 **品質分析** | 可讀性評分、結構分析 | ✅ |
| 📁 **批次處理** | 支援目錄遞迴處理 | ✅ |
| 🌐 **多語言** | Python/JS/TS/Java/Go/Rust等 | ✅ |
| ⚡ **零依賴** | 純標準庫實現 | ✅ |

### 🚀 快速開始

#### 環境要求
- **Python**: 3.7 或更高版本
- **作業系統**: Windows / macOS / Linux

#### 安裝步驟

**方式一：直接下載使用（推薦）**
```bash
# 克隆倉庫
git clone https://github.com/gitstq/MarkdownForge-CLI.git
cd MarkdownForge-CLI

# 直接使用
python markdownforge.py --help
```

**方式二：安裝到系統**
```bash
# 安裝
pip install .

# 使用命令
markdownforge --help
```

#### 基本使用

```bash
# 將程式碼檔案轉換為Markdown文件
python markdownforge.py generate example.py -o docs/example.md

# 格式化Markdown文件
python markdownforge.py format README.md

# 分析Markdown文件品質
python markdownforge.py analyze README.md

# 批次處理整個目錄
python markdownforge.py batch ./src --recursive
```

### 📖 詳細使用指南

#### 1️⃣ 程式碼轉文件 (generate)

```bash
# 基本用法
markdownforge generate code.py

# 指定輸出檔案
markdownforge generate code.py -o documentation.md

# 顯示詳細統計
markdownforge generate code.py --stats
```

**支援的檔案類型：**
- Python (`.py`)
- JavaScript (`.js`)
- TypeScript (`.ts`)
- Java (`.java`)
- Go (`.go`)
- Rust (`.rs`)
- C/C++ (`.c`, `.cpp`)
- Markdown (`.md`)

#### 2️⃣ 文件格式化 (format)

```bash
# 格式化並覆蓋原檔案
markdownforge format README.md

# 格式化並儲存到新檔案
markdownforge format README.md -o README_formatted.md
```

**格式化功能：**
- 統一標題格式（`# Title`）
- 規範化列表符號
- 優化連結和圖片格式
- 清理多餘空行

#### 3️⃣ 文件分析 (analyze)

```bash
# 標準輸出
markdownforge analyze README.md

# JSON格式輸出
markdownforge analyze README.md --json
```

**分析指標：**
- 總行數、標題數、程式碼塊數
- 連結數、圖片數、表格數
- 可讀性評分（0-10）
- 結構評分（0-10）

#### 4️⃣ 批次處理 (batch)

```bash
# 處理當前目錄
markdownforge batch .

# 遞迴處理子目錄
markdownforge batch ./src --recursive

# 指定檔案類型
markdownforge batch ./src -e .py .js .md

# 指定輸出目錄
markdownforge batch ./src -o ./docs
```

### 💡 設計思路與迭代規劃

#### 🎯 設計理念
1. **簡潔至上** - 零依賴，開箱即用
2. **開發者優先** - 針對程式碼文件化場景深度優化
3. **可擴展性** - 模組化設計，易於添加新語言支援

#### 🗺️ 迭代路線圖

| 版本 | 功能 | 預計時間 |
|------|------|----------|
| v1.1.0 | 支援更多語言（Ruby、PHP、Swift） | 2025-Q3 |
| v1.2.0 | 添加文件模板系統 | 2025-Q3 |
| v1.3.0 | 整合AI智能摘要 | 2025-Q4 |
| v2.0.0 | Web介面版本 | 2026-Q1 |

#### 🤝 貢獻方向
- 添加新的程式語言支援
- 優化文件模板
- 改進分析演算法
- 翻譯文件

### 📦 打包與部署指南

#### 作為Python套件安裝

```bash
# 安裝
pip install .

# 解除安裝
pip uninstall markdownforge-cli
```

#### 打包為可執行檔案

```bash
# 安裝PyInstaller
pip install pyinstaller

# 打包
pyinstaller --onefile markdownforge.py --name markdownforge

# 可執行檔案位於 dist/markdownforge
```

#### 系統級安裝（Linux/macOS）

```bash
# 複製到系統路徑
sudo cp markdownforge.py /usr/local/bin/markdownforge
sudo chmod +x /usr/local/bin/markdownforge

# 現在可以直接使用
markdownforge --help
```

### 🤝 貢獻指南

#### 提交PR
1. Fork 本倉庫
2. 建立特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 推送分支 (`git push origin feature/AmazingFeature`)
5. 建立 Pull Request

#### 提交規範
- `feat:` 新功能
- `fix:` 修復問題
- `docs:` 文件更新
- `refactor:` 程式碼重構
- `test:` 測試相關

### 📄 開源協議

本專案採用 [MIT](LICENSE) 協議開源。

---

## 📖 English

### 🎉 Introduction

**MarkdownForge-CLI** is a lightweight terminal tool designed for developers that intelligently converts code files into well-structured Markdown documents, providing a one-stop solution for document formatting and quality analysis.

#### 💡 Pain Points
- 📚 Code documentation is time-consuming and hard to maintain
- 🎨 Inconsistent Markdown formatting reduces readability
- 📊 Lack of document quality assessment tools
- 🔧 Inefficient batch processing of code documentation

#### ✨ Differentiation Highlights
- **Zero Dependencies** - Pure Python standard library implementation
- **Multi-Language Support** - Python, JavaScript, TypeScript, Java, Go, Rust, and more
- **Smart Parsing** - Automatically identifies classes, functions, methods
- **Quality Scoring** - Readability and structure scoring for optimization
- **Batch Processing** - Supports batch conversion and formatting for entire directories

### ✨ Core Features

| Feature | Description | Status |
|---------|-------------|--------|
| 📝 **Code to Doc** | Auto-generate Markdown from code | ✅ |
| 🎨 **Doc Formatting** | Standardize Markdown format | ✅ |
| 📊 **Quality Analysis** | Readability & structure scoring | ✅ |
| 📁 **Batch Processing** | Recursive directory support | ✅ |
| 🌐 **Multi-Language** | Python/JS/TS/Java/Go/Rust/etc | ✅ |
| ⚡ **Zero Dependencies** | Pure standard library | ✅ |

### 🚀 Quick Start

#### Requirements
- **Python**: 3.7 or higher
- **OS**: Windows / macOS / Linux

#### Installation

**Option 1: Direct Download (Recommended)**
```bash
# Clone repository
git clone https://github.com/gitstq/MarkdownForge-CLI.git
cd MarkdownForge-CLI

# Use directly
python markdownforge.py --help
```

**Option 2: System Installation**
```bash
# Install
pip install .

# Use command
markdownforge --help
```

#### Basic Usage

```bash
# Convert code file to Markdown
python markdownforge.py generate example.py -o docs/example.md

# Format Markdown document
python markdownforge.py format README.md

# Analyze Markdown quality
python markdownforge.py analyze README.md

# Batch process directory
python markdownforge.py batch ./src --recursive
```

### 📖 Detailed Usage Guide

#### 1️⃣ Code to Document (generate)

```bash
# Basic usage
markdownforge generate code.py

# Specify output file
markdownforge generate code.py -o documentation.md

# Show detailed stats
markdownforge generate code.py --stats
```

**Supported File Types:**
- Python (`.py`)
- JavaScript (`.js`)
- TypeScript (`.ts`)
- Java (`.java`)
- Go (`.go`)
- Rust (`.rs`)
- C/C++ (`.c`, `.cpp`)
- Markdown (`.md`)

#### 2️⃣ Document Formatting (format)

```bash
# Format and overwrite original
markdownforge format README.md

# Format and save to new file
markdownforge format README.md -o README_formatted.md
```

**Formatting Features:**
- Standardize heading format (`# Title`)
- Normalize list symbols
- Optimize link and image format
- Clean up extra blank lines

#### 3️⃣ Document Analysis (analyze)

```bash
# Standard output
markdownforge analyze README.md

# JSON format output
markdownforge analyze README.md --json
```

**Analysis Metrics:**
- Total lines, headings, code blocks
- Links, images, tables count
- Readability score (0-10)
- Structure score (0-10)

#### 4️⃣ Batch Processing (batch)

```bash
# Process current directory
markdownforge batch .

# Recursive processing
markdownforge batch ./src --recursive

# Specify file types
markdownforge batch ./src -e .py .js .md

# Specify output directory
markdownforge batch ./src -o ./docs
```

### 💡 Design Philosophy & Roadmap

#### 🎯 Design Principles
1. **Simplicity First** - Zero dependencies, works out of the box
2. **Developer-Centric** - Optimized for code documentation workflows
3. **Extensibility** - Modular design for easy language additions

#### 🗺️ Roadmap

| Version | Feature | ETA |
|---------|---------|-----|
| v1.1.0 | More languages (Ruby, PHP, Swift) | 2025-Q3 |
| v1.2.0 | Document template system | 2025-Q3 |
| v1.3.0 | AI-powered smart summaries | 2025-Q4 |
| v2.0.0 | Web interface version | 2026-Q1 |

#### 🤝 Contribution Areas
- Add new programming language support
- Optimize document templates
- Improve analysis algorithms
- Translate documentation

### 📦 Packaging & Deployment

#### As Python Package

```bash
# Install
pip install .

# Uninstall
pip uninstall markdownforge-cli
```

#### Package as Executable

```bash
# Install PyInstaller
pip install pyinstaller

# Build
pyinstaller --onefile markdownforge.py --name markdownforge

# Executable at dist/markdownforge
```

#### System-wide Installation (Linux/macOS)

```bash
# Copy to system path
sudo cp markdownforge.py /usr/local/bin/markdownforge
sudo chmod +x /usr/local/bin/markdownforge

# Now ready to use
markdownforge --help
```

### 🤝 Contributing

#### Submitting PRs
1. Fork this repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'feat: Add some AmazingFeature'`)
4. Push branch (`git push origin feature/AmazingFeature`)
5. Create Pull Request

#### Commit Convention
- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation updates
- `refactor:` Code refactoring
- `test:` Testing related

### 📄 License

This project is open-sourced under the [MIT](LICENSE) License.

---

<div align="center">

**Made with ❤️ by gitstq**

[Report Bug](https://github.com/gitstq/MarkdownForge-CLI/issues) · [Request Feature](https://github.com/gitstq/MarkdownForge-CLI/issues)

</div>
