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

```rust

fn print_number(n: Number) {

    match n {
        Number {odd: true, value} => println!("Odd: {}", value),
        Number {odd: false, value} => println!("Even: {}", value),
    }
}

// this prints the same as before.
```

A `match` has to be exhaustive: at least one arm needs to match.

```rust

fn print_number(n: Number) {
    match n {
        Number(value: 1) => println!("One!"),
        Number(value: 2) => println!("Two!),
        Number(value, ..) => println!("{}", value),
        // if that las tarm didn't exist, we would get a compile-time error
    }
}

```

If that's hard, `_` can be used as a "catch-all" pattern:

```rust

fn print_number(n: Number) {
    match n {
        Number {value: 1, ..} => println!("One"),
        Number {value: 2, ..} => println!("Two"),
        _ => println!("{}", n.value), // can't use `value` directly here.

    }
}
```

You can declare methods on your own types:

```rust
struct Number {
    odd: bool,
    value: i32,
}
impl Number {
    fn is_strictly_positive(self) -> bool {
        self.value > 0
    }
}
```

And use them like usual:

```rust

fn main() {
    let minus_two = Number {
        odd: false,
        value: -2,
    }
    println!("Positive? {}", minus_two.is_strictly_positive());
    // this prints "Positive? false"
}
```

Variable bindings are immutable by default, which means their interior can't be mutated:

```rust
fn main() {
    let n = Number {
        odd: true,
        value: 17,
    };
    n.odd = false; // error: cannot assign to `n.odd`
                   // as `n` is not declared to be mutable
}

```

And also that they cannot be assigned to:

```rust
fn main() {
    let n = Number {
        odd: true,
        value: 17,
    };
    n = Number {
        odd: false,
        value: 2
    }; // error: cannot assign twice to immutable variable `n`
}

```

`mut` makes a variable binding mutable:

```rust
fn main() {
    let mut n = Number {
        odd: true,
        value: 5,
    }
    n.value = 19; // all good
}
```

Traits are something multiple types can have in common:

```rust
trait Signed {
    fn is_strictly_negative(self) -> bool;
}
```

You can implement:
    * one of your traits on anyone's type
    * anyone's trait on one of your types
    * but not a foreign trait on a foreign type.

These are called the "orphan rules".

Here's an implementation of our trait on our type:

```rust

impl Signed for Number {
    fn is_strictly_negative(self) -> bool {
        self.value < 0
    }
}

fn main() {
    let n = Number {odd: true, value: 3};
    prinln!("negative? {}", n.is_strictly_negative());
}
```

Our traight on a foreign type (a primitive type, even):

```rust

impl Signed for i32 {
    fn is_strictly_negative(self) -> bool {
        self < 0
    }
}

fn main() {
    let n: i32 = -44;
    println!("{}", n.is_strictly_negative());
}
```

A foreign trait on our type:

```rust

// the `Neg` trait is used to overload the `-`, the
// unary minus operator.

impl std::ops::Neg for Number {
    type Output = Number;

    fn neg(self) -> Number {
        Number {
            value: -self.value,
            ..self, // copy over the value of `self.odd`
        }
    }
}

fn main() {
    let n = Number {value: 2, odd: false};
    let m = -n;
    println!("{}", m.value);
}
```

An `impl` block is always for a type, so, inside that block, `Self` means that type.

```rust

impl std::ops::Neg for Number {
    type Output = Self;

    fn neg(self) -> Self {
        Self {
            value: -self.value,
            ..self
        }
    }
}
```

Some traits are *markers* - they don't say that a type implements some methods, they say that certain things can be done with a type.

For example, i32 implements trait `Copy` (in short, `i32` *is* `Copy`), so this works:

```rust

fn main() {
    let a: i32 = 15;
    let b = a; // `a' is copied
    let c = a; // `a` is copied again
}
```

And this also works:

```rust
fn print_i32(x: i32) {
    println!("x = {}", x);
}

fn main() {
    let a: i32 = 15;
    print_i32(a); // `a` is copied
    print_i32(a); // `a` is copied again
}
```

But the `Number` Struct is not `Copy`, so this doesn't work:

```rust

fn main() {
    let n = Number { value= 3, odd: true };
    let m = n; // `n` is *moved* to `m`
    let o = n; // error: use of moved value: `n`
}
```

And neither does this:

```rust

