impl Solution {
    pub fn calculate_z_array(s: &str) -> Vec<usize> {
        let length = s.len();
        let chars: Vec<char> = s.chars().collect();
        let mut z = vec![0; length];
        let (mut left, mut right) = (0, 0);

        for i in 1..length {
            if i < right {
                z[i] = std::cmp::min(right - i, z[i - left]);
            }
            while i + z[i] < length && chars[z[i]] == chars[i + z[i]] {
                z[i] += 1;
            }
            if i + z[i] > right {
                left = i;
                right = i + z[i];
            }
        }

        z
    }

    pub fn min_starting_index(text: String, pattern: String) -> i32 {
        // Combine pattern + text
        let combined = format!("{}{}", pattern, text);
        let forward_z = Self::calculate_z_array(&combined);

        // Reverse pattern and text
        let reversed_pattern: String = pattern.chars().rev().collect();
        let reversed_text: String = text.chars().rev().collect();
        let combined_reversed = format!("{}{}", reversed_pattern, reversed_text);
        let backward_z = Self::calculate_z_array(&combined_reversed);

        let total_length = forward_z.len();
        let pattern_length = pattern.len();

        let mut index = 2 * pattern_length;

        // Adjust index
        index = total_length - index;
        index = pattern_length + index;

        for i in pattern_length..total_length {
            if index >= total_length || index < pattern_length {
                break;
            }

            let forward_value = forward_z[i];
            let backward_value = backward_z[index];

            if forward_value + backward_value >= pattern_length - 1 {
                return (i - pattern_length) as i32;
            }

            if index == 0 { break; }
            index -= 1;
        }

        -1
    }
}