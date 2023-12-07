use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'migratoryBirds' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

fn migratoryBirds(arr: &[i32]) -> i32 {
    use std::collections::hash_map::*;
    use std::collections::hash_map::Entry::*;
    let mut occurrences: HashMap<i32,i32> = HashMap::new();
    arr.iter().for_each(|&bird| {
        match occurrences.entry(bird) {
            Occupied(e) => {*e.into_mut()+=1},
            Vacant(e) => {e.insert(1);},
        }
    });
    *occurrences.iter().max_by(|x,y| {
        match x.1.cmp(y.1) {
            std::cmp::Ordering::Less => std::cmp::Ordering::Less,
            std::cmp::Ordering::Equal => y.0.cmp(x.0),
            std::cmp::Ordering::Greater => std::cmp::Ordering::Greater,
        }
    }).unwrap().0
}

#[cfg(test)]
mod tests{
    use crate::migratoryBirds;
    #[test]
    fn assert_output_1(){
        let input: Vec<i32> = vec![1,4,4,4,5,3];
        assert_eq!(migratoryBirds(&input), 4);
    }
    #[test]
    fn assert_output_2(){
        let input: Vec<i32> = vec![1,4,4,4,5,5,5,3];
        assert_eq!(migratoryBirds(&input), 4);
    }
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let _arr_count = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    let arr: Vec<i32> = stdin_iterator.next().unwrap().unwrap()
        .trim_end()
        .split(' ')
        .map(|s| s.to_string().parse::<i32>().unwrap())
        .collect();

    let result = migratoryBirds(&arr);

    writeln!(&mut fptr, "{}", result).ok();
}