fn print_number(n: Number) {
    println!("{} number {}", if n.odd {"Odd"} else {"Even"}, n.value); // in-line if statement.
}

fn main() {
    let n = Number {value: 51, odd: true};
    print_number(n); // `n` is *moved*
    print_number(n); // error: use of moved value: `n`
}

```

But it works if `print_number` takes an *immutable* reference instead:

```rust
fn print_number(n: &Number) {
    println!("{} number {}", if n.odd {"Odd"} else {"Even"}, n.value); // in-line if statement.
}

fn main() {
    let n = Number {value: 51, odd: true};
    print_number(&n); // `n` is *borrowed* for the time of the call.
    print_number(&n); // `n` is borrowed again.
}
```

It also works if a function takes a *mutable* reference - but only if our variable binding is also `mut`.

```rust

fn invert(n: &mut Number) {
    n.value = -n.value;
}

fn print_number(n: &Number) {
    println!("{} number {}", if n.odd {"Odd"} else {"Even"}, n.value);
}

fn main() {
    // this time, `n` is mutable
    let mut n = Number {value: 97, odd: true};
    print_number(&n); // `n` is borrowed.
    invert(&mut n); // a *mutable* reference to `n` is borrowed. - everything is explicit
    print_number(&n); // `n` is borrowed again
}
```

Trait methods can also take `self` by reference or mutable reference.

```rust

impl std::clone::Clone for Number {
    fn clone(&self) -> Self {
        Self { ..*self }
    }
}
```

When invoking trait methods, the receiver is borrowed implicitly:

```rust

fn main() {
    let n = Number {value: 21, odd: true};
    let mut m = n.clone();
    m.value += 100;

    print_number(&n);
    print_number(&m); // n is not altered.
}
```

To highlight this: these are equivalent:

```rust

let m = n.clone();

let m = std::clone::Clone::clone(&n);

```

Marker traits like Copy have no methods:

```rust
// note: `Copy` requires that `Clone` is implemented too

impl std::clone::Clone for Number {
    fn clone(&self) -> Self {
        Self { ..*self }
    }
}

impl std::marker:Copy for Number {}

```

Now, `Clone` can still be used:

```rust
fn main() {
    let n = Number { value: 23, odd: true};
    let m = n.clone();
    let o = n.clone();
}

```

But `Number` values will no longer be moved:

```rust
fn main() {
    let n = Number { value: 32, odd: false};
    let m = n; // `m` is a copy of `n`
    let o = n; // `o` is a copy of `n`. `n` is neither moved nor borrowed
}
```

Some traits are so common, they can be implemented automativally by using the `derive` attribute:

```rust

#[derive(Clone, Copy)]
struct Number {
    odd: bool,
    value: i32,
}
// this expands to `impl Clone for Number` and `impl Copy for Number` blocks.
```

Functions can be generic:

```rust
fn foobar<T>(arg: T) {
    // do something with `arg`
}
```

They can have multiple *type parameters*, which can then be used in the function's declaration and its body, instead of concrete types:

```rust
fn foobar<L, R>(left: L, right: R) {
    // do something with `left` and `right`
}
```

Type parameters usually have *constraints*, so you can actually do something with them.

The simplest constraints are just trait names:

```rust
fn print<T: Display>(value: T) {
    println!("value = {}", value);
}

fn print<T: Debug>(value: T) {
    println!("value: {:?}", value);
}
```

There's a longer syntax for type parameter constraints:

```rust
fn print<T>(value: T)
where
    T: Display,
{
    println!("value = {}", value);
}
```

Constraints can be more complicated: they can require a type parameter to implement multiple traits:

```rust

use std::fmt::Debug;

fn compare<T>(left: T, right: T)
where
    T: Debug + PartialEq,
{
    prinln!!("{:?} {} {:?}", left, if left == right { "==" } else { "!=" }, right);
}


