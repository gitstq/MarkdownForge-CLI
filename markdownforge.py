#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MarkdownForge-CLI
轻量级终端Markdown文档智能生成与优化引擎
Lightweight Terminal Markdown Document Intelligent Generation & Optimization Engine

Author: gitstq
Version: 1.0.0
License: MIT
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, asdict
from enum import Enum

__version__ = "1.0.0"
__author__ = "gitstq"


class FileType(Enum):
    """支持的文件类型"""
    PYTHON = ".py"
    JAVASCRIPT = ".js"
    TYPESCRIPT = ".ts"
    JAVA = ".java"
    GO = ".go"
    RUST = ".rs"
    CPP = ".cpp"
    C = ".c"
    MARKDOWN = ".md"
    HTML = ".html"
    CSS = ".css"
    JSON = ".json"
    YAML = ".yaml"
    TOML = ".toml"


@dataclass
class CodeElement:
    """代码元素"""
    type: str
    name: str
    line_start: int
    line_end: int
    docstring: str
    signature: str
    decorators: List[str]


@dataclass
class AnalysisResult:
    """分析结果"""
    file_path: str
    total_lines: int
    code_lines: int
    comment_lines: int
    blank_lines: int
    elements: List[CodeElement]
    complexity_score: float


@dataclass
class MarkdownMetrics:
    """Markdown文档指标"""
    total_lines: int
    heading_count: int
    code_block_count: int
    link_count: int
    image_count: int
    table_count: int
    readability_score: float
    structure_score: float


