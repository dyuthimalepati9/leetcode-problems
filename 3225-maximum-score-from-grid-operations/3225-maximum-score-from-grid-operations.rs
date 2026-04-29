impl Solution {
    pub fn maximum_score(grid: Vec<Vec<i32>>) -> i64 {
        let n = grid.len();
        let mut pref = vec![vec![0i64; n + 1]; n];
        for j in 0..n {
            for i in 0..n {
                pref[j][i + 1] = pref[j][i] + grid[i][j] as i64;
            }
        }
        let mut dp = vec![vec![i64::MIN; n + 1]; 2];
        for h in 0..=n {
            dp[0][h] = 0;
        }
        for j in 1..n {
            let mut new_dp = vec![vec![i64::MIN; n + 1]; 2];
            let mut p_max = i64::MIN;
            for h in 0..=n {
                p_max = p_max.max(dp[0][h] - pref[j - 1][h]);
                new_dp[0][h] = new_dp[0][h].max(p_max + pref[j - 1][h]);
            }
            p_max = i64::MIN;
            for h in (0..=n).rev() {
                p_max = p_max.max(dp[0][h]).max(dp[1][h]);
                new_dp[1][h] = new_dp[1][h].max(p_max);
            }
            p_max = i64::MIN;
            for h in (0..=n).rev() {
                p_max = p_max.max(dp[0][h]).max(dp[1][h]);
                new_dp[0][0] = new_dp[0][0].max(p_max);
            }
            p_max = i64::MIN;
            for h in (0..=n).rev() {
                p_max = p_max
                    .max(dp[0][h] + pref[j][h])
                    .max(dp[1][h] + pref[j][h]);
                new_dp[1][h] = new_dp[1][h].max(p_max - pref[j][h]);
            }
            p_max = i64::MIN;
            for h in 0..=n {
                p_max = p_max.max(dp[1][h]);
                new_dp[1][h] = new_dp[1][h].max(p_max);
            }
            p_max = i64::MIN;
            for h in 0..=n {
                p_max = p_max.max(dp[0][h]).max(dp[1][h]);
                new_dp[0][h] = new_dp[0][h].max(p_max);
            }
            dp = new_dp;
        }
        let mut res = 0i64;
        for state in 0..2 {
            for h in 0..=n {
                res = res.max(dp[state][h]);
            }
        }
        res
    }
}