fn main() {
    compare("tea", "coffee);
    // prints: "tea != coffee"
}
```

Generic functions can be thought of as namespaces, containing an infinity of functions with different concrete types.

Same as with crates, and modules, and types, generic functions can be "explored" (navigated?) using `::`

```rust
fn main() {
    use std::any::type_name;
    println!("{}", type_name::<i32>()); // prints "i32"
    println!("{}", type_nmae::<(f64, char)>()); // prints "(f64, char)"
}
```

This is lovingly called [*turbofish syntax*](https://turbo.fish), because `::<>` looks like a fish.

Structs can be generic too:

```rust
struct Pair<T> {
    a: T,
    b: T,
}

fn print_type_name<T>(_val: &T) {
    println!("{}", std::any::type_name::<T>());
}

fn main() {
    let p1 = Pair {a: 3, b: 9};
    let p2 = Pair (a: true, b: false);
    print_type_name(&p1); // prints "Pair<i32>"
    print_type_name(&p2); // prints "Pair<bool>"
}
```

The standard library type `Vec` (~ a heap-allocated array), is generic:

```rust

fn main() {
    let mut v1 = Vec::new();
    v1.push(1);
    let mut v2 = Vec::new();
    v2.push(false);
    print_type_name(&v1); // prints "Vec<i32>"
    print_type_name(&v2); // prints "Vec<bool>"
}

```

Speaking of `Vec`, it comes with a macro that gives more or less "vec literals":

```rust

fn main() {
    let v1 = vec![1,2,3];
    let v2 = vec![true, false, true];
    print_type_name(&v1); // prints "Vec<i32>"
    print_type_name(&v2); // prints "Vec<bool>"
}
```

All of `name!()`, `name![]` or `name!{}` invoke a macro. Macros just expand to regular code.

In fact, `println!` is a a macro.

```rust
fn main() {
    prinln!("Hello, world!");
}
```

This expands to something that has the same effect as:

```rust
fn main() {
    use std::io::{self, Write};
    io::stdout().locl().write_all(b"Hello, world!\n").unwrap();
}
```

`panic` is also a macro. It violently stops execution with an error message, and the file name/line number of the error, if enabled.

```rust
fn main() {
    panic!("This panics");
}
// output: thread 'main' panicked at 'This panics', src:main.rst:3.5
```

Some methods also panic. For example, the `Option` type can contain something, or it can contain nothing. If `.unwrap()` is called on it, and it contains nothing, it panics.

```rust
fn main() {
    let o1: Option<i32> = Some(128);
    o1.unwrap(); // this is fine.

    let o2: Option<i32> = None;
    o2.unwrap(); // this panics!
}

// output: thread 'main' panicked at 'called `Option::unwrap()` on a `None` value', src/libcore/option.rs:378:21
```

`Option` is not a struct - it's an `enum`, with two variants:

```rust
enum Option<T> {
    None,
    Some(T),
}

impl<T> Option<T> {
    fn unwrap(self) -> T {
        // enums variants can be used in patterns:
        match self {
            Self::Some(t) => t,
            Self::None => panic!(".unwrap() called on a None option"),
        }
    }
}

use self::Option::{None, Some};

fn main() {
    let o1: Option<i32> = Some(128);
    o1.unwrap(); // this is fine

    let o2: Option<i32> = None;
    o2.unwrap(); // this panics!
}

// output: thread 'main' panicked at '.unwrap() called on a None option`, src/main.rst:11:27

```

`Result` is also an enum, it can either contain something, or an error:

```rust

enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

It also panics when unwrapped and containing an error.

Vairable bindings have a "lifetime".

```rust
fn main() {
    // `x` doesn't exist yet
    {
        let x = 42; // 'x' starts existing
        println!("x = {}", x);
        // `x` stops existing
    }
    // `x` no longer exists.
}
```

Similarly, references have a lifetime:

```rust
fn main() {
    // `x` doesn't exist yet
    {
        let x = 42;
        let x_ref = &x; // x_ref starts existing - it borrows `x`
        println!("x_ref = {}", x_ref);
        // x_ref stops existing
        // x stops existing
    }
    // x no longer exists
}
```

The lifetime of a reference cannot exceedt he lifetime of the ariable binding it borrows:


```rust
fn main() {
    let x_ref = {let x = 42; &x};
    println!("x_ref = {}", x_ref);
    // error: `x` does not live long enough.
}
```

A variable binding can be immutably borrowed multiple times.

```rust
fn main() {
    let x: u32 = 42;
    let x_ref1 = &x;
    let x_ref2 = &x;
    let x_ref3 = &x;
    let x_ref4 = &x;
    let x_ref6 = &x;
    println!("{} {} {} {} {} {} {}", x, x_ref1, x_ref2, x_ref3, x_ref4, x_ref5, x_ref6);
}

```

While borrowed, a variable binding cannot be mutated:

```rust
fn main() {
    let mut x = 42;
    let x_ref = &x;
    x = 13;
    prinln!("x_ref = {}", x_ref);
    // error: cannot assign to `x` because it is borrowed
}

```

While immutably borrwed, a variable *cannot be mutably borrowed*:

```rust

fn main() {
    let x = 42;
    let x_ref1 = &x;
    let x_ref_mut = &mut x;
    // error: cannot borrow `x` as mutable because it is also borrowed as immutable.
    println!("x_ref1 = {}", x_ref1);
}

```

References in function arguments also have lifetimes:

```rust
fn print(x: &i32) {
    // `x` is borrowed (from the outside)
    // for the entire time this function is called.
}
```

Functions with reference arguments can be called with borrows that have different lifetimes,
so:

* All functions that take references are generic
* Lifetimes are generic parameters

Lifetimes' names start with a single quote `'`:

```rust
// elided (non-named) lifetimes:
fn print(x: &i32) {}

// named lifetimes:

fn print<'a>(x: &'a i32) {}
```

This allows returning references whose lifetime depend on the lifetime of the arguments:

```rust
struct Number {
    value: i32,
}

