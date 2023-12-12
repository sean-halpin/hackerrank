use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'pickingNumbers' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY a as parameter.
 */

fn pickingNumbers(a: &[i32]) -> i32 {
    let mut max: i32 = 0;
    for i in 0..a.len() {
        let first: i32 = a[i];
        let subset_within_one_pos: i32 = a.iter().filter(|&&n| (first - n) >= -1 && (first - n) <= 0).count() as i32;
        let subset_within_one_neg: i32 = a.iter().filter(|&&n| (first - n) >= 0 && (first - n) <= 1).count() as i32;
        let largest_subset_within_one = subset_within_one_pos.max(subset_within_one_neg);
        println!("{}, {}", first, largest_subset_within_one);
        if largest_subset_within_one > max {
            max = largest_subset_within_one
        }
    }
    max as i32
}

#[cfg(test)]
mod tests {
    use crate::pickingNumbers;

    #[test]
    fn assert_output() {
        let result: i32 = pickingNumbers(&vec![4, 6, 5, 3, 3, 1]);
        assert_eq!(result, 3);
    }
    #[test]
    fn assert_output_a() {
        let result: i32 = pickingNumbers(&vec![1, 2, 2, 3, 1, 2]);
        assert_eq!(result, 5);
    }
    #[test]
    fn assert_output_b() {
        let result: i32 = pickingNumbers(&vec![4,2,3,4,4,9,98,98,3,3,3,4,2,98,1,98,98,1,1,4,98,2,98,3,9,9,3,1,4,1,98,9,9,2,9,4,2,2,9,98,4,98,1,3,4,9,1,98,98,4,2,3,98,98,1,99,9,98,98,3,98,98,4,98,2,98,4,2,1,1,9,2,4]);
        assert_eq!(result, 22);
    }
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let n = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim()
        .parse::<i32>()
        .unwrap();

    let a: Vec<i32> = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim_end()
        .split(' ')
        .map(|s| s.to_string().parse::<i32>().unwrap())
        .collect();

    let result = pickingNumbers(&a);

    writeln!(&mut fptr, "{}", result).ok();
}
