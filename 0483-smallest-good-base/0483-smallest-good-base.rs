impl Solution {
    pub fn smallest_good_base(n: String) -> String {
        let num: u64 = n.parse().unwrap();
        let max_m = (num as f64).log2() as u32 + 1;
        for m in (1..=max_m).rev() {
            let mut left = 2_u64;
            let mut right = (num as f64).powf(1.0 / m as f64) as u64 + 1;
            while left <= right {
                let mid = left + (right - left) / 2;
                let mut sum = 0_u64;
                let mut curr = 1_u64;
                let mut overflow = false;
                for i in 0..=m {
                    sum = match sum.checked_add(curr) {
                        Some(val) => val,
                        None => {
                            overflow = true;
                            break;
                        }
                    };
                    if sum > num {
                        overflow = true;
                        break;
                    }
                    if i < m {
                        curr = match curr.checked_mul(mid) {
                            Some(val) => val,
                            None => {
                                overflow = true;
                                break;
                            }
                        };
                    }
                }
                if overflow {
                    right = mid - 1;
                } else if sum < num {
                    left = mid + 1;
                } else {
                    return mid.to_string();
                }
            }
        }
        
        (num - 1).to_string()
    }
}