// The println macro
pub fn run() {
  let life = 42;
  println!("hello");
  println!("{:?}", life);
  println!("{:?} {:?}", life, life);
  println!("the meaning is {:?}", life);
  println!("{life:?}"); //For debugging
  println!("{life}"); //For end user
}