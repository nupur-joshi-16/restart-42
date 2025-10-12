// Variables in Rust
pub fn run() {
  // Immutable by default, but can be mutable.
  // Immutable - cannot be changed
  // Mutable - can be changed

  let two = 2; // i32 (integer) — default integer type in Rust
  let hello = "hello"; // &str (string slice) — immutable reference to string
  let j = "j"; // &str (string slice)
  let my_half = 0.5; // f64 (floating-point number) — default float type in Rust
  let mut my_name = "Nupur"; // &str (string slice), mutable reference (can reassign)
  let quit_program = false; // bool (boolean)
  let your_half = my_half; // f64 (floating-point number) — same type as my_half

}