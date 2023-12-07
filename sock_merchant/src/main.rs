use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'sockMerchant' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY ar
 */

fn sockMerchant(n: i32, ar: &[i32]) -> i32 {
    use std::collections::hash_map::*;
    let mut sock_map: HashMap<i32, i32> = HashMap::new();
    ar.iter().for_each(|&sock_type| {
        match sock_map.entry(sock_type) {
            Entry::Occupied(entry) => {
                *entry.into_mut() += 1;
            }
            Entry::Vacant(vacant_entry) => {
                vacant_entry.insert(1);
            }
        };
    });
    let pair_count: i32 = sock_map
        .values()
        .map(|&sock_count| 
            if sock_count == 0 {0} else {(sock_count - (sock_count % 2))/2}).sum();
    pair_count
}

#[cfg(test)]
mod tests {
    use crate::sockMerchant;

    #[test]
    fn assert_output() {
        let input = vec![10, 20, 20, 10, 10, 30, 50, 10, 20];
        let result = sockMerchant(9, &input);
        assert_eq!(result, 3);
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

    let ar: Vec<i32> = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim_end()
        .split(' ')
        .map(|s| s.to_string().parse::<i32>().unwrap())
        .collect();

    let result = sockMerchant(n, &ar);

    writeln!(&mut fptr, "{}", result).ok();
}
