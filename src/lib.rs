use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use lazy_static::lazy_static;
use regex::Regex;


pub mod responsive_maintainer;


pub fn print_scores(url_file: &str) {
    let urls: Vec<String, String> = parse_url_file(url_file);

    let ramp_up_score: f64 = ramp_up_score(url_file);
    let correctness_score: f64 = correctness_score(url_file);
    let bus_factor_score: f64 = bus_factor_score(url_file);
    let responsive_maintainer_score: f64 = responsive_maintainer::score(url_file);
    //let license_score: f64 = license_score(url_file);

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
    let mut urls: Vec<(String, String)> = Vec::new();

    // Read URLs from file
    if let Ok(lines) = read_lines(url_file) {
        for line in lines {
            if let Ok(url) = line {
                urls.push(parse_url(url));
            }
        }
    }

    return urls;
}

fn parse_url(url: &str) -> (String, String) {
    // Determine source
    lazy_static! {
        static ref RE: Regex = Regex::new(
            r"\S*(github.com|npmjs.com)/([a-zA-Z0-9-]+)/([a-zA-Z0-9-_.]+)"
        ).unwrap();
    }

    RE.captures(url)[0]
}

// Code adapted from "PyO3 user guide: 7."
// url: "https://pyo3.rs/v0.18.0/python_from_rust.html"
fn ramp_up_score(url_file: &str) -> f64 {

    return 0.0
}

fn correctness_score(url_file: &str) -> f64 {

    return 0.0
}

fn bus_factor_score(url_file: &str) -> f64 {

    return 0.0
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

// #[no_mangle]
// pub extern "C" fn bus_score(val: i32)-> i32{
//     // let URL: &str = "https://github.com/Chise7/ECE461_Team11";
//     // let repo = Repository::open(URL).expect("Couldn't create file");

//     // let mut revwalk = repo.revwalk().expect("None");
//     // revwalk.push_head();
//     // let mut authors: Vec<String> = revwalk.map(|r| {
//     //     let oid = r;
//     //     repo.find_commit(oid)
//     // })

//     let mut result:i32 = 0; 
//     if val >= 5 && val < 100{
//         result = 75;
//     } 
//     if val >= 100 {
//         result = 100;
//     };
//     return result
// }

// use std::collections::HashSet;
// extern crate git2;
// use git2::Repository;
// use git2::Sort;

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

use std::ffi::CStr;
use std::os::raw::c_char;
use std::os::raw::c_int;
use std::str;

pub extern "C" fn net_score(bus:i32, correct:i32, responsive:i32, ramp:i32, license:i32)->i32{
    let result:i32 = (((10 * bus)+(30*responsive)+(30*correct) + (30*ramp))*license) / 100;
    return result
}

#[no_mangle]
pub extern "C" fn license_score(license: *const c_char, license_list: *const c_char) -> i32{

// Using Unsafe to dereference the pointer and converting it to bytes
let c_ptr_to_bytes = unsafe { CStr::from_ptr(license).to_bytes() };

// Using Unsafe to dereference the pointer and converting it to bytes
let c_ptr_to_bytes2 = unsafe { CStr::from_ptr(license_list).to_bytes() };

// Converting from bytes to a string
let license = str::from_utf8(c_ptr_to_bytes).unwrap();

// Converting from bytes to a string
let license_list = str::from_utf8(c_ptr_to_bytes2).unwrap();

// Unwrap, in case license is empty or null
// Return 1 if GNU v2.1 License found
    if license_list.contains(license) {
        return 1;
    }
    else{
        return 0;
    }
}

// Returns 0 and should return score
// use std::ffi::CStr;
// use std::os::raw::c_char;
// use std::os::raw::c_int;
// use std::str;

// #[no_mangle]
// pub extern "C" fn bus_score(val: i32)-> i32{
//     // let URL: &str = "https://github.com/Chise7/ECE461_Team11";
//     // let repo = Repository::open(URL).expect("Couldn't create file");

//     // let mut revwalk = repo.revwalk().expect("None");
//     // revwalk.push_head();
//     // let mut authors: Vec<String> = revwalk.map(|r| {
//     //     let oid = r;
//     //     repo.find_commit(oid)
//     // })

//     let mut result:i32 = 0; 
//     if val >= 5 && val < 100{
//         result = 75;
//     } 
//     if val >= 100 {
//         result = 100;
//     };
//     return result
// }


// pub extern "C" fn net_score(bus:i32, correct:i32, responsive:i32, ramp:i32, license:i32)->i32{
//     let result:i32 = (((10 * bus)+(30*responsive)+(30*correct) + (30*ramp))*license) / 100;
//     return result
// }

// #[no_mangle]
// pub extern "C" fn license_score(license: *const c_char) -> i32{

// // Using Unsafe to dereference the pointer and converting it to bytes
// let c_ptr_to_bytes = unsafe { CStr::from_ptr(license).to_bytes() };

// // Converting from bytes to a string
// let license = str::from_utf8(c_ptr_to_bytes);

// // Unwrap, in case license is empty or null
// // Return 1 if GNU v2.1 License found
//     if license.unwrap().contains("v2.1") {
//         return 1;
//     }
//     else{
//         return 0;
//     }
// }

// // Returns 0 and should return score

// #[no_mangle]
// pub extern "C" fn get_rm_score(rm_score: c_int) -> c_int{
//     let correctness_rm_score = 3;
//     let score = rm_score * correctness_rm_score;
//     return score;
// }

// #[macro_use]
// extern crate cpython;

// use cpython::{PyResult,Python};

// py_module_initializer!(mylib, |py, m| {
//     // m.add(py, "__doc__", "This module is implemented in Rust.")?;
//     m.add(py, "get_result", py_fn!(py, get_result(val: &str)))?;
//     Ok(())
// });

// fn get_result(_py: Python, val: &str) -> PyResult<String> {
//     Ok("Rust says: ".to_owned() + val)
// }