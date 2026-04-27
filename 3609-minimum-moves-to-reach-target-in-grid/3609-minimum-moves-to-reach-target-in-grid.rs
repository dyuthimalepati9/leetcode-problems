impl Solution {
    pub fn min_moves(sx: i32, sy: i32, tx: i32, ty: i32) -> i32 {
        use std::collections::HashMap;
        const INF: i64 = i64::MAX / 4;
        fn dfs(
            x: i64,
            y: i64,
            sx: i64,
            sy: i64,
            memo: &mut HashMap<(i64, i64), i64>,
        ) -> i64 {
            if x == sx && y == sy {
                return 0;
            }
            if x < sx || y < sy {
                return INF;
            }
            if x == 0 && y == 0 {
                return INF;
            }

            if let Some(&v) = memo.get(&(x, y)) {
                return v;
            }
            let best = if x > y {
                if x >= 2 * y {
                    if x & 1 == 1 {
                        INF
                    } else {
                        let t = dfs(x / 2, y, sx, sy, memo);
                        if t >= INF { INF } else { t + 1 }
                    }
                } else {
                    let t = dfs(x - y, y, sx, sy, memo);
                    if t >= INF { INF } else { t + 1 }
                }
            } else if y > x {
                if y >= 2 * x {
                    if y & 1 == 1 {
                        INF
                    } else {
                        let t = dfs(x, y / 2, sx, sy, memo);
                        if t >= INF { INF } else { t + 1 }
                    }
                } else {
                    let t = dfs(x, y - x, sx, sy, memo);
                    if t >= INF { INF } else { t + 1 }
                }
            } else {
                let a = dfs(0, y, sx, sy, memo);
                let b = dfs(x, 0, sx, sy, memo);
                let m = a.min(b);
                if m >= INF { INF } else { m + 1 }
            };
            memo.insert((x, y), best);
            best
        }
        let sx = sx as i64;
        let sy = sy as i64;
        let tx = tx as i64;
        let ty = ty as i64;
        let mut memo = HashMap::new();
        let ans = dfs(tx, ty, sx, sy, &mut memo);
        if ans >= INF { -1 } else { ans as i32 }
    }
}