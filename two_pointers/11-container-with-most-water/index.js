/**
 * [Problem ref]{@link  https://leetcode.com/problems/container-with-most-water/}
 * @description You are given an integer array height of length n.
 * There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
 * Find two lines that together with the x-axis form a container, such that the container contains the most water.
 * Return the maximum amount of water a container can store.
 */

/**
 * @param {number[]} height
 * @return {number}
 */
const maxArea = function (height) {
  let area = 0;
  let l = 0;
  let r = height.length - 1;

  while (l < r) {
    area = Math.max(area, Math.min(height[l], height[r]) * (r - l));

    if (height[l] < height[r]) {
      l++;
    } else {
      r--;
    }
  }

  return area;
};
