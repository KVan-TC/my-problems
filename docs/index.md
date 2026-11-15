# Danh sách bài tập

<input type="text" id="problemSearch" onkeyup="filterProblems()" placeholder="Tìm kiếm mã bài, tên bài hoặc dạng bài..." style="width: 100%; padding: 10px 14px; margin-bottom: 16px; border: 1px solid var(--md-default-fg-color--lighter); border-radius: 6px; background: var(--md-default-bg-color); color: var(--md-default-fg-color); font-size: 0.95rem;">

{{ render_problem_table() }}

<script>
function filterProblems() {
  const input = document.getElementById("problemSearch");
  const filter = input.value.toLowerCase();
  const table = document.querySelector(".md-typeset table");
  if (!table) return;
  const trs = table.querySelectorAll("tbody tr");
  trs.forEach(tr => {
    const text = tr.textContent.toLowerCase();
    tr.style.display = text.includes(filter) ? "" : "none";
  });
}
</script>
