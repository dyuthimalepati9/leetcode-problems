impl Solution {
    pub fn min_operations(grid: Vec<Vec<i32>>, x: i32) -> i32 {
        let n = grid.len();
        let m = grid[0].len();
        let total = (n * m) as i32;
        let mut freq = vec![0; 10001];
        let mut mn = grid[0][0];
        let mut mx = mn;
        for row in &grid {
            for &c in row {
                if (c - grid[0][0]) % x != 0 {
                    return -1;
                }
                freq[c as usize] += 1;
                mn = mn.min(c);
                mx = mx.max(c);
            }
        }
        let target = (total + 1) / 2;
        let mut acc = 0;
        let mut median = mn;
        let mut i = mn;
        while i <= mx {
            acc += freq[i as usize];
            if acc >= target {
                median = i;
                break;
            }
            i += x;
        }
        let mut ops = 0;
        let mut i = mn;
        while i <= mx {
            ops += ((i - median).abs() / x) * freq[i as usize];
            i += x;
        }
        ops
    }
}