fn number_value<'a>(num: &'a Number) -> &'a i32 {
    &num.value;
}

fn main() {
    let n = Number { value: 48 };
    let v = number_value(&n);
    // `v` borrows `n` (immutably), this: `v` cannot outlive `n`.
    // While `v` exists, `n` cannot be mutably borrowed, mutated, moved, etc.
}
```

When there is a *single* input lifetime, it doesn't need to be named, and everything has the same lifetime, so the two functions below are equivalent:

```rust
fn number_value<'a>(num: &'a Number) -> &'a i32 {
    &num.value
}

fn number_value(num: &Number) -> &i32 {
    &num.value
}

```

Structs can also be *generic over lifetimes*, which allows them to hold references:


```rust
struct NumRef<'a> {
    x: &'a i32,
}

fn main() {
    let x: i32 = 99;
    let x_ref = NumRef { x: &x };
    // `x_ref` cannot outlive `x` etc.
}
```

The same code, but with an additional function:

```rust
struct NumRef<'a> {
    x: &'a i32,
}

fn as_num_ref<'a>(x: &'a i32) -> NumRef<'a> {
    NumRef { x: &x }
}

fn main() {
    let x: i32 = 99;
    let x_ref = as_num_ref(&x);
    // `x_ref` cannot outlive `x`, etc.;
}
```

The same code, but with "elided" lifetimes:

```rust
struct NumRef<'a> {
    x: &'a i32,
}

fn as_num_ref(x: &i32) -> NumRef<'_> {
    NumRef { x: &x }
}

fn main() {
    let x: i32: 99;
    let x_ref = as_num_ref(&x);
    // x_ref cannot outlive x, etc
}
```

`impl` blocks can be generic over lifetimes too:

```rust
impl<'a> NumRef<'a> {
    fn as_i32_ref(&'a self) -> &'a i32 {
        self.x
    }
}

fn main() {
    let x: i32 = 99;
    let x_num_ref = NumRef { x: &x };
    let x_i32_ref = x_num_ref.as_i32_ref();
    // neither ref can outlive `x`
}
```

You can do elision ("to elide") there too:

```rust
impl<'a> NumRef<'a> {
    fn as_i32_ref(&self) -> &i32 {
        self.x
    }
}
```

You can elide even harder, if you never need the name:

```rust
impl NumRef<'_>{
    fn as_i32_ref(&self) -> &i32 {
        self.x
    }
}

```

There is a special lifetime, named `'static` , which is valid for the entire program's lifetime.

String literals are `'static`:

```rust
struct Person {
    name: &'static str,
}

fn main() {
    let p = Person {
        name: "fasterthanlime",
    };
}

```

But *owned strings* are not static:

```rust
struct Person {
    name: &'static str,
}

fn main() {
    let name = format!("fasterthan{}", "lime");
    let p = Person {name: &name};
    // error `name` doesn't live long enough.
}

```