class CodeParser:
    """代码解析器"""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.content = ""
        self.lines = []
        self.elements = []

    def parse(self) -> AnalysisResult:
        """解析代码文件"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
                self.lines = self.content.split('\n')
        except Exception as e:
            raise ValueError(f"无法读取文件 {self.file_path}: {e}")

        file_ext = Path(self.file_path).suffix.lower()

        if file_ext == '.py':
            self._parse_python()
        elif file_ext in ['.js', '.ts']:
            self._parse_javascript()
        elif file_ext == '.java':
            self._parse_java()
        elif file_ext == '.go':
            self._parse_go()
        elif file_ext == '.rs':
            self._parse_rust()
        else:
            self._parse_generic()

        total_lines = len(self.lines)
        code_lines = sum(1 for line in self.lines if line.strip() and not line.strip().startswith('#'))
        comment_lines = sum(1 for line in self.lines if self._is_comment_line(line))
        blank_lines = total_lines - code_lines - comment_lines

        complexity = self._calculate_complexity()

        return AnalysisResult(
            file_path=self.file_path,
            total_lines=total_lines,
            code_lines=code_lines,
            comment_lines=comment_lines,
            blank_lines=blank_lines,
            elements=self.elements,
            complexity_score=complexity
        )

    def _is_comment_line(self, line: str) -> bool:
        """判断是否为注释行"""
        stripped = line.strip()
        return stripped.startswith('#') or stripped.startswith('//') or stripped.startswith('/*') or stripped.startswith('*')

    def _parse_python(self):
        """解析Python代码"""
        in_docstring = False
        docstring_delimiter = None
        current_class = None
        current_function = None
        decorators = []

        for i, line in enumerate(self.lines):
            stripped = line.strip()

            # 处理文档字符串
            if not in_docstring:
                if stripped.startswith('"""') or stripped.startswith("'''"):
                    in_docstring = True
                    docstring_delimiter = stripped[:3]
                    if len(stripped) > 3 and stripped.endswith(docstring_delimiter):
                        in_docstring = False
                    continue
            else:
                if docstring_delimiter in stripped:
                    in_docstring = False
                continue

            # 收集装饰器
            if stripped.startswith('@'):
                decorators.append(stripped)
                continue

            # 解析类定义
            class_match = re.match(r'^class\s+(\w+)\s*(?:\(([^)]*)\))?:', stripped)
            if class_match:
                class_name = class_match.group(1)
                current_class = class_name
                element = CodeElement(
                    type="class",
                    name=class_name,
                    line_start=i + 1,
                    line_end=i + 1,
                    docstring="",
                    signature=stripped,
                    decorators=decorators.copy()
                )
                self.elements.append(element)
                decorators = []
                continue

            # 解析函数定义
            func_match = re.match(r'^(?:async\s+)?def\s+(\w+)\s*\(([^)]*)\)', stripped)
            if func_match:
                func_name = func_match.group(1)
                current_function = func_name
                element = CodeElement(
                    type="method" if current_class else "function",
                    name=func_name,
                    line_start=i + 1,
                    line_end=i + 1,
                    docstring="",
                    signature=stripped,
                    decorators=decorators.copy()
                )
                self.elements.append(element)
                decorators = []
                continue

    def _parse_javascript(self):
        """解析JavaScript/TypeScript代码"""
        for i, line in enumerate(self.lines):
            stripped = line.strip()

            # 解析类定义
            class_match = re.match(r'^class\s+(\w+)', stripped)
            if class_match:
                element = CodeElement(
                    type="class",
                    name=class_match.group(1),
                    line_start=i + 1,
                    line_end=i + 1,
                    docstring="",
                    signature=stripped,
                    decorators=[]
                )
                self.elements.append(element)
                continue

            # 解析函数定义
            func_patterns = [
                r'^(?:export\s+)?(?:async\s+)?function\s+(\w+)',
                r'^(?:const|let|var)\s+(\w+)\s*=\s*(?:async\s+)?\(',
                r'^(\w+)\s*\([^)]*\)\s*{'
            ]
            for pattern in func_patterns:
                func_match = re.match(pattern, stripped)
                if func_match:
                    func_name = func_match.group(1)
                    element = CodeElement(
                        type="function",
                        name=func_name,
                        line_start=i + 1,
                        line_end=i + 1,
                        docstring="",
                        signature=stripped,
                        decorators=[]
                    )
                    self.elements.append(element)
                    break

    def _parse_java(self):
        """解析Java代码"""
        for i, line in enumerate(self.lines):
            stripped = line.strip()

            # 解析类定义
            class_match = re.match(r'^(?:public\s+|private\s+|protected\s+)?(?:abstract\s+)?class\s+(\w+)', stripped)
            if class_match:
                element = CodeElement(
                    type="class",
                    name=class_match.group(1),
                    line_start=i + 1,
                    line_end=i + 1,
                    docstring="",
                    signature=stripped,
                    decorators=[]
                )
                self.elements.append(element)
                continue

            # 解析方法定义
            method_match = re.match(r'^(?:public\s+|private\s+|protected\s+)?(?:static\s+)?\w+\s+(\w+)\s*\(', stripped)
            if method_match:
                element = CodeElement(
                    type="method",
                    name=method_match.group(1),
                    line_start=i + 1,
                    line_end=i + 1,
                    docstring="",
                    signature=stripped,
                    decorators=[]
                )
                self.elements.append(element)

    def _parse_go(self):
        """解析Go代码"""
        for i, line in enumerate(self.lines):
            stripped = line.strip()

            # 解析函数定义
            func_match = re.match(r'^func\s+(?:\([^)]*\)\s+)?(\w+)', stripped)
            if func_match:
                element = CodeElement(
                    type="function",
                    name=func_match.group(1),
                    line_start=i + 1,
                    line_end=i + 1,
                    docstring="",
                    signature=stripped,
                    decorators=[]
                )
                self.elements.append(element)

    def _parse_rust(self):
        """解析Rust代码"""
        for i, line in enumerate(self.lines):
            stripped = line.strip()

            # 解析结构体
            struct_match = re.match(r'^pub\s+struct\s+(\w+)', stripped)
            if struct_match:
                element = CodeElement(
                    type="struct",
                    name=struct_match.group(1),
                    line_start=i + 1,
                    line_end=i + 1,
                    docstring="",
                    signature=stripped,
                    decorators=[]
                )
                self.elements.append(element)
                continue

            # 解析函数
            fn_match = re.match(r'^(?:pub\s+)?fn\s+(\w+)', stripped)
            if fn_match:
                element = CodeElement(
                    type="function",
                    name=fn_match.group(1),
                    line_start=i + 1,
                    line_end=i + 1,
                    docstring="",
                    signature=stripped,
                    decorators=[]
                )
                self.elements.append(element)

    def _parse_generic(self):
        """通用解析"""
        pass

    def _calculate_complexity(self) -> float:
        """计算复杂度评分"""
        complexity = 0.0
        for line in self.lines:
            stripped = line.strip()
            # 简单的复杂度计算：控制流语句
            if any(keyword in stripped for keyword in ['if', 'for', 'while', 'switch', 'try', 'except']):
                complexity += 1
        return min(complexity / 10, 10.0)


