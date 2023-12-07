use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'divisibleSumPairs' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. INTEGER_ARRAY ar
 */

fn divisibleSumPairs(n: i32, k: i32, ar: &[i32]) -> i32 {
    let mut pairs: Vec<(i32,i32)> = Vec::<(i32,i32)>::new();
    for i in (0..ar.len()-1) {
        print!("i: {}", i);
        for j in (i+1)..ar.len() {
            println!("\tj: {}", j);
            pairs.push((ar[i],ar[j]))
        }
    };
    println!("{:?}", pairs);
    pairs.iter().map(|(n,k)| n+k).filter(|s| s%k==0).count() as i32
}


#[cfg(test)]
mod tests {
    use crate::divisibleSumPairs;

    #[test]
    fn assert_output_2() {
        let result = divisibleSumPairs(2, 2, &vec![8, 10]);
        assert_eq!(result, 1);
    }

    #[test]
    fn assert_output() {
        let result = divisibleSumPairs(6, 3, &vec![1,3,2,6,1,2]);
        assert_eq!(result, 5);
    }

}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let first_multiple_input: Vec<String> = stdin_iterator.next().unwrap().unwrap()
        .split(' ')
        .map(|s| s.to_string())
        .collect();

    let n = first_multiple_input[0].trim().parse::<i32>().unwrap();

    let k = first_multiple_input[1].trim().parse::<i32>().unwrap();

    let ar: Vec<i32> = stdin_iterator.next().unwrap().unwrap()
        .trim_end()
        .split(' ')
        .map(|s| s.to_string().parse::<i32>().unwrap())
        .collect();

    let result = divisibleSumPairs(n, k, &ar);

    writeln!(&mut fptr, "{}", result).ok();
}