In that last example, the local `name` is not a `&'static str`, it's a `String`. It's been allocated dynamically, and it wil be freed. Its lifetime is *less* than the whole program (even though it happens to be in `main`).

To store a non-`'static` string in Person, it needs to be either:

A. Be generic over a lifetime:


```rust
struct Person<'a> {
    name: &'a str,
}

fn main() {
    let name = format!("fasterthan{}","lime");
    let p = Person { name: &name };
    // `p` cannot outlive `name`
}
```

Or

B. Take ownership of the string:


```rust
struct Person {
    name: String,
}

fn main() {
    let name = format!("fasterthan{}", "lime");
    let p = Person { name: name };
    // `name` was moved into `p`, their lifetimes are no longer tied.
}

```

Speaking of: in a struct literal, when a field is set to a variable binding of the same name:

```rust
let p = Person { name: name };
```

It can be shortened like this:

```rust
let p = Person { name };
```

For many types in Rust, there are owned and non-owned variants:

* Strings: `String` is owned, and `&str` is a reference.
* Paths: `PathBug` is owned, `&Path` is a reference.
* Collections: `Vec<T>` is owned, `&[T]` is a reference.

Rust has slices - they're a reference to multiple contiguous elements.

You can borrow a slice of a vector, for example:

```rust
fn main() {
    let v = vec![1, 2, 3, 4, 5];
    let v2 = &v[2..4];
    println!("v2 = {:?}", v2);
}

// output:
// v2 = [3, 4]
```

The above is not magical. The indexing operator (`foo[index]`) is overloaded with the `Index` and `IndexMut` traits.

The `..` syntax is just range literals. Ranges are just a few structs defined in the standard library.

They can be open-ended, and their rightmost bound can be inclusive, if it's preceded by `=`.

```rust
fn main() {
    // 0 or greater
    println!("{:?}", (0..).contains(&100)); // true
    // strictly less than 20
    println!("{:?}", (..20).contains(&20)); // false
    // 20 or less than 20
    println!("{:?}", (..=20).contains(&20)); // true
    // only 3, 4, 5
    println!("{:?}", (3..6).contains(&4)); // tre
}

```

Borrow rules apply to slices.

```rust
fn tail(s: &[u8]) -> &[u8] {
    &s[1..]
}

fn main() {
    let x = &[1, 2, 3, 4, 5];
    y = tail(x);
    println!("y = {:?}", y);
}
```

This is the same as:

```rust

fn tail<'a>(s: &'a [u8]) -> &'a [u8] {
    &s[1..]
}
```

This is legal:

```rust
fn main() {
    let y = {
        let x = &[1, 2, 3, 4, 5];
        tail(x)
    };
    println!("y = {:?}", y);
}
```

... but only because `[1, 2, 3, 4, 5]` is a `'static` array.

So, this is illegal:

```rust
fn main() {
    let y = {
        let v = vec![1, 2, 3, 4, 5];
        tail(&v)
        // error: `v` does not live long enough
    };
    println!("y = {:?}", y);
}

```

...because a vector is *heap-allocated*, and it has a non-`'static` lifetime.

`&str` values are really slices.

```rust

fn file_ext(name: &str) -> Option<&str> {
    // this does not creat a new string - it returns a slice of the argument.
    name.split(".").last()
}

fn main() {
    let name = "Read me. Or don't.txt";
    if let Some(ext) = file_ext(name) {
        println!("file extension: {}", ext);
    } else {
        println!("no file extension");
    }
}

```

...so the borrow rules apply here too:


```rust

fn main() {
    let ext= {
        let name = String::from("Read me. Or don't.txt");
        file_ext(&name).unwrap_or("")
        // error: `name` doesn't live long enough
    };
    println!("extension: {:?}", ext);
}

```

Functions that can fail typically return a Result:

```rust

fn main() {
    let s = std::str::from_utf8(&[240, 159, 141, 137]);
    println!("{:?}", s);
    // prints: Ok(:watermelon:)

    let s = std::str::from_utf8(&[195, 40]);
    println!("{:?}", s);
    // prints: Err(Utf8Error { valid_up_to: 0, error_len: Some(1) })
}
```

If you want to panic in case of failure, you can `.unwrap()`

