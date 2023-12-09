use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'countingValleys' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER steps
 *  2. STRING path
 */

struct ValleyTracker {
    current_elevation: i32,
    valley_count: i32,
}

fn countingValleys(steps: i32, path: &str) -> i32 {
    let valley_track: ValleyTracker = ValleyTracker {
        current_elevation: 0,
        valley_count: 0,
    };
    path.to_string()
        .chars()
        .map(|c| match c {
            'U' => 1,
            'D' => -1,
            _ => 0,
        })
        .fold(valley_track, |vt: ValleyTracker, step: i32| -> ValleyTracker {
            match vt.current_elevation == -1 && step == 1 {
                true => {
                    ValleyTracker {
                        current_elevation: vt.current_elevation + step,
                        valley_count: vt.valley_count + 1,
                    }
                }
                false => {
                            ValleyTracker {
                                current_elevation: vt.current_elevation + step,
                                valley_count: vt.valley_count,
                            }
                        }
            }
        })
        .valley_count
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let steps = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim()
        .parse::<i32>()
        .unwrap();

    let path = stdin_iterator.next().unwrap().unwrap();

    let result = countingValleys(steps, &path);

    writeln!(&mut fptr, "{}", result).ok();
}
