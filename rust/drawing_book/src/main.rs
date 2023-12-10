use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'pageCount' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER p
 */

fn pageCount(n: i32, p: i32) -> i32 {
    let start_page_rank = 0;
    let end_page_rank = n /2;
    let current_page_rank = p / 2;

    let dist_front = current_page_rank - start_page_rank;
    let dist_back = end_page_rank - current_page_rank;
    dist_front.min(dist_back)
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let n = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    let p = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    let result = pageCount(n, p);

    writeln!(&mut fptr, "{}", result).ok();
}

#[cfg(test)]
mod tests{
    use crate::pageCount;
    #[test]
    fn assert_output_0(){
        assert_eq!(pageCount(5,2), 1);
    }    
    #[test]
    fn assert_output_1(){
        assert_eq!(pageCount(5,3), 1);
    }
    #[test]
    fn assert_output_2(){
        assert_eq!(pageCount(7,3), 1);
    }
    #[test]
    fn assert_output_3(){
        assert_eq!(pageCount(9,3), 1);
    }
    #[test]
    fn assert_output_4(){
        assert_eq!(pageCount(5,5), 0);
    }
    // #[test]
    // #[should_panic]
    // fn assert_output_5(){
    //     assert_eq!(pageCount(0,5), 0);
    // }
    #[test]
    fn assert_output_6(){
        assert_eq!(pageCount(5,0), 0);
    }
    #[test]
    fn assert_output_7(){
        assert_eq!(pageCount(6,5), 1);
    }
}
