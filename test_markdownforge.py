#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MarkdownForge-CLI 测试文件
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

# 导入被测试模块
import markdownforge as mf


class TestCodeParser(unittest.TestCase):
    """测试代码解析器"""

    def setUp(self):
        """设置测试环境"""
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        """清理测试环境"""
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_parse_python_class(self):
        """测试解析Python类"""
        test_file = Path(self.test_dir) / "test.py"
        test_content = '''
class TestClass:
    """测试类文档字符串"""
    
    def __init__(self):
        self.value = 0
    
    def method(self):
        """方法文档字符串"""
        return self.value
'''
        test_file.write_text(test_content, encoding='utf-8')

        parser = mf.CodeParser(str(test_file))
        result = parser.parse()

        self.assertEqual(result.total_lines, 11)
        self.assertTrue(len(result.elements) > 0)
        
        classes = [e for e in result.elements if e.type == "class"]
        self.assertEqual(len(classes), 1)
        self.assertEqual(classes[0].name, "TestClass")

    def test_parse_python_function(self):
        """测试解析Python函数"""
        test_file = Path(self.test_dir) / "test_func.py"
        test_content = '''
def hello():
    """Say hello"""
    print("Hello")

def world():
    print("World")
'''
        test_file.write_text(test_content, encoding='utf-8')

        parser = mf.CodeParser(str(test_file))
        result = parser.parse()

        functions = [e for e in result.elements if e.type == "function"]
        self.assertEqual(len(functions), 2)

    def test_parse_javascript(self):
        """测试解析JavaScript"""
        test_file = Path(self.test_dir) / "test.js"
        test_content = '''
class MyClass {
    constructor() {
        this.value = 0;
    }
}

function testFunc() {
    return 42;
}
'''
        test_file.write_text(test_content, encoding='utf-8')

        parser = mf.CodeParser(str(test_file))
        result = parser.parse()

        self.assertTrue(len(result.elements) >= 1)


class TestMarkdownAnalyzer(unittest.TestCase):
    """测试Markdown分析器"""

    def setUp(self):
        """设置测试环境"""
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        """清理测试环境"""
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_analyze_markdown(self):
        """测试分析Markdown"""
        test_file = Path(self.test_dir) / "test.md"
        test_content = '''# Title

## Section 1

Some text here.

```python
print("hello")
```

## Section 2

[Link](https://example.com)

![Image](image.png)

| Col1 | Col2 |
|------|------|
| A    | B    |
'''
        test_file.write_text(test_content, encoding='utf-8')

        analyzer = mf.MarkdownAnalyzer(str(test_file))
        metrics = analyzer.analyze()

        self.assertEqual(metrics.heading_count, 3)
        self.assertEqual(metrics.code_block_count, 1)
        self.assertEqual(metrics.link_count, 1)
        self.assertEqual(metrics.image_count, 1)
        self.assertTrue(metrics.readability_score > 0)


class TestMarkdownFormatter(unittest.TestCase):
    """测试Markdown格式化器"""

    def test_format_headings(self):
        """测试格式化标题"""
        content = "#Title\n##  Section"
        formatter = mf.MarkdownFormatter(content)
        result = formatter.format()

        self.assertIn("# Title", result)
        self.assertIn("## Section", result)

    def test_format_lists(self):
        """测试格式化列表"""
        content = "- item1\n* item2\n+ item3"
        formatter = mf.MarkdownFormatter(content)
        result = formatter.format()

        self.assertIn("- item1", result)
        self.assertIn("- item2", result)
        self.assertIn("- item3", result)


class TestMarkdownGenerator(unittest.TestCase):
    """测试Markdown生成器"""

    def test_generate(self):
        """测试生成Markdown"""
        analysis = mf.AnalysisResult(
            file_path="/test/test.py",
            total_lines=100,
            code_lines=80,
            comment_lines=10,
            blank_lines=10,
            elements=[
                mf.CodeElement(
                    type="class",
                    name="TestClass",
                    line_start=1,
                    line_end=10,
                    docstring="Test class",
                    signature="class TestClass:",
                    decorators=[]
                )
            ],
            complexity_score=3.5
        )

        generator = mf.MarkdownGenerator(analysis)
        result = generator.generate()

        self.assertIn("# test.py", result)
        self.assertIn("TestClass", result)
        self.assertIn("100", result)


class TestMarkdownForge(unittest.TestCase):
    """测试MarkdownForge主类"""

    def setUp(self):
        """设置测试环境"""
        self.test_dir = tempfile.mkdtemp()
        self.forge = mf.MarkdownForge()

    def tearDown(self):
        """清理测试环境"""
        import shutil
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_code_to_markdown(self):
        """测试代码转Markdown"""
        test_file = Path(self.test_dir) / "sample.py"
        test_content = '''
def hello():
    print("Hello, World!")
'''
        test_file.write_text(test_content, encoding='utf-8')

        result = self.forge.code_to_markdown(str(test_file))

        self.assertIn("sample.py", result)
        self.assertIn("hello", result)
        self.assertEqual(self.forge.get_stats()["processed_files"], 1)

    def test_format_markdown(self):
        """测试格式化Markdown"""
        test_file = Path(self.test_dir) / "sample.md"
        test_content = "#Title\n##Section"
        test_file.write_text(test_content, encoding='utf-8')

        self.forge.format_markdown(str(test_file))

        formatted = test_file.read_text(encoding='utf-8')
        self.assertIn("# Title", formatted)

    def test_analyze_markdown(self):
        """测试分析Markdown"""
        test_file = Path(self.test_dir) / "analysis.md"
        test_content = "# Title\n\nSome content."
        test_file.write_text(test_content, encoding='utf-8')

        metrics = self.forge.analyze_markdown(str(test_file))

        self.assertIsInstance(metrics, mf.MarkdownMetrics)
        self.assertTrue(metrics.total_lines > 0)


def run_tests():
    """运行所有测试"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(TestCodeParser))
    suite.addTests(loader.loadTestsFromTestCase(TestMarkdownAnalyzer))
    suite.addTests(loader.loadTestsFromTestCase(TestMarkdownFormatter))
    suite.addTests(loader.loadTestsFromTestCase(TestMarkdownGenerator))
    suite.addTests(loader.loadTestsFromTestCase(TestMarkdownForge))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
