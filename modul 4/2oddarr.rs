use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let data: Vec<i32> = input.trim().split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect();
    for i in 0..data.len() {
        if data[i] % 2 != 0 {
            print!("{} ", data[i]);
        }
        else {
            print!("0 ");
        }
    }

}
