// use std::collections::HashSet;
// extern crate git2;
// use git2::Repository;
// use git2::Sort;
use std::ffi::CStr;
use std::os::raw::c_char;
use std::os::raw::c_int;
use std::str;

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


pub extern "C" fn net_score(bus:i32, correct:i32, responsive:i32, ramp:i32, license:i32)->i32{
    let result:i32 = (((10 * bus)+(30*responsive)+(30*correct) + (30*ramp))*license) / 100;
    return result
}

#[no_mangle]
pub extern "C" fn license_score(license: *const c_char) -> i32{

// Using Unsafe to dereference the pointer and converting it to bytes
let c_ptr_to_bytes = unsafe { CStr::from_ptr(license).to_bytes() };

// Converting from bytes to a string
let license = str::from_utf8(c_ptr_to_bytes);

// Unwrap, in case license is empty or null
// Return 1 if GNU v2.1 License found
    if license.unwrap().contains("v2.1") {
        return 1;
    }
    else{
        return 0;
    }
}

// Returns 0 and should return score

#[no_mangle]
pub extern "C" fn get_rm_score(rm_score: c_int) -> c_int{
    let correctness_rm_score = 3;
    let score = rm_score * correctness_rm_score;
    return score;
}







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