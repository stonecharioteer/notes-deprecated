# Rust Documentation

This folder contains my notes on the Rust Documentation as I work through them.

I found [A Half Hour to Learn Rust](https://fasterthanli.me/articles/a-half-hour-to-learn-rust) very useful before starting this book.

## A Half Hour to Learn Rust

`let` introduces a variable binding:

```rust
let x; // declare 'x'
x = 42; // assign 42 to `x`
```

This can also be written as a single line:

```rust
let x = 42;
```

You can specify the variable's type explicitly with `:`, that's a type annotation.

```rust
let x: i32; // 'i32' is a signed 32-bit integer.
x = 42;

// there's i8, i16, i32, i64, i128
//      also u8, u16, u32, u64, u128 for unsigned
```

This can also be written in a single line:

```rust
let x: i32 = 42;
```

If you declare a name and initialize it later, the compier will prevent you from using it before it's finalized.

```rust
let x;
foobar(x); // error: borrow of possibly-uninitializzed variable: `x`
x = 42;
```

However, doing this is completely fine:

```rust
let x;
x = 42;
foobar(x); // the type of `x` will be inferred from here.
```

The underscore `_` is a special name - or rather, a "lack of name". It basically means to throw away something:

```rust
// this does *nothing* because 42 is a constant
let _ = 42;

// this calls `get_thing` but throws away the result.
let _ = get_thing();
```

Names that *start* with an underscore are regular names, it's just that the compiler won't warn about them being unused.

```rust
// we may use `_x` eventually, but out code is a work-in-progress
// and we just wanted to get rid of a compiler warning for now.
let _x = 42;
```

Separate bindings with the same name can be introduced - you can *shadow* a variable binding:

```rust
let x = 13;
let x = x + 3;
// using `x` after that line only refers to the second `x`
// the first `x` no longer exists.
```

Rust has tuples, which you can think of as "fixed-length collections of values of different types".

```rust
let pair = ('a', 17);
pair.0; // this is 'a'
pair.1; // this is 17
```

If we really wanted to annotate the type of `pair`, we would write:

```rust
let pair: (char, i32) = ('a', 17);
```

Tuples can be *destructured* when doing an assignment, which means they're broken down into their individual fields:

```rust
let (some_char, some_int) = ('a', 17);
// now `some_char` is 'a' and `some_int` is 17
```

This is especially useful when a function returns a tuple:

```rust
let (left, right) = slice.split_at(middle);
```

Of course, when destructuring a tuple, `_` can be used to throw away part of it:

```rust
let (_, right) = slice.split_at(middle);
```

The semi-colon `;` marks the end of the statement:

```rust
let x;
let y: i8 = 2;
let (_, right) = some_function(y);
```

Which means statements can span multiple lines:

```rust
let x = vec![1, 2, 3, 4, 5, 6, 7, 8, 9]
    .iter()
    .map(|x| x + 3)
    .fold(0, |x, y| x + y);
```

(We'll go over what those actually mean later).

`fn` declares a function;

Here's a void function:

```rust
fn greet() {
    println!("Hi there!");
}
```

And here's a function that returns a 32-bit signed integer. The arrow indicates its return type:


```rust

fn fair_dice_roll() -> i32 {
    4
}

```

A pair of brackets declares a block, which has its own scope:

```rust

// this prints "in", then "out"

fn main() {
    let x = "out";
    {
        // this is a different `x`
        let x = "in";
        println!(x);
    }
    println!(x);
}

```

Blocks are also expressions, which mean they evaluate to... a value.

```rust
// this
let x = 42;

// is equivalent to this
let x = { 42 };

```

Inside a block, there can be multiple statements:

```rust
let x = {
    let y = 1; // first statement
    let z = 2; // second statement
    y + z // this is the *tail* - what the whole block will evaluate to.
}
```

And that's why "omitting" the semicolon at the end of a function" is the same as *returning*, ie, these are equivalent:

```rust

fn fair_dice_roll() -> i32 {
    4
}

fn fair_dice_roll() -> i32 {
    return 4;
}
```

`if` conditionals are also expressions:

```rust
fn fair_dice_roll() -> i32 {
    if feeling_lucky {
        6
    } else {
        4
    }
}
```

A `match` is also an expression:

```rust
fn fair_dice_roll() -> i32 {
    match feeling_lucking {
        true => 6,
        false => 4,
    }
}
```

`true` and `false` are the boolean states.

Dots are typically used to access fields of a value:

```rust
let a = (10, 20);
a.0; // this is 10
let amos = get_some_struct();
amos.nickname; // this is the `nickname` attribute of a `Struct`

```

Or call a method on a value:

```rust
let nick = "fasterthanlime";
nick.len(); // this is 14
```

The double-colon, `::`, is similar but it operates on *namespaces*.

In this example, `std` is a *crate* (~ a library), `cmp` is a *module* (~ a source file), and `min` is a *function*.

```rust
let least = std::cmp::min(3,8); // this is 3
```

`use` directives can be used to "bring in scope" names from other namespaces:

```rust
use std::cmp::min;

let least = min(7, 1); // this is 1
```

Within `use` directives, curly brackets have another meaning: they're *globs*. If we want to import both `min` and `max`, we can do any of these:

```rust
// this works:

use std::cmp::min;
use std::cmp::max;

// this also works:
use std::cmp::{min, max};

// this also works!
use std::{cmp::min, cmp::max};
```

A wildcard `*` lets you import every symbol from a namespace:

```rust
// this brings in `min' and `max` in scope, and many other things.

use std::cmp::*;
```

Types are namespaces too, and methods can be called as regular functions:

```rust

// `Vec` is a regular struct, not a primitive type.

let v = Vec::new();

// this is exactly the same code, but with the *full* path to `Vec`.
let v = std::vec::Vec::new();
```
This works because Rust inserts this at the beginning of every module:

```rust
use std::prelude::v1::*;
```

(Which in turn re-exports a lot of symbols, like `Vec`, `String`, `Option` and `Result`).

Structs are declared with the `struct` keyword:

```rust
struct Vec2 {
    x: f64, // 64-bit floating point, aka "double precision"
    y: f64,
}
```

They can be initialized using *struct literals*:

```rust

let v1 = Vec2 { x: 1.0, y: 3.0 };
let v2 = Vec2 { y:2.0, x: 4.0 };
```

There is a shortcut for initializing the *rest of the fields* from another struct:

```rust
let v3 = Vec2 {
    x: 13.0,
    ..v2
};
```

This is called "struct update syntax", can only happen in the last position, and cannot be followed by a comma.

Note that *the rest of the fields* can mean *all the fields*.

```rust
let v4 = Vec2 { ..v2 };
```

Structs, like tuples, can be destructured.

Just like this is a valid `let` pattern:

```rust
let (left, right) = slice.splice_at(middle);
```

So is this:

```rust
let Vec2 {x, ..} = v;
// this throws away `v.y`.
```

`let` patterns can be used as conditions in `if`:

```rust

struct Number {
    odd: bool,
    value: i32,
}

fn main() {
    let one = Number {odd: true, value: 1};
    let two = Number { odd: false, value: 2};

    print_number(one);
    print_number(two);
}

fn print_number(n: Number) {
    if let Number { odd: true, value } = n {
        println!("Odd number: {}", value);
    } else if let Number { odd: false, value} = n {
        println!("Even number: {}", value);
    }
}

// this prints:
// Odd number: 1
// Even number: 2
```

`match` arms are also patterns, just like `if let`.
