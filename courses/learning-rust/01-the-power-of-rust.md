# Section 1: The Power of Rust

## Hello, Rust

1. Immutable by default

Declare variables using: `let x = 10;`

To *enable* mutability, use: `var mut x = 10;`

2. Uninitialized variables are forbidden


Functions in Rust look like this:

```rust
fn main() {
    println!("Hello, world!");
}
```


```rust

fn main() {

    let a = 1;
    let b = 2;
    println!("{} + {} = {}", a, b, a+b);
}
```

`println!` is a *macro*, what that means is that the compiler does some predetermination ahead of time
for the types that are passed to it each time.

3. Rust has *a strong, static type system*.

Strongly typed means that types are not automatically cast from one to another.

Static means that the types are known at compile time.

