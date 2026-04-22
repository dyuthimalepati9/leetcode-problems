impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let pricesSize = prices.len();
        if pricesSize <= 1 {
            return 0;
        }
        let mut buy1 = i32::MAX;  
        let mut buy2 = i32::MAX;  
        let mut profit1 = 0;       
        let mut sum_profit = 0;       
        for i in 0..pricesSize {
            if buy1 > prices[i] {
                buy1 = prices[i]; 
            }
            if profit1 < prices[i] - buy1 {
                profit1 = prices[i] - buy1; 
            }
            if buy2 > prices[i] - profit1 {
                buy2 = prices[i] - profit1; 
            }
            if sum_profit < prices[i] - buy2 {
                sum_profit = prices[i] - buy2; 
            }
        }
        return sum_profit;
    }
}