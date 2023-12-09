use std::io::{self, BufRead};

fn sum_of_divisible_numbers(n: u64, d: u64) -> u64 {
    let num_terms = (n - 1) / d;
    let sum = num_terms * (2 * d + (num_terms - 1) * d) / 2;
    sum
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let t = stdin_iterator.next().unwrap().unwrap().trim().parse::<u64>().unwrap();

    for _ in 0..t {
        let n = stdin_iterator.next().unwrap().unwrap().trim().parse::<u64>().unwrap();
        let sum = sum_of_divisible_numbers(n,3) + 
            sum_of_divisible_numbers(n,5) - 
            sum_of_divisible_numbers(n,15);
        println!("{}", sum);
    }
}
