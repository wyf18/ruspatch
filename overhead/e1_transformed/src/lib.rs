use lazy_static::lazy_static;
lazy_static! {
    pub static ref LIB: std::sync::RwLock<Option<libloading::Library>> =
        unsafe { std::sync::RwLock::new(Some(libloading::Library::new("./libe1.so").unwrap())) };
}
