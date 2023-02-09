use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

// TODO
pub fn build() {

}

// TODO
pub fn install() {

}

// TODO
pub fn test() {

}

pub fn parse_url_file(url_file: &str) {
    // TODO Check if file exists

    // Read URLs from file
    if let Ok(lines) = read_lines(url_file) {
        for line in lines {
            if let Ok(url) = line {
                println!("{}", url);
            }
        }
    }
}

// From "Rust By Example: 20.4.3"
// url: "https://doc.rust-lang.org/rust-by-example/std_misc/file/read_lines.html"
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>> where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}