use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        println!("ERROR: incorrect usage");
        println!("USAGE:");
        println!("\t./run build");
        println!("\t./run install");
        println!("\t./run test");
        println!("\t./run <URL_FILE>");
        return;
    }

    match args[1].as_str() {
        "build" => run::build(),
        "install" => run::install(),
        "test" => run::test(),
        _ => run::parse_url_file(args[1].as_str()),
    }
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


pub extern "C" fn net_score(bus:i32, correct:i32, responsive:i32, ramp:i32, license:i32)->i32{
    let result:i32 = (((10 * bus)+(30*responsive)+(30*correct) + (30*ramp))*license) / 100;
    return result
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