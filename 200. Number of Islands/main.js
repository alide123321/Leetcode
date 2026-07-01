/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  if (!grid || grid.length === 0) return 0;

  const m = grid.length;
  const n = grid[0].length;

  const visited = new Set();
  let numOfIslands = 0;

  for (let r = 0; r < m; ++r) {
    for (let c = 0; c < n; ++c) {
      const key = `${r},${c}`;
      if (grid[r][c] === "0" || visited.has(key)) continue;

      ++numOfIslands;
      dfs(r, c);
    }
  }

  return numOfIslands;

  function dfs(r, c) {
    if (r < 0 || c < 0 || r >= m || c >= n) return;
    if (grid[r][c] === "0") return;

    const key = `${r},${c}`;
    if (visited.has(key)) return;
    visited.add(key);

    dfs(r + 1, c);
    dfs(r - 1, c);
    dfs(r, c + 1);
    dfs(r, c - 1);
  }
};
