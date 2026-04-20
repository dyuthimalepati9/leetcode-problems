impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        if height.is_empty() { return 0; }
        let (mut l, mut r) = (0, height.len() - 1);
        let (mut l_max, mut r_max, mut res) = (0, 0, 0);
        while l < r {
            if height[l] < height[r] {
                if height[l] >= l_max { l_max = height[l]; }
                else { res += l_max - height[l]; }
                l += 1;
            } else {
                if height[r] >= r_max { r_max = height[r]; }
                else { res += r_max - height[r]; }
                r -= 1;
            }
        }
        res
    }
}