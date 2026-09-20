#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""词频统计程序。

读取与脚本同目录下的 article.txt，统计每个单词出现的次数：
  * 忽略大小写（The 与 the 记为同一个单词）
  * 忽略标点（逗号、句号、引号、感叹号等都不算单词的一部分）
  * 按出现次数从高到低输出，次数相同时按字母顺序排列
"""

import re
from collections import Counter
from pathlib import Path

ARTICLE_FILE = "article.txt"

# 一个"单词" = 英文字母串，允许中间带一个撇号（如 don't、it's）
WORD_PATTERN = re.compile(r"[a-z]+(?:'[a-z]+)?")


def count_words(text):
    """把文本转成 单词 -> 次数 的字典。"""
    words = WORD_PATTERN.findall(text.lower())
    return Counter(words)


def main():
    # 用脚本所在目录定位 article.txt，这样在任意目录下运行都能找到
    article_path = Path(__file__).resolve().parent / ARTICLE_FILE

    if not article_path.is_file():
        print(f"错误：找不到文件 {article_path}")
        print(f"请在该目录下新建 {ARTICLE_FILE} 后再运行。")
        return 1

    # 优先按 UTF-8 读取（utf-8-sig 可自动去掉记事本写入的 BOM）；
    # 若文件是 ANSI/GBK 保存的，再退回 GBK 读，避免新手常见的中文编码报错
    try:
        text = article_path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        text = article_path.read_text(encoding="gbk", errors="replace")
    counts = count_words(text)

    if not counts:
        print("未在文件中统计到任何单词。")
        return 0

    # 次数降序；次数相同则按单词字母序，保证输出稳定
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    word_width = max(len(word) for word, _ in ranked)
    count_width = max(len(str(n)) for _, n in ranked)
    total = sum(counts.values())
    print(f"共 {len(counts)} 个不同单词，总计 {total} 个单词\n")
    for word, n in ranked:
        print(f"{word:<{word_width}}  {n:>{count_width}}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
