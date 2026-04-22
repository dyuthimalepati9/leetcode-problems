fn getparent(p: &mut Vec<usize>, mut u: usize) -> usize {
    while p[u] != u {
        let pp = p[p[u]];
        p[u] = pp;
        u = p[u]
    }
    u
}
fn is_tree_after_one_removal(n: usize, edges: &Vec<Vec<i32>>) -> (bool, Option<Vec<i32>>) {
    let mut p = (0..n).collect::<Vec<usize>>();
    let mut res = None;
    for e in edges.iter() {
        let u = e[0] as usize -1;
        let v = e[1] as usize -1;
        let pu = getparent(&mut p, u);
        let pv = getparent(&mut p, v);
        if pu == pv  {
            if res.is_none() {
                res = Some(e)
            } else {
                return (false, None)
            }
        }
        p[pv] = pu; 
    }
    (true, res.cloned())
}
impl Solution {
    pub fn find_redundant_directed_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
        let n = edges.len();
        let mut incoming = vec![0; n];
        for e in edges.iter() {
            let v = e[1] as usize -1;
            incoming[v] += 1;
        }
        if let Some(v) = (0..n).filter(|i|incoming[*i]==2).next() {
            let ek = edges.iter().filter(|&e|e[1]==v as i32 + 1).cloned().collect::<Vec<Vec<i32>>>();
            for avoid in ek.into_iter().rev() {
                let ee = edges.iter().filter(|e| **e != avoid).cloned().collect::<Vec<_>>();
                if is_tree_after_one_removal(n, &ee) == (true, None) {
                    return avoid.clone()
                }
            }
        }
        if let (true, Some(e)) = is_tree_after_one_removal(n, &edges) {
            return e
        }
        unreachable!()
    }
}