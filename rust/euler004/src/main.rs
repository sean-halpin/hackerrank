use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let t = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim()
        .parse::<i32>()
        .unwrap();

    for _ in 0..t {
        let n = stdin_iterator
            .next()
            .unwrap()
            .unwrap()
            .trim()
            .parse::<i32>()
            .unwrap();

        let lower_palindrome_limit = 101101;
        let higher_palindrome_limit = 1_000_000;
        let limit = if n < lower_palindrome_limit {
            lower_palindrome_limit
        } else if n > higher_palindrome_limit {
            higher_palindrome_limit
        } else {
            n
        };
        let digits = 3;
        let x: i32 = "9".repeat(digits).parse().unwrap();
        let y: i32 = "9".repeat(digits).parse().unwrap();

        let mut max: i32 = 0;
        for i in (1..=x).rev() {
            for j in (1..=y).rev() {
                let product: i32 = i * j;
                if product <= limit && product > max {
                    let product_string: String = product.to_string();
                    let reversed_product_string: String =
                        product.to_string().chars().rev().collect();
                    if product_string.eq(&reversed_product_string)
                        && product >= lower_palindrome_limit
                        && product < n
                    {
                        max = product;
                    }
                }
            }
        }
        println!("{}", max);
    }
}
