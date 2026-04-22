impl Solution {
    pub fn two_edit_words(queries: Vec<String>, dictionary: Vec<String>) -> Vec<String> {
        let mut ans : Vec<String> = Vec::new();
        for i in 0..queries.len(){
            let q = queries[i].as_bytes();
            'outer : for j in 0..dictionary.len(){
                let mut dif = 0;
                let d = dictionary[j].as_bytes();
                for k in 0..d.len(){
                    if q[k] != d[k]{
                        dif += 1;
                    }
                    if dif > 2{
                        continue 'outer;
                    }
                }
                ans.push(queries[i].clone());
                break;
            }
        } 
        ans
    }
}