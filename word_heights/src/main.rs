use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'designerPdfViewer' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY h
 *  2. STRING word
 */

fn designerPdfViewer(h: &[i32], word: &str) -> i32 {
    let ascii_a_index = 'a' as u8;
    let map: Vec<i32> = word.to_string().chars().into_iter().map(|c| {
        let ascii_char_index = c as u8;
        let zeroed_char_index = (ascii_char_index - ascii_a_index) as usize;
        h[zeroed_char_index]
    }).collect();
    map.iter().max().unwrap() * (word.len() as i32)
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let h: Vec<i32> = stdin_iterator.next().unwrap().unwrap()
        .trim_end()
        .split(' ')
        .map(|s| s.to_string().parse::<i32>().unwrap())
        .collect();

    let word = stdin_iterator.next().unwrap().unwrap();

    let result = designerPdfViewer(&h, &word);

    writeln!(&mut fptr, "{}", result).ok();
}
