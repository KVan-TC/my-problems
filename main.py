import os
import re

def define_env(env):
    @env.macro
    def render_problem_table():
        problems_dir = os.path.join(env.project_dir, 'docs', 'problems')
        if not os.path.exists(problems_dir):
            return "*Chưa có bài tập nào.*"

        rows = []
        for filename in sorted(os.listdir(problems_dir)):
            if not filename.endswith('.md') or filename == 'index.md':
                continue

            filepath = os.path.join(problems_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            slug = filename[:-3]
            code = slug
            title = slug

            # 1. Lấy Mã bài và Tên bài từ dòng tiêu đề H1 (# CODE - Title hoặc # Title)
            h1_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if h1_match:
                h1_text = h1_match.group(1).strip()
                if ' - ' in h1_text:
                    code, title = [x.strip() for x in h1_text.split(' - ', 1)]
                elif ' – ' in h1_text:
                    code, title = [x.strip() for x in h1_text.split(' – ', 1)]
                else:
                    title = h1_text

            # 2. Lấy Thời gian, Bộ nhớ, Dạng bài / Tags từ các dòng metadata trong đề
            time_match = re.search(r'(?:Giới hạn thời gian|Time limit)[^:\n]*:\s*\**\s*([^\n*]+)', content, re.IGNORECASE)
            mem_match = re.search(r'(?:Giới hạn bộ nhớ|Memory limit)[^:\n]*:\s*\**\s*([^\n*]+)', content, re.IGNORECASE)
            tag_match = re.search(r'(?:Dạng bài|Tags?|Chủ đề)[^:\n]*:\s*\**\s*([^\n*]+)', content, re.IGNORECASE)

            time_limit = time_match.group(1).strip() if time_match else "1.0s"
            memory_limit = mem_match.group(1).strip() if mem_match else "256MB"

            if tag_match:
                raw_tags = [t.strip() for t in tag_match.group(1).split(',') if t.strip()]
                tags_str = ', '.join(f"`{t}`" for t in raw_tags)
            else:
                tags_str = ""

            link = f"problems/{slug}/"
            rows.append(f"| [**{code}**]({link}) | [{title}]({link}) | {tags_str} | {time_limit} | {memory_limit} |")

        if not rows:
            return "*Chưa có bài tập nào.*"

        header = (
            "| Mã bài | Tên bài | Dạng bài | Thời gian | Bộ nhớ |\n"
            "| :--- | :--- | :--- | :---: | :---: |\n"
        )
        return header + "\n".join(rows)
