fn main() {

    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (x, y, z) = tup;

    println!("{} {} {}", x, y, z);
    let f = tup.0;
    let g = tup.1;
    let h = tup.2;

    println!("{} {} {}", f, g, h);
}
