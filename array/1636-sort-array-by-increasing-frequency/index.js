const frequencySort = function (nums) {
  const map = new Map();
  for (const n of nums) {
    map.set(n, (map.get(n) || 0) + 1);
  }
  return nums.sort((a, b) => map.get(a) - map.get(b) || b - a);
};
