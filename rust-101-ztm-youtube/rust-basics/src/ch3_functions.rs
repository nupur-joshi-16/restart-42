// Functions in Rust
pub fn run() {

  // Anatomy of function
  fn add (a:i32, b:i32) -> i32 {
    a + b
  }

  // fn is a keyword
  // add is a function name.
  // (a:i32, b:i32) are parameters
  // a and b are variable names
  // i32 is 32 bit integer
  // -> i32 is a return type
  // {} function body
  
  // using function
  let x = add(1, 1);
    println!("1 + 1 = {}", x);
  let y = add(20, 10);
    println!("{}", y);
  let z = add(x, 100);
    println!("{}", z);
}