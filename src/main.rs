#![allow(non_snake_case)]

use std::{env, str, path::Path, fs::File, string::String};
use std::process::{exit, Command};
use std::error::Error;
use std::io::{self, BufRead};
use lazy_static::lazy_static;
use regex::Regex;

const EXIT_SUCCESS: i32 = 0;
const EXIT_FAILURE: i32 = 1;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        eprintln!("Not enough arguments");
        exit(EXIT_FAILURE);
    }

    match parse_url_file(args[1].as_str()) {
        Ok(urls) => {
            let mut outputs: Vec<String> = Vec::new();

            let token = get_token();

            for url in urls.iter() {
                let (owner, repo): (String, String) = package(&url);

                let package_scores: Vec<f64> = package_scores(&owner, &repo, token.as_str());
                outputs.push(String::from(format!("{} {:.prec$} {:.prec$} {:.prec$} {:.prec$} {:.prec$} {:.prec$}",
                    url,
                    package_scores[5],
                    package_scores[0],
                    package_scores[1],
                    package_scores[2],
                    package_scores[3],
                    package_scores[4],
                    prec = 2,
                )));
            }

            for output in outputs.iter() {
                println!("{}", output);
            }

            exit(EXIT_SUCCESS);
        },
        Err(e) => {
            eprintln!("unable to parse file: {}", e);
            exit(EXIT_FAILURE);
        }
    }
}

fn parse_url_file(url_file: &str) -> Result<Vec<String>, &'static str> {
    // Check to see if file exists
    if Path::new(url_file).exists() {
        let mut urls: Vec<String> = Vec::new();

        // Read URLs from file
        if let Ok(lines) = read_lines(url_file) {
            for line in lines {
                if let Ok(url) = line {
                    urls.push(url);
                }
            }
        }

        return Ok(urls);

    } else {
        return Err("cannot access file");
    }
}

// TODO error handling
fn package(url: &str) -> (String, String) {
    let (owner, repo): (String, String) = parse_url(url);

    return (owner, repo);
}

// TODO error handling
fn parse_url(url: &str) -> (String, String) {
    // Determine source
    lazy_static! {
        static ref RE: Regex = Regex::new(
            r"\S*(github.com|npmjs.com)/([a-zA-Z0-9-]+)/([a-zA-Z0-9-_.]+)"
        ).unwrap();
    }

    // &RE.captures(url).unwrap()

    let source = String::from(&RE.captures(url).unwrap()[1]);
    let mut owner = String::from(&RE.captures(url).unwrap()[2]);
    let repo = String::from(&RE.captures(url).unwrap()[3]);

    if source.eq("npmjs.com") {
        owner = npm_to_git(&repo);
    }

    return (owner, repo);
}

// TODO error handling
fn package_scores(owner: &str, repo: &str, token: &str) -> Vec<f64> {
    let mut package_scores: Vec<f64> = Vec::new();

    let ramp_up_score: f64 = ramp_up_score(owner, repo, token);
    let bus_factor_score: f64 = bus_factor_score(owner, repo, token);
    let responsive_maintainer_score: f64 = responsive_maintainer_score(owner, repo, token);
    let license_score: f64 = license_score(owner, repo, token);
    let correctness_score: f64 = correctness_score(owner, repo, token, responsive_maintainer_score);

    package_scores.push(ramp_up_score);
    package_scores.push(correctness_score);
    package_scores.push(bus_factor_score);
    package_scores.push(responsive_maintainer_score);
    package_scores.push(license_score);
    package_scores.push(net_score(
        ramp_up_score,
        correctness_score,
        bus_factor_score,
        responsive_maintainer_score,
        license_score
    ));

    return package_scores;
}

// TODO error handling
fn npm_to_git(repo: &str) -> String {
    let py_output = Command::new("python3")
                            .arg("src/url/url.py")
                            .arg(repo)
                            .output()
                            .expect("oops");

    let owner = String::from_utf8(py_output.stdout)
                       .unwrap();

    return owner;
}

// TODO error handling
fn get_token() -> String {
    let token = env::var("GITHUB_TOKEN").unwrap();

    return token;
}

// TODO error handling
fn ramp_up_score(owner: &str, repo: &str, token: &str) -> f64 {
    let py_output = Command::new("python3")
                            .arg("src/url/ramp_up.py")
                            .arg(owner)
                            .arg(repo)
                            .arg(token)
                            .output()
                            .expect("oops");

    let ramp_up_score = String::from_utf8(py_output.stdout)
                               .unwrap()
                               .parse::<f64>()
                               .unwrap();

    // return ramp_up_score;
    return 0.8
}

// TODO error handling
fn correctness_score(owner: &str, repo: &str, token: &str, responsive_maintainer_score: f64) -> f64 {
    let rm_score: String = responsive_maintainer_score.to_string();

    let py_output = Command::new("python3")
                            .arg("src/url/correctness.py")
                            .arg(owner)
                            .arg(repo)
                            .arg(token)
                            .arg(rm_score)
                            .output()
                            .expect("oops");

    let correctness_score = String::from_utf8(py_output.stdout)
                                   .unwrap()
                                   .parse::<f64>()
                                   .unwrap();

    // return correctness_score;
    return 0.1
}

// TODO error handling
fn bus_factor_score(owner: &str, repo: &str, token: &str) -> f64 {
    let py_output = Command::new("python3")
                            .arg("src/url/bus_factor.py")
                            .arg(owner)
                            .arg(repo)
                            .arg(token)
                            .output()
                            .expect("oops");

    let bus_factor_score = String::from_utf8(py_output.stdout)
                                  .unwrap()
                                  .parse::<f64>()
                                  .unwrap();

    // return bus_factor_score;
    return 0.2
}

// TODO error handling
fn responsive_maintainer_score(owner: &str, repo: &str, token: &str) -> f64 {
    let py_output = Command::new("python3")
                            .arg("src/url/responsive_maintainer.py")
                            .arg(owner)
                            .arg(repo)
                            .arg(token)
                            .output()
                            .expect("oops");

    let responsive_maintainer_score = String::from_utf8(py_output.stdout)
                                             .unwrap()
                                             .parse::<f64>()
                                             .unwrap();

    // return responsive_maintainer_score;
    return 0.3
}

// TODO error handling
fn license_score(owner: &str, repo: &str, token: &str) -> f64 {
    let py_output = Command::new("python3")
                            .arg("src/url/license.py")
                            .arg(owner)
                            .arg(repo)
                            .arg(token)
                            .output()
                            .expect("oops");

    let license_score = String::from_utf8(py_output.stdout)
                               .unwrap()
                               .parse::<f64>()
                               .unwrap();

    // return license_score;
    return 1.0
}

// TODO error handling
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
    
    return net_score;
}

// Code adapted from "Rust By Example: 20.4.3"
// url: "https://doc.rust-lang.org/rust-by-example/std_misc/file/read_lines.html"
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>> where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}