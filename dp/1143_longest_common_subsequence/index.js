/**
 * [Problem ref]{@link https://leetcode.com/problems/longest-common-subsequence/}
 * @description Given two strings text1 and text2, 
 * return the length of their longest common subsequence. 
 * If there is no common subsequence, return 0.
 */

const longestCommonSubsequence = function (text1, text2) {
    let dp = new Array(text1.length + 1).fill(0).map(() => new Array(text2.length + 1).fill(0));

    for (let i = 1; i <= text1.length; i++) {
        for (let j = 1; j <= text2.length; j++) {
            if (text1[i - 1] === text2[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    return dp[text1.length][text2.length];
};