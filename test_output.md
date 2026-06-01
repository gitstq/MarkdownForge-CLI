# markdownforge.py

## 📄 文件信息

- **文件路径**: `markdownforge.py`
- **文件类型**: .py
- **总行数**: 834
- **代码行数**: 653
- **注释行数**: 43
- **空行数**: 138
- **复杂度评分**: 10.00/10

## 📊 代码统计

```
总行数:        834
代码行数:      653 (78.3%)
注释行数:       43 (5.2%)
空行数:        138 (16.5%)
```

## 🔧 代码元素

### 类定义

#### `FileType`
- **位置**: 第 28 行
- **签名**: `class FileType(Enum):`

#### `CodeElement`
- **位置**: 第 47 行
- **签名**: `class CodeElement:`
- **装饰器**: @dataclass

#### `AnalysisResult`
- **位置**: 第 59 行
- **签名**: `class AnalysisResult:`
- **装饰器**: @dataclass

#### `MarkdownMetrics`
- **位置**: 第 71 行
- **签名**: `class MarkdownMetrics:`
- **装饰器**: @dataclass

#### `CodeParser`
- **位置**: 第 83 行
- **签名**: `class CodeParser:`

#### `MarkdownAnalyzer`
- **位置**: 第 347 行
- **签名**: `class MarkdownAnalyzer:`

#### `MarkdownGenerator`
- **位置**: 第 447 行
- **签名**: `class MarkdownGenerator:`

#### `MarkdownFormatter`
- **位置**: 第 548 行
- **签名**: `class MarkdownFormatter:`

#### `MarkdownForge`
- **位置**: 第 620 行
- **签名**: `class MarkdownForge:`

### 方法定义

#### `__init__()`
- **位置**: 第 86 行
- **签名**: `def __init__(self, file_path: str):`

#### `parse()`
- **位置**: 第 92 行
- **签名**: `def parse(self) -> AnalysisResult:`

#### `_is_comment_line()`
- **位置**: 第 133 行
- **签名**: `def _is_comment_line(self, line: str) -> bool:`

#### `_parse_python()`
- **位置**: 第 138 行
- **签名**: `def _parse_python(self):`

#### `_parse_javascript()`
- **位置**: 第 203 行
- **签名**: `def _parse_javascript(self):`

#### `_parse_java()`
- **位置**: 第 245 行
- **签名**: `def _parse_java(self):`

#### `_parse_go()`
- **位置**: 第 279 行
- **签名**: `def _parse_go(self):`

#### `_parse_rust()`
- **位置**: 第 298 行
- **签名**: `def _parse_rust(self):`

#### `_parse_generic()`
- **位置**: 第 332 行
- **签名**: `def _parse_generic(self):`

#### `_calculate_complexity()`
- **位置**: 第 336 行
- **签名**: `def _calculate_complexity(self) -> float:`

#### `__init__()`
- **位置**: 第 350 行
- **签名**: `def __init__(self, file_path: str):`

#### `analyze()`
- **位置**: 第 355 行
- **签名**: `def analyze(self) -> MarkdownMetrics:`

#### `_calculate_readability()`
- **位置**: 第 412 行
- **签名**: `def _calculate_readability(self) -> float:`

#### `_calculate_structure_score()`
- **位置**: 第 430 行
- **签名**: `def _calculate_structure_score(self, heading_count: int, total_lines: int) -> float:`

#### `__init__()`
- **位置**: 第 450 行
- **签名**: `def __init__(self, analysis_result: AnalysisResult):`

#### `generate()`
- **位置**: 第 453 行
- **签名**: `def generate(self) -> str:`

#### `__init__()`
- **位置**: 第 551 行
- **签名**: `def __init__(self, content: str):`

#### `format()`
- **位置**: 第 555 行
- **签名**: `def format(self) -> str:`

#### `__init__()`
- **位置**: 第 623 行
- **签名**: `def __init__(self):`

#### `code_to_markdown()`
- **位置**: 第 631 行
- **签名**: `def code_to_markdown(self, file_path: str, output_path: Optional[str] = None) -> str:`

#### `format_markdown()`
- **位置**: 第 647 行
- **签名**: `def format_markdown(self, file_path: str, output_path: Optional[str] = None) -> str:`

#### `analyze_markdown()`
- **位置**: 第 667 行
- **签名**: `def analyze_markdown(self, file_path: str) -> MarkdownMetrics:`

#### `get_stats()`
- **位置**: 第 707 行
- **签名**: `def get_stats(self) -> Dict:`

#### `create_cli()`
- **位置**: 第 712 行
- **签名**: `def create_cli():`

---
*文档生成时间: 2026-06-01 02:09:40*
*由 MarkdownForge-CLI v1.0.0 自动生成*