use std::env;
use std::process::exit;
use std::path::Path;

const EXIT_SUCCESS: i32 = 0;
const EXIT_FAILURE: i32 = 1;

fn main() {
    let args: Vec<String> = env::args().collect();

    if Path::new(args[1].as_str()).exists() {
        run::print_scores(args[1].as_str());
        exit(EXIT_SUCCESS);
    } else {
        println!("ERROR: File does not exist");
        exit(EXIT_FAILURE);
    }
}