class MarkdownAnalyzer:
    """Markdown文档分析器"""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.content = ""
        self.lines = []

    def analyze(self) -> MarkdownMetrics:
        """分析Markdown文档"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
                self.lines = self.content.split('\n')
        except Exception as e:
            raise ValueError(f"无法读取文件 {self.file_path}: {e}")

        total_lines = len(self.lines)
        heading_count = 0
        code_block_count = 0
        link_count = 0
        image_count = 0
        table_count = 0
        in_code_block = False

        for line in self.lines:
            stripped = line.strip()

            # 标题
            if re.match(r'^#{1,6}\s+', stripped):
                heading_count += 1

            # 代码块
            if stripped.startswith('```'):
                if not in_code_block:
                    code_block_count += 1
                    in_code_block = True
                else:
                    in_code_block = False

            # 链接
            link_count += len(re.findall(r'\[([^\]]+)\]\(([^)]+)\)', line))

            # 图片
            image_count += len(re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', line))

            # 表格
            if '|' in stripped and not in_code_block:
                if re.match(r'^\|.*\|$', stripped):
                    table_count += 1

        readability = self._calculate_readability()
        structure = self._calculate_structure_score(heading_count, total_lines)

        return MarkdownMetrics(
            total_lines=total_lines,
            heading_count=heading_count,
            code_block_count=code_block_count,
            link_count=link_count,
            image_count=image_count,
            table_count=table_count,
            readability_score=readability,
            structure_score=structure
        )

    def _calculate_readability(self) -> float:
        """计算可读性评分"""
        if not self.content:
            return 0.0

        # 简单的可读性指标
        avg_line_length = sum(len(line) for line in self.lines) / len(self.lines) if self.lines else 0

        # 较短的行通常更易读
        if avg_line_length < 50:
            return 9.0
        elif avg_line_length < 80:
            return 8.0
        elif avg_line_length < 120:
            return 6.0
        else:
            return 4.0

    def _calculate_structure_score(self, heading_count: int, total_lines: int) -> float:
        """计算结构评分"""
        if total_lines == 0:
            return 0.0

        # 标题密度
        heading_density = heading_count / total_lines * 100

        # 合理的标题密度在 2-10% 之间
        if 2 <= heading_density <= 10:
            return 9.0
        elif heading_density < 2:
            return 5.0
        else:
            return 7.0


class MarkdownGenerator:
    """Markdown文档生成器"""

    def __init__(self, analysis_result: AnalysisResult):
        self.analysis = analysis_result

    def generate(self) -> str:
        """生成Markdown文档"""
        file_name = Path(self.analysis.file_path).name
        file_ext = Path(self.analysis.file_path).suffix

        md_content = []

        # 标题
        md_content.append(f"# {file_name}")
        md_content.append("")

        # 文件信息
        md_content.append("## 📄 文件信息")
        md_content.append("")
        md_content.append(f"- **文件路径**: `{self.analysis.file_path}`")
        md_content.append(f"- **文件类型**: {file_ext}")
        md_content.append(f"- **总行数**: {self.analysis.total_lines}")
        md_content.append(f"- **代码行数**: {self.analysis.code_lines}")
        md_content.append(f"- **注释行数**: {self.analysis.comment_lines}")
        md_content.append(f"- **空行数**: {self.analysis.blank_lines}")
        md_content.append(f"- **复杂度评分**: {self.analysis.complexity_score:.2f}/10")
        md_content.append("")

        # 代码统计
        md_content.append("## 📊 代码统计")
        md_content.append("")
        md_content.append("```")
        md_content.append(f"总行数:     {self.analysis.total_lines:6d}")
        md_content.append(f"代码行数:   {self.analysis.code_lines:6d} ({self.analysis.code_lines/self.analysis.total_lines*100:.1f}%)")
        md_content.append(f"注释行数:   {self.analysis.comment_lines:6d} ({self.analysis.comment_lines/self.analysis.total_lines*100:.1f}%)")
        md_content.append(f"空行数:     {self.analysis.blank_lines:6d} ({self.analysis.blank_lines/self.analysis.total_lines*100:.1f}%)")
        md_content.append("```")
        md_content.append("")

        # 代码元素
        if self.analysis.elements:
            md_content.append("## 🔧 代码元素")
            md_content.append("")

            # 按类型分组
            classes = [e for e in self.analysis.elements if e.type == "class"]
            functions = [e for e in self.analysis.elements if e.type == "function"]
            methods = [e for e in self.analysis.elements if e.type == "method"]
            structs = [e for e in self.analysis.elements if e.type == "struct"]

            if classes:
                md_content.append("### 类定义")
                md_content.append("")
                for elem in classes:
                    md_content.append(f"#### `{elem.name}`")
                    md_content.append(f"- **位置**: 第 {elem.line_start} 行")
                    md_content.append(f"- **签名**: `{elem.signature}`")
                    if elem.decorators:
                        md_content.append(f"- **装饰器**: {', '.join(elem.decorators)}")
                    md_content.append("")

            if structs:
                md_content.append("### 结构体定义")
                md_content.append("")
                for elem in structs:
                    md_content.append(f"#### `{elem.name}`")
                    md_content.append(f"- **位置**: 第 {elem.line_start} 行")
                    md_content.append(f"- **签名**: `{elem.signature}`")
                    md_content.append("")

            if functions:
                md_content.append("### 函数定义")
                md_content.append("")
                for elem in functions:
                    md_content.append(f"#### `{elem.name}()`")
                    md_content.append(f"- **位置**: 第 {elem.line_start} 行")
                    md_content.append(f"- **签名**: `{elem.signature}`")
                    if elem.decorators:
                        md_content.append(f"- **装饰器**: {', '.join(elem.decorators)}")
                    md_content.append("")

            if methods:
                md_content.append("### 方法定义")
                md_content.append("")
                for elem in methods:
                    md_content.append(f"#### `{elem.name}()`")
                    md_content.append(f"- **位置**: 第 {elem.line_start} 行")
                    md_content.append(f"- **签名**: `{elem.signature}`")
                    if elem.decorators:
                        md_content.append(f"- **装饰器**: {', '.join(elem.decorators)}")
                    md_content.append("")

        # 生成时间
        md_content.append("---")
        md_content.append(f"*文档生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
        md_content.append(f"*由 MarkdownForge-CLI v{__version__} 自动生成*")

        return '\n'.join(md_content)


class MarkdownFormatter:
    """Markdown格式化器"""

    def __init__(self, content: str):
        self.content = content
        self.lines = content.split('\n')

    def format(self) -> str:
        """格式化Markdown内容"""
        formatted_lines = []
        in_code_block = False
        prev_was_heading = False

        for i, line in enumerate(self.lines):
            stripped = line.strip()

            # 代码块处理
            if stripped.startswith('```'):
                in_code_block = not in_code_block
                formatted_lines.append(stripped)
                continue

            if in_code_block:
                formatted_lines.append(line)
                continue

            # 标题规范化
            heading_match = re.match(r'^(#{1,6})\s*(.+)$', stripped)
            if heading_match:
                level = len(heading_match.group(1))
                title = heading_match.group(2).strip()
                # 确保标题前后有空行
                if formatted_lines and not prev_was_heading:
                    formatted_lines.append('')
                formatted_lines.append(f"{'#' * level} {title}")
                formatted_lines.append('')
                prev_was_heading = True
                continue

            prev_was_heading = False

            # 列表规范化
            list_match = re.match(r'^(\s*)[-*+]\s+(.+)$', stripped)
            if list_match:
                indent = list_match.group(1)
                content = list_match.group(2)
                formatted_lines.append(f"{indent}- {content}")
                continue

            # 有序列表规范化
            ordered_match = re.match(r'^(\s*)\d+[.)]\s+(.+)$', stripped)
            if ordered_match:
                indent = ordered_match.group(1)
                content = ordered_match.group(2)
                formatted_lines.append(f"{indent}1. {content}")
                continue

            # 链接规范化
            line = re.sub(r'\[([^\]]+)\]\s*\(([^)]+)\)', r'[\1](\2)', line)

            # 图片规范化
            line = re.sub(r'!\[([^\]]*)\]\s*\(([^)]+)\)', r'![\1](\2)', line)

            formatted_lines.append(line)

        # 清理多余空行
        result = '\n'.join(formatted_lines)
        result = re.sub(r'\n{3,}', '\n\n', result)

        return result.strip()


class MarkdownForge:
    """MarkdownForge主类"""

    def __init__(self):
        self.stats = {
            "processed_files": 0,
            "generated_docs": 0,
            "formatted_files": 0,
            "analyzed_files": 0
        }

    def code_to_markdown(self, file_path: str, output_path: Optional[str] = None) -> str:
        """将代码文件转换为Markdown文档"""
        parser = CodeParser(file_path)
        analysis = parser.parse()

        generator = MarkdownGenerator(analysis)
        markdown_content = generator.generate()

        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            self.stats["generated_docs"] += 1

        self.stats["processed_files"] += 1
        return markdown_content

    def format_markdown(self, file_path: str, output_path: Optional[str] = None) -> str:
        """格式化Markdown文档"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        formatter = MarkdownFormatter(content)
        formatted_content = formatter.format()

        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(formatted_content)
            self.stats["formatted_files"] += 1
        else:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(formatted_content)
            self.stats["formatted_files"] += 1

        self.stats["processed_files"] += 1
        return formatted_content

    def analyze_markdown(self, file_path: str) -> MarkdownMetrics:
        """分析Markdown文档"""
        analyzer = MarkdownAnalyzer(file_path)
        metrics = analyzer.analyze()
        self.stats["analyzed_files"] += 1
        self.stats["processed_files"] += 1
        return metrics

    def batch_process(self, directory: str, recursive: bool = False, 
                     file_extensions: Optional[List[str]] = None) -> Dict:
        """批量处理目录"""
        if file_extensions is None:
            file_extensions = ['.py', '.js', '.ts', '.java', '.go', '.rs', '.md']

        results = {
            "processed": [],
            "failed": [],
            "skipped": []
        }

        path = Path(directory)
        pattern = "**/*" if recursive else "*"

        for file_path in path.glob(pattern):
            if file_path.is_file() and file_path.suffix in file_extensions:
                try:
                    if file_path.suffix == '.md':
                        # 格式化Markdown
                        self.format_markdown(str(file_path))
                        results["processed"].append(str(file_path))
                    else:
                        # 转换为Markdown
                        output_path = file_path.with_suffix('.md')
                        self.code_to_markdown(str(file_path), str(output_path))
                        results["processed"].append(str(file_path))
                except Exception as e:
                    results["failed"].append({"file": str(file_path), "error": str(e)})

        return results

    def get_stats(self) -> Dict:
        """获取处理统计"""
        return self.stats.copy()


