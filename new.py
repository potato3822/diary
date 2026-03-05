#!/usr/bin/env python3
import sys
from datetime import datetime
from pathlib import Path


def main() -> None:
    """
    使用方法:
        python new_post.py "2.28-a"

    功能:
        - 自动使用今天的日期生成文件名: YYYY-MM-DD-标题.md
        - 在文件头写入当前日期时间 (精确到秒)，方便区分一天内多篇日记
    """
    if len(sys.argv) < 2:
        print(f"用法: {Path(sys.argv[0]).name} \"标题(例如: 2.28-a)\"")
        sys.exit(1)

    title = sys.argv[1]

    # 当前日期和时间
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")  # 用于文件名和 date 字段的日期部分
    datetime_str = now.strftime("%Y-%m-%d %H:%M:%S")  # 如果你想在正文里用也可以

    posts_dir = Path("_posts")
    posts_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{date_str}-{title}.md"
    full_path = posts_dir / filename

    if full_path.exists():
        print(f"文件已存在: {full_path}")
        sys.exit(1)

    # 写入和你现有文件类似的头部
    front_matter = f"""---
title: "{title}"
date: {date_str}
layout: post
---

"""

    full_path.write_text(front_matter, encoding="utf-8")

    print(f"已创建: {full_path}")
    print(f"当前时间: {datetime_str}")


if __name__ == "__main__":
    main()

