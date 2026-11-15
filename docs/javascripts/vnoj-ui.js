document.addEventListener("DOMContentLoaded", () => {
  const STORAGE_KEY = "vnoj_my_problems_progress";
  const getProgress = () => JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
  const setProgress = (data) => localStorage.setItem(STORAGE_KEY, JSON.stringify(data));

  const STATES = [
    { key: "todo", label: "⬜ Chưa làm", icon: "⬜" },
    { key: "trying", label: "🟨 Đang làm", icon: "🟨" },
    { key: "ac", label: "✅ Đã AC", icon: "✅" }
  ];

  // 1. Nút cập nhật trạng thái trong trang chi tiết bài tập
  const statusBtn = document.querySelector(".vnoj-status-btn");
  if (statusBtn) {
    const code = statusBtn.dataset.code;
    const renderBtn = () => {
      const cur = getProgress()[code] || "todo";
      const st = STATES.find(s => s.key === cur) || STATES[0];
      statusBtn.textContent = st.label;
    };
    renderBtn();
    statusBtn.addEventListener("click", () => {
      const prog = getProgress();
      const curIdx = STATES.findIndex(s => s.key === (prog[code] || "todo"));
      prog[code] = STATES[(curIdx + 1) % STATES.length].key;
      setProgress(prog);
      renderBtn();
    });
  }

  // 2. Tự động ghép Sample Input X và Sample Output X thành 2 cột cạnh nhau
  document.querySelectorAll("h2").forEach(h2 => {
    const text = h2.textContent.trim();
    const match = text.match(/^Sample Input\s*(\d*)$/i);
    if (match) {
      const idx = match[1];
      const inPre = h2.nextElementSibling;
      const outH2 = inPre ? inPre.nextElementSibling : null;
      const outPre = outH2 ? outH2.nextElementSibling : null;
      if (inPre && outH2 && outPre && outH2.textContent.trim().match(/^Sample Output/i)) {
        const grid = document.createElement("div");
        grid.className = "vnoj-sample-grid";
        grid.innerHTML = `
          <div class="vnoj-sample-box"><div class="vnoj-sample-title">Sample Input ${idx}</div></div>
          <div class="vnoj-sample-box"><div class="vnoj-sample-title">Sample Output ${idx}</div></div>
        `;
        grid.children[0].appendChild(inPre.cloneNode(true));
        grid.children[1].appendChild(outPre.cloneNode(true));
        h2.parentNode.insertBefore(grid, h2);
        h2.remove(); inPre.remove(); outH2.remove(); outPre.remove();
      }
    }
  });

  // 3. Bảng danh sách bài tập phân trang kiểu VNOJ ở trang chủ
  if (window.VNOJ_PROBLEMS && document.getElementById("vnoj-tbody")) {
    const PER_PAGE = 25;
    let currentPage = 1;
    const allProblems = window.VNOJ_PROBLEMS;
    const searchInput = document.getElementById("vnoj-search");
    const tagSelect = document.getElementById("vnoj-tag-filter");
    const statusSelect = document.getElementById("vnoj-status-filter");

    // Nạp danh sách tags vào bộ lọc
    const uniqueTags = [...new Set(allProblems.flatMap(p => p.tags))].sort();
    uniqueTags.forEach(t => {
      const opt = document.createElement("option");
      opt.value = t; opt.textContent = t;
      tagSelect.appendChild(opt);
    });

    const renderTable = () => {
      const q = searchInput.value.toLowerCase().trim();
      const tag = tagSelect.value;
      const stFilter = statusSelect.value;
      const prog = getProgress();

      const filtered = allProblems.filter(p => {
        const st = prog[p.code] || "todo";
        const matchQ = !q || p.code.toLowerCase().includes(q) || p.title.toLowerCase().includes(q) || p.tags.some(t => t.toLowerCase().includes(q));
        const matchTag = !tag || p.tags.includes(tag);
        const matchSt = !stFilter || st === stFilter;
        return matchQ && matchTag && matchSt;
      });

      const totalPages = Math.max(1, Math.ceil(filtered.length / PER_PAGE));
      if (currentPage > totalPages) currentPage = 1;
      const slice = filtered.slice((currentPage - 1) * PER_PAGE, currentPage * PER_PAGE);

      const tbody = document.getElementById("vnoj-tbody");
      tbody.innerHTML = slice.map(p => {
        const st = prog[p.code] || "todo";
        const icon = (STATES.find(s => s.key === st) || STATES[0]).icon;
        const pills = p.tags.map(t => `<span class="vnoj-pill" data-tag="${t}">${t}</span>`).join(" ");
        return `
          <tr>
            <td>${icon}</td>
            <td><a href="${p.url}"><strong>${p.code}</strong></a></td>
            <td><a href="${p.url}">${p.title}</a></td>
            <td>${pills}</td>
            <td>${p.time}</td>
            <td>${p.memory}</td>
          </tr>`;
      }).join("");

      const pagDiv = document.getElementById("vnoj-pagination");
      pagDiv.innerHTML = "";
      for (let i = 1; i <= totalPages; i++) {
        const btn = document.createElement("button");
        btn.className = `vnoj-page-btn ${i === currentPage ? "active" : ""}`;
        btn.textContent = i;
        btn.onclick = () => { currentPage = i; renderTable(); };
        pagDiv.appendChild(btn);
      }
    };

    [searchInput, tagSelect, statusSelect].forEach(el => {
      el.addEventListener("input", () => { currentPage = 1; renderTable(); });
    });
    renderTable();
  }
});