def create_cli():
    """创建命令行接口"""
    parser = argparse.ArgumentParser(
        prog='markdownforge',
        description='🚀 MarkdownForge-CLI - 轻量级终端Markdown文档智能生成与优化引擎',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  %(prog)s generate code.py                    # 将代码转换为Markdown
  %(prog)s generate code.py -o doc.md          # 指定输出文件
  %(prog)s format README.md                    # 格式化Markdown文件
  %(prog)s analyze README.md                   # 分析Markdown文档
  %(prog)s batch ./src --recursive             # 批量处理目录

更多信息: https://github.com/gitstq/MarkdownForge-CLI
        '''
    )

    parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')

    subparsers = parser.add_subparsers(dest='command', help='可用命令')

    # generate 命令
    gen_parser = subparsers.add_parser('generate', help='将代码文件转换为Markdown文档')
    gen_parser.add_argument('input', help='输入文件路径')
    gen_parser.add_argument('-o', '--output', help='输出文件路径')
    gen_parser.add_argument('--stats', action='store_true', help='显示详细统计信息')

    # format 命令
    fmt_parser = subparsers.add_parser('format', help='格式化Markdown文档')
    fmt_parser.add_argument('input', help='输入文件路径')
    fmt_parser.add_argument('-o', '--output', help='输出文件路径（默认覆盖原文件）')

    # analyze 命令
    ana_parser = subparsers.add_parser('analyze', help='分析Markdown文档质量')
    ana_parser.add_argument('input', help='输入文件路径')
    ana_parser.add_argument('--json', action='store_true', help='以JSON格式输出')

    # batch 命令
    batch_parser = subparsers.add_parser('batch', help='批量处理目录')
    batch_parser.add_argument('directory', help='目标目录')
    batch_parser.add_argument('-r', '--recursive', action='store_true', help='递归处理子目录')
    batch_parser.add_argument('-e', '--extensions', nargs='+', 
                             default=['.py', '.js', '.ts', '.md'],
                             help='处理的文件扩展名')
    batch_parser.add_argument('-o', '--output-dir', help='输出目录')

    return parser


def main():
    """主函数"""
    parser = create_cli()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    forge = MarkdownForge()

    try:
        if args.command == 'generate':
            print(f"🚀 正在生成Markdown文档: {args.input}")
            content = forge.code_to_markdown(args.input, args.output)

            if args.output:
                print(f"✅ 文档已生成: {args.output}")
            else:
                print(content)

            if args.stats:
                print(f"\n📊 处理统计: {forge.get_stats()}")

        elif args.command == 'format':
            print(f"🎨 正在格式化: {args.input}")
            forge.format_markdown(args.input, args.output)

            if args.output:
                print(f"✅ 已格式化并保存到: {args.output}")
            else:
                print(f"✅ 已格式化: {args.input}")

        elif args.command == 'analyze':
            print(f"🔍 正在分析: {args.input}")
            metrics = forge.analyze_markdown(args.input)

            if args.json:
                print(json.dumps(asdict(metrics), indent=2, ensure_ascii=False))
            else:
                print(f"\n📄 文档分析结果:")
                print(f"  总行数: {metrics.total_lines}")
                print(f"  标题数: {metrics.heading_count}")
                print(f"  代码块: {metrics.code_block_count}")
                print(f"  链接数: {metrics.link_count}")
                print(f"  图片数: {metrics.image_count}")
                print(f"  表格数: {metrics.table_count}")
                print(f"  可读性评分: {metrics.readability_score:.1f}/10")
                print(f"  结构评分: {metrics.structure_score:.1f}/10")

        elif args.command == 'batch':
            print(f"📁 批量处理目录: {args.directory}")
            results = forge.batch_process(args.directory, args.recursive, args.extensions)

            print(f"\n✅ 处理完成:")
            print(f"  成功: {len(results['processed'])} 个文件")
            print(f"  失败: {len(results['failed'])} 个文件")

            if results['failed']:
                print(f"\n❌ 失败的文件:")
                for item in results['failed']:
                    print(f"  - {item['file']}: {item['error']}")

        print(f"\n📊 总计处理: {forge.get_stats()['processed_files']} 个文件")

    except Exception as e:
        print(f"❌ 错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
