use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};

/*
 * Complete the 'dayOfProgrammer' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts INTEGER year as parameter.
 */

struct ProgDayMonthYear {
    day: i32,
    month: i32, 
    year: i32
}
use std::fmt;

impl ProgDayMonthYear{
    fn new(year: i32) -> ProgDayMonthYear {
        let mut days_per_month: Vec<i32> = vec![31,28,31,30,31,30,31,31,30,31,30,31];
        let is_julian_leap_year = |year: i32| -> bool {
            year % 4 == 0
        };
        let is_gregorian_leap_year = |year: i32| -> bool {
            year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)
        };
        let mut nth_day: i32 = 256;
        if year == 1918 {
            nth_day += 13;
        }
        if (year < 1918 && is_julian_leap_year(year)) || (year >= 1918 && is_gregorian_leap_year(year)) {
            days_per_month[1] = 29;
        }
        
        let mut day: i32 = 0;
        let mut month: i32 = 0;
        days_per_month.iter().for_each(|&days_in_month| {
            if nth_day > 0 {
                day = nth_day;
                month += 1;
            }
            nth_day -= days_in_month;
        }
        );
        ProgDayMonthYear{ day, month, year }
    }
}

impl fmt::Display for ProgDayMonthYear {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:02}.{:02}.{:04}", self.day, self.month, self.year)
    }
}

fn dayOfProgrammer(year: i32) -> String {
    ProgDayMonthYear::new(year).to_string()
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let year = stdin_iterator.next().unwrap().unwrap().trim().parse::<i32>().unwrap();

    let result = dayOfProgrammer(year);

    writeln!(&mut fptr, "{}", result).ok();
}

#[cfg(test)]
mod tests {
    use crate::dayOfProgrammer;

    #[test]
    fn assert_output() {
        let result = dayOfProgrammer(2000);
        assert_eq!(result, "12.09.2000");
    }
    #[test]
    fn assert_output_1() {
        let result = dayOfProgrammer(2010);
        assert_eq!(result, "13.09.2010");
    }
    #[test]
    fn assert_output_2() {
        let result = dayOfProgrammer(1917);
        assert_eq!(result, "13.09.1917");
    }
    #[test]
    fn assert_output_3() {
        let result = dayOfProgrammer(1918);
        assert_eq!(result, "26.09.1918");
    }
    #[test]
    fn assert_output_4() {
        let result = dayOfProgrammer(1919);
        assert_eq!(result, "13.09.1919");
    }
    #[test]
    fn assert_output_5() {
        let result = dayOfProgrammer(1800);
        assert_eq!(result, "12.09.1800");
    }
}