use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let t = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    for _ in 0..t {
        let mut n = stdin_iterator.next().unwrap().unwrap().trim().parse::<i64>().unwrap();
        let mut pfs: Vec<i64> = vec![];
        while n % 2 == 0 {
            pfs.push(2);
            n = n / 2;
        }
    
        for i in 3..f64::sqrt(n as f64) as i64 {
            // While i divides n, print i and divide n
            while n % i == 0 {
                pfs.push(i);
                n = n / i;
            }
        }
    
        if n > 2 {
            pfs.push(n);
        }
        println!("{}", pfs.iter().max().unwrap());
    }
}
