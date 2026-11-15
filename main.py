import os
import re
import json
import yaml

def parse_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if match:
        meta = yaml.safe_load(match.group(1)) or {}
        body = match.group(2)
        return meta, body
    return {}, content

def define_env(env):
    @env.macro
    def render_problem_table():
        problems_dir = os.path.join(env.project_dir, 'docs', 'problems')
        problems = []
        if os.path.exists(problems_dir):
            for fname in sorted(os.listdir(problems_dir)):
                if fname.endswith('.md'):
                    fpath = os.path.join(problems_dir, fname)
                    meta, _ = parse_frontmatter(fpath)
                    code = meta.get('code', fname[:-3])
                    problems.append({
                        'code': code,
                        'title': meta.get('title', code),
                        'time': meta.get('time_limit', '1.0s'),
                        'memory': meta.get('memory_limit', '256MB'),
                        'tags': meta.get('tags', []),
                        'url': f'problems/{fname[:-3]}/'
                    })
        data_json = json.dumps(problems, ensure_ascii=False)
        return f"""
<div id="vnoj-problemset-app">
  <div class="vnoj-toolbar">
    <input type="text" id="vnoj-search" placeholder="Tìm theo mã bài, tên bài hoặc dạng bài...">
    <select id="vnoj-tag-filter"><option value="">Tất cả dạng bài</option></select>
    <select id="vnoj-status-filter">
      <option value="">Tất cả trạng thái</option>
      <option value="ac">Đã AC</option>
      <option value="trying">Đang làm</option>
      <option value="todo">Chưa làm</option>
    </select>
  </div>
  <div class="vnoj-table-wrapper">
    <table class="vnoj-table">
      <thead>
        <tr>
          <th style="width: 45px;">TT</th>
          <th style="width: 120px;">Mã bài</th>
          <th>Tên bài</th>
          <th>Dạng bài</th>
          <th style="width: 100px;">Thời gian</th>
          <th style="width: 100px;">Bộ nhớ</th>
        </tr>
      </thead>
      <tbody id="vnoj-tbody"></tbody>
    </table>
  </div>
  <div id="vnoj-pagination" class="vnoj-pagination"></div>
</div>
<script>window.VNOJ_PROBLEMS = {data_json};</script>
"""

def on_page_markdown(markdown, page, config, files):
    src_path = page.file.src_path
    if src_path.startswith('problems/') and src_path.endswith('.md'):
        full_path = os.path.join(config['docs_dir'], src_path)
        meta, body = parse_frontmatter(full_path)
        code = meta.get('code', os.path.basename(src_path)[:-3])
        title = meta.get('title', code)
        time_lim = meta.get('time_limit', '1.0s')
        mem_lim = meta.get('memory_limit', '256MB')
        tags = meta.get('tags', [])
        submit_url = meta.get('submit_url', '')

        tags_html = ''.join([f'<span class="vnoj-pill" data-tag="{t}">{t}</span>' for t in tags])
        submit_btn = (
            f'<a href="{submit_url}" target="_blank" rel="noopener" class="vnoj-submit-btn">'
            f'Gửi lời giải</a>'
            if submit_url else ''
        )

        oj_header = f"""
<div class="vnoj-problem-header">
  <div class="vnoj-header-top">
    <h1 class="vnoj-problem-title">{code} - {title}</h1>
    <div class="vnoj-actions">
      <button class="vnoj-status-btn" data-code="{code}" title="Đánh dấu tiến độ">Chưa làm</button>
      {submit_btn}
    </div>
  </div>
  <div class="vnoj-oj-meta">
    <span><strong>Giới hạn thời gian:</strong> {time_lim}</span>
    <span><strong>Giới hạn bộ nhớ:</strong> {mem_lim}</span>
    <span><strong>Input:</strong> standard input</span>
    <span><strong>Output:</strong> standard output</span>
  </div>
  <div class="vnoj-tags-bar"><strong>Dạng bài:</strong> {tags_html}</div>
</div>
"""
        # Tự động nhúng code từ thư mục solutions/<CODE>.cpp
        project_root = os.path.dirname(config['docs_dir'])
        sol_path = os.path.join(project_root, 'solutions', f'{code}.cpp')
        sol_section = ''
        if os.path.exists(sol_path):
            with open(sol_path, 'r', encoding='utf-8') as sf:
                cpp_code = sf.read().strip()
            sol_section = f"""

---

??? tip "💡 Hướng dẫn giải & Mã nguồn tham khảo (`solutions/{code}.cpp`)"
    ```cpp
{chr(10).join('    ' + line for line in cpp_code.splitlines())}
    ```
"""
        return oj_header + "\n" + body + sol_section
    return markdown
