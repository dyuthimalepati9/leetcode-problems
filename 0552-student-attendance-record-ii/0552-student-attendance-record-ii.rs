use std::cmp;
impl Solution {
    pub fn check_record(n: i32) -> i32 {
        let modulo = 1000000007;
        let mut late_combos = vec![0 as u32; cmp::max(3, (n + 1) as usize)];
        late_combos[0] = 1;
        late_combos[1] = 2;
        late_combos[2] = 4;
        for i in 3..=(n as usize) {
            late_combos[i] = (late_combos[i-3] + late_combos[i-2] + late_combos[i-1]) % modulo
        }
        let mut ans: u64 = late_combos[n as usize] as u64;
        for a in 0..n as usize {
            ans += late_combos[a] as u64 * late_combos[n as usize - a - 1] as u64;
            ans %= modulo as u64
        }
        ans as i32
    }
}