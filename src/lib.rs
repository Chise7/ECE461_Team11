#![allow(non_snake_case)]

use std::ffi::CStr;
use std::os::raw::c_char;
use std::os::raw::c_int;
use std::str;


#[no_mangle]
fn net_score(mut ramp_up_score: f64,
             mut correctness_score: f64,
             mut bus_factor_score: f64,
             mut responsive_maintainer_score: f64,
             mut license_score: f64)
            -> f64 {
    //These lines deal with errors
    //if the scores return negative this will calculate the score with that subscore as 0
    if ramp_up_score < 0.0{
        ramp_up_score = 0.0
    }
    if correctness_score < 0.0{
        correctness_score = 0.0;
    }
    if bus_factor_score < 0.0{
        bus_factor_score = 0.0;
    }
    if responsive_maintainer_score < 0.0{
        responsive_maintainer_score = 0.0;
    }
    if license_score < 0.0{
        license_score = 0.0;
    }
    let net_score: f64 = 
        license_score * (
            0.3 * ramp_up_score +
            0.3 * correctness_score +
            0.1 * bus_factor_score +
            0.3 * responsive_maintainer_score
        );
    
    return net_score
}

 #[no_mangle]
 pub extern "C" fn get_rm_score(rm_score: c_int) -> c_int{
    let correctness_rm_score = 3;
    let score = rm_score * correctness_rm_score;
    return score;
 }

#[no_mangle]
pub extern "C" fn bus_score(val: i32)-> i32{
//     // let URL: &str = "https://github.com/Chise7/ECE461_Team11";
//     // let repo = Repository::open(URL).expect("Couldn't create file");

//     // let mut revwalk = repo.revwalk().expect("None");
//     // revwalk.push_head();
//     // let mut authors: Vec<String> = revwalk.map(|r| {
//     //     let oid = r;
//     //     repo.find_commit(oid)
//     // })

    let mut result:i32 = 0; 
    if val >= 5 && val < 100{
        result = 75;
    } 
    if val >= 100 {
        result = 100;
    };
    return result
}
