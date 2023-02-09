use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use cpython::{Python, PyResult};

// #[macro_use]
// extern crate cpython;


// py_module_initializer!(mylib, |py, m| {
//     // m.add(py, "__doc__", "This module is implemented in Rust.")?;
//     m.add(py, "get_result", py_fn!(py, get_result(val: &str)))?;
//     Ok(())
// });

// fn get_result(_py: Python, val: &str) -> PyResult<String> {
//     Ok("Rust says: ".to_owned() + val)
// }


pub fn print_scores(url_file: &str) {
    let urls: Vec<String> = parse_url_file(url_file);

    let ramp_up_score: f64 = ramp_up_score(url_file);
    let correctness_score: f64 = correctness_score(url_file);
    let bus_factor_score: f64 = bus_factor_score(url_file);
    let responsive_maintainer_score: f64 = responsive_maintainer_score(url_file);
    let license_score: f64 = license_score(url_file);

    let net_score: f64 = net_score(
        ramp_up_score,
        correctness_score,
        bus_factor_score,
        responsive_maintainer_score,
        license_score
    );

    for url in urls {
        println!("{} {:.prec$} {:.prec$} {:.prec$} {:.prec$} {:.prec$} {:.prec$}",
            url,
            net_score,
            ramp_up_score,
            correctness_score,
            bus_factor_score,
            responsive_maintainer_score,
            license_score,
            prec = 1,
        );
    }
}

fn parse_url_file(url_file: &str) -> Vec<String> {
    let mut urls = Vec::new();

    // Read URLs from file
    if let Ok(lines) = read_lines(url_file) {
        for line in lines {
            if let Ok(url) = line {
                urls.push(url);
            }
        }
    }

    return urls;
}

// Code adapted from "PyO3 user guide: 7."
// url: "https://pyo3.rs/v0.18.0/python_from_rust.html"
fn ramp_up_score(url_file: &str) -> f64 {
    let py_

    return 0.0
}

fn correctness_score(url_file: &str) -> f64 {

    return 0.0
}

fn bus_factor_score(url_file: &str) -> f64 {

    return 0.0
}

fn responsive_maintainer_score(url_file: &str) -> f64 {
    let p

    return 0.0
}

fn license_score(url_file: &str) -> f64 {

    return 1.0
}

fn net_score(ramp_up_score: f64,
             correctness_score: f64,
             bus_factor_score: f64,
             responsive_maintainer_score: f64,
             license_score: f64)
            -> f64 {

    let net_score: f64 = 
        license_score * (
            0.3 * ramp_up_score +
            0.3 * correctness_score +
            0.1 * bus_factor_score +
            0.3 * responsive_maintainer_score
        );
    
    return net_score
}

// Code adapted from "Rust By Example: 20.4.3"
// url: "https://doc.rust-lang.org/rust-by-example/std_misc/file/read_lines.html"
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>> where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

#[no_mangle]
pub extern "C" fn bus_score(val: i32)-> i32{
    // let URL: &str = "https://github.com/Chise7/ECE461_Team11";
    // let repo = Repository::open(URL).expect("Couldn't create file");

    // let mut revwalk = repo.revwalk().expect("None");
    // revwalk.push_head();
    // let mut authors: Vec<String> = revwalk.map(|r| {
    //     let oid = r;
    //     repo.find_commit(oid)
    // })

    let mut result:i32 = 0; 
    if val >= 5 && val < 100{
        result = 75;
    } 
    if val >= 100 {
        result = 100;
    };
    return result
}