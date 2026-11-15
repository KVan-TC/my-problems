import os
import yaml
from collections import defaultdict

def define_env(env):
    @env.macro
    def problem_tabs():
        problems_dir = os.path.join(env.project_dir, "docs", "problems")
        all_rows = []
        tag_groups = defaultdict(list)

        if os.path.exists(problems_dir):
            for root, _, files in os.walk(problems_dir):
                for file in sorted(files):
                    if not file.endswith(".md"):
                        continue
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, os.path.join(env.project_dir, "docs")).replace("\\", "/")

                    meta = {}
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                        if content.startswith("---"):
                            parts = content.split("---", 2)
                            if len(parts) >= 3:
                                meta = yaml.safe_load(parts[1]) or {}

                    code = meta.get("code", file[:-3])
                    title = meta.get("title", code)
                    raw_tags = meta.get("tags", "")
                    limits = meta.get("limits", "1.0s / 256MB")

                    if isinstance(raw_tags, str):
                        tags_list = [t.strip() for t in raw_tags.split(",") if t.strip()]
                    elif isinstance(raw_tags, list):
                        tags_list = [str(t).strip() for t in raw_tags if str(t).strip()]
                    else:
                        tags_list = []

                    tags_display = ", ".join(tags_list) if tags_list else "-"
                    row_str = f"    | [{code}]({rel_path}) | {title} | {tags_display} | {limits} |"

                    all_rows.append(row_str)
                    for tag in tags_list:
                        tag_groups[tag].append(row_str)

        header = [
            "    | Mã bài | Tên bài | Chủ đề (Tags) | Giới hạn |",
            "    | :--- | :--- | :--- | :--- |"
        ]

        output = ['=== "Tất cả"'] + header + all_rows + [""]

        for tag in sorted(tag_groups.keys()):
            output.append(f'=== "{tag}"')
            output.extend(header)
            output.extend(tag_groups[tag])
            output.append("")

        return "\n".join(output)