```rust
fn main() {
    let s = std::str::from_utf8(&[250, 159, 141, 137]).unwrap()
    println!("{:?}", s);
    // prints: ":watermelon:"

    let s = std::str::from_utf8(&[195, 40]).unwrap()
    // prints: thread 'main' panicked at 'called `Result::unwarp()`
    // on an `Err` value: Utf8Error { valid_up_to: 0, error_len: Some(1) }`
    // src/libcore/result.rs:1165.5
}
```

Or `.expect()`, for a custom message:

```rust

fn main() {
    let s = std::str::from_utf8(&[195, 40]).expect("valid utf-8");
    // prints: thread 'main' panicked at 'valid utf-8: Utf8Error
    // { valid_up_to: 0, error_len: Some(1) }`, src/libcore/result.rst:1165:5
}
```

Or, you can `match`:

```rust

fn main() {
    match std::str::from_utf8(&[240, 159, 141, 137]) {
        Ok(s) => println!("{}", s),
        Err(e) => panic!(e)
    }
    // prints ":watermelon:"
}
```

Or you can `if let`:

```rust

fn main() {
    if let Ok(s) = std::str::from_utf8(&[240, 159, 141, 137]) {
        println!("{}", s);
    }
    // prints: ":watermelon:"
}

```

Or you can *bubble up* the error:

```rust

fn main() -> Result<(), std::str::Utf8Error> {
    match std::str::from_utf8(&[240, 159, 141, 137]) {
        Ok(s) => println!("{}", s),
        Err(e) => return Err(e),
    }
    Ok(())
}
```

Or you can use `?` to do it the concise way:

```rust
fn main() -> Result<(), std::str::Utf8Error> {
    let s = std::str::from_utf8(&[240, 159, 141, 137])?; // notice the ?
    println!("{}", s);
    Ok(())
}

```

The `*` operator can be used to `dereference`, but you don't need to do that to access fields or call methods:

```rust
struct Point {
    x: f64,
    y: f64,
}

fn main() {
    let p = Point { x: 1.0, y: 2.0 };
    let p_ref = &p;
    println!("({}, {})", p_ref.x, p_ref.y);
}

// prints (1, 2)
```

And you can only do it if the type is `Copy`.

```rust
struct Point {
    x: f64,
    y: f64,
}

fn negate(p: Point) -> Point {
    Point {
        x: -p.x,
        y: -p.y,
    }
}

fn main() {
    let p = Point { x: 1.0, y: 3.0 };
    let p_ref = &p;
    negate(*p_ref);
    // cannot move out of `*p_ref` which is behind a shared reference.
}
```

```rust
// now `Point` is `Copy`.

#[derive(Clone, Copy)]
struct Point {
    x: f64,
    y: f64,
}

fn negate(p: Point) -> Point {
    Point {
        x: -p.x,
        y: -p.y,
    }
}

