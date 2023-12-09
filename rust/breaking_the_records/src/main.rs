use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'breakingRecords' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY scores as parameter.
 */

#[derive(Debug)]
struct Record {
    initial: bool, 
    min: i32,
    max: i32,
    min_breaks: i32,
    max_breaks: i32,
}

fn breakingRecords(scores: &[i32]) -> Vec<i32> {
    let init: Record = Record{initial: true, min: 0, max: 0, min_breaks:0, max_breaks: 0};
    let result: Record = scores.iter().fold(init, |record_book, &score| {
        Record { 
            initial: false,
            min: if score < record_book.min || record_book.initial { score } else {record_book.min},
            max: if score > record_book.max || record_book.initial { score } else {record_book.max}, 
            min_breaks: if score < record_book.min && !record_book.initial { record_book.min_breaks + 1 } else {record_book.min_breaks},
            max_breaks: if score > record_book.max && !record_book.initial { record_book.max_breaks + 1 } else {record_book.max_breaks}
        }
    });
    vec![result.max_breaks, result.min_breaks]
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let n = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    let scores: Vec<i32> = stdin_iterator.next().unwrap().unwrap()
        .trim_end()
        .split(' ')
        .map(|s| s.to_string().parse::<i32>().unwrap())
        .collect();

    let result = breakingRecords(&scores);

    for i in 0..result.len() {
        write!(&mut fptr, "{}", result[i]).ok();

        if i != result.len() - 1 {
            write!(&mut fptr, " ").ok();
        }
    }

    writeln!(&mut fptr).ok();
}
