#[no_mangle]
pub extern "C" fn get_string() -> *const u8  {
    "This works?".as_ptr() 
}

#[no_mangle]
pub extern "C" fn get_score() -> *const u8  {
    "This works?".as_ptr() 
}