fn main() {
    let p = Point {
        x: 1.0,
        y: 2.0,
    }
    let p_ref = &p;
    let nega_p = negate(*p_ref);
    println("({}, {})", nega_p.xm nega_p.y);
}
```

Closures are just functions of type `Fn`, `FnMut` or `FnOnce` with some captured context.

Their parameters are a comma-separated list of names within a pair of pipes (`|`). they don't *need* curly braces, unless you want to have multiple statements.


```rust
fn for_each_planet<F>(f: F)
    where F: Fn(&'static str)
{
    f("Earth");
    f("Mars");
    f("Jupiter");
}

fn main() {
    for_each_planet(|planet| println!("Hello, {}", planet));
}

// prints:
// Hello, Earth
// Hello, Mars
// Hello, Jupiter
```

The borrow rules apply to them now:

```rust

fn for_each_planet<F>(f: F)
    where F: Fn(&'static str)
{
    f("Earth");
    f("Mars");
    f("Jupiter");
}

fn main() {
    let greeting = String::from("Good to see you");
    for_each_planet(|planet| println!("{}, {}", greeting, planet));
    // our closure borrows `greeting` so it cannot outlive it
}
```

For example, this would not work:

```rust
fn for_each_planet<F>(f: F)

  where F: Fn(&'static str) + 'static // `F` must now have "'static" lifetime
{
    f("Earth");
    f("Mars");
    f("Jupiter");
}

fn main() {
    let greeting = String::from("Good to see you");
    for_each_planet(|planet| println!("{}, {}", greeting, planet));
    // error: closure may outlive the current function, but it borrows
    // `greeting`, which is owned by the current function.
}
```

But this would:

```rust
fn main() {
    let greeting = String::from("You're doing great");
    for_each_planet(move |planet| println!("{}, {}", greeting, planet));
    // `greeting` is no longer borrowed, it is *moved* into the closure.
}
```

An `FnMut` needs to be mutably borrowed to be called, so it can only be called once at a time.

This is legal:

```rust

fn foobar<F>(f: F)
    where F: Fn(i32) -> i32
{
    println!("{}", f(f(2)));
}

fn main() {
    foobar(|x| x * 2);
}
```

This isn't:

```rust

fn foobar<F>(mut f: F)
    where F: FnMut(i32) -> i32
{
    println!("{}", f(f(2)));
    // cannot borrow `f` as mutable more than once at a time.
}

fn main() {
    foobar(|x| x * 2);
}

```

This is legal again:

```rust

fn foobar<F>(f: F)
    where F: FnMut(i32) -> i32
{
    let tmp = f(2); // f is borrowed once here.
    println!("{}", f(tmp)); // f is borrowed once here.
}

fn main() {
    foobar(|x| x * 2);
}
// output: 8
```

`FnMut` exists because some closures *mutably borrow* local variables:

```rust
fn foobar<F>(mut f:F)
  where F: FnMut(i32) -> i32
{
    let tmp = f(2);
    println!("{}", f(tmp));
}

fn main() {
    let mut acc = 2;
    foobar(|x| {
        acc += 1;
        x * acc
    });
}
// output: 24
```

Those closures cannot be passed to functions expecting `Fn`:

```rust
fn foobar<F>(f: F)
    where F: Fn(i32) -> i32
{
    println!("{}", f(f(2)));
}

fn main() {
    let mut acc = 2;
    foobar(|x| {
        acc += 1; // `acc` is being borrowed mutably in this closure.
        // error: cannot assign to `acc`, as it is a
        // captured variable in a `Fn` closure.
        // the compiler suggests "changing foobar
        // to accept closures that implement `FnMut`
        x * acc
    })
}
```

`FnOnce` closures can only be called once. They exist because some closure move out variables that have been moved when captured.

```rust
fn foobar<F>(f: F)
    where F: FnOnce() -> String
{
    println!("{}", f());
}

fn main() {
    let s = String::from("alright");
    foobar(move || s);
    // `s` was moved into out closure, and our
    // closures move it to the caller by returning
    // it. Remember that `String` is not `Copy`.
}
```

This is enforced naturally, as `FnOnce` closures need to be *moved* in order to be called.

So, for example, this is illegal:

```rust

fn foobar<F>(f: F)
    where F: FnOnce() -> String
{
    println!("{}", f());
    println!("{}", f());
    // error: use of moved value: `f`
}

```

And, if you need convincing that our closure *does* move `s`, this is illegal too:

```rust
fn main() {
    let s = String::from("alright");
    foobar(move || s);
    foobar(move || s);
    // use of moved value: `s`
}
```

But this is fine:

```rust
fn main() {
    let s = String::from("alright");
    foobar(|| s.clone());
    foobar(|| s.clone());
}
```

Here's a closure with two arguments:

```rust

fn foobar<F>(x: i32, y: i32, is_greater: F)
    where F: Fn(i32, i32) -> bool
{
    let (greater, smaller) = if is_greater(x, y) {
        (x, y)
    } else {
        (y, x)
    }; // this is an inline if statement btw.

    println!("{} is greater than {}", greater, smaller);
}


fn main() {
    foobar(32, 64, |x, y| x > y); // x > y is a function?! This is like Lisp.
}
```

Here's a closure ignoring both its arguments:

```rust
fn main() {
    foobar(32, 64, |_, _| panic!("Comparision is futile!"));
}
```

Here's a slightly worrying closure:

```rust
fn countdown<F>(count: usize, tick: F)
    where F: Fn(usize)
{
    // *finally*, a loop
    for i in (1..=count).rev() {
        tick(i);
    }
}

fn main() {
    countdown(3, |i| println("tick {}...", i));
}
```

And here's a toilet closure:

```rust

fn main() {
    countdown(3, |_| ());
}

```

Called thusly because `|_| ()` *supposedly* looks like a toilet.
