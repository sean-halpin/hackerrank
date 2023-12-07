[Sock Merchant](https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true)

## Run Local

```
OUTPUT_PATH="$(pwd)/out.txt" cargo run
```

## Input

```
9
10 20 20 10 10 30 50 10 20
```

## Output

```
3
```

# ChatGPT's concise and readable version of my solution
```
use std::collections::HashMap;

fn sock_merchant(n: i32, ar: &[i32]) -> i32 {
    let mut sock_map = HashMap::new();

    for &sock_type in ar {
        *sock_map.entry(sock_type).or_insert(0) += 1;
    }

    let pair_count: i32 = sock_map.values().map(|&sock_count| sock_count / 2).sum();
    pair_count
}
```