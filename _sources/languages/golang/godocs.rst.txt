=============================
Golang Documentation
=============================

--------------------------
Observations on Golang
--------------------------

* Type-Safe
* Memory-Safe
* Garbage-Collected
* The combination of threads and garbage-collection is particularly interesting.
  * You don't need to figure out when a thread was using an object.
* Golang has always been said to be simple. What, 50 keywords?

------------------------------
The Golang Tutorial
------------------------------

`@3m <https://www.youtube.com/watch?v=gA4YXUJX7t8&?t=180s>`_
So I am supposed to take the Golang tutorial and then read Effective Go before
I proceed. Will do that.

My friend `Karthikeyan <https://tirkarthi.github.io/>`_ recommended
`Caleb Doxsey's An Introduction to Programming in Go <https://www.golang-book.com/books/intro>`_,
which is available for free at that link. However,
I will shelve perfection and completion in the language (for now),
and `I will focus on the official tutorial. <https://tour.golang.org/>`_


.. note::

    All code for this tutorial is in the same repository as these notes,
    but I will be including the code here as I go along.

    Additionally, the section on languages/golang will be a better segue
    into the language.

    In the folder golang, I am going to store all the go code I write
    to learn the language. It won't have anything to do with this course, but
    well.


.. code-block::go
    :linenos:

    package main

    import "fmt"

    func main() {
        fmt.Printf("hello, world\n")
    }

-------------------------------
Observations as a Pythonista
-------------------------------

* W00t! I am not writing semi-colons.
* Braces are okay. I can live with those.
* `import` uses *quotes*. I was *just* telling someone about this yesterday.
* `There is an interactive tutorial website. <https://tour.golang.org/welcome/>`_
* 2009-11-10 23:00:00 UTC is Golang's Birthday, apparently.
* The way go prints out the timestamp when I use :code:`time.Now()` is so weird.
    What are those extra numbers? It has the timezone, and that is great.
    But it also has something akin to :code:`m=+0.00086191`. What is that?
* Every Go Program is made up of Packages?
   * Not everyone realizes that Python is so similar. *Every* python "object" is an "object", complete with its own constructor and all.
   * Note to self: You can preach all the language agnosticism you want, but you cannot take the snake out of the snake charmer's basket.


.. code-block:: go
    :linenos:

    package main


    import (
        "fmt"
        "math/rand"
    )

    func main() {
        fmt.Println("My favorite number is ", rand.Intn(10))
    }


Wait. The output is *always* the same! The tour page says this:

    | Note: The environment in which these programs are executed is deterministic,
    | so each time you run the example program rand.Intn will return the same number.
    | (To see a different number, seed the number generator; see rand.Seed.
    | Time is constant in the playground, so you will need to use something else as the seed.)

Also, so importing ``math/rand`` allows me to use rand at the global level.

.. code-block:: go
    :linenos:

    package main

    import (
        "fmt"
        "math/rand"
    )

    func main() {
        rand.Seed(1091234017)
        fmt.Println("My favorite number is ", rand.Intn(10))
    }

Huh. The output remains constant every time I execute. So true random number
generation is not possible here? I wonder what Python does. I guess it uses
something the timestamp to generate the seed each time. You learn something new!

Go uses **tabs! Not spaces.** Heh. Pied Piper should have used Golang.

.. code-block:: go
    :linenos:

    package main

    import (
        "fmt"
        "math"
    )

    func main() {
        fmt.Println(math.Pi)
    }

So Go only exposes those variables that start with a capital first letter?
Works for me.

`Go's types come **after** the variable name. <https://blog.golang.org/declaration-syntax>`_
I like this, to be honest.

Oh wow. That article on declarations is **insane**. I can see why Python's
type hints took the ``x: int`` form now.

``a, b := 1, 2`` seems to be the way to define variable without declaring their
type. The types are implied from the variables on the right. This is not
usable outside of a function since every statement *must* begin with a keyword.

.. code-block:: go
    :linenos:

    package main

    import "fmt"

    func split(sum int) (x, y int) {
        x = sum * 4 / 9
        y = sum - x
        return
    }

    func main() {
        fmt.Println(split(17))
    }

Naming the return variables allows you to return them implicitly. I am not so
certain I would use that. Cannot see what it is useful. Perhaps in a way so I
can keep track of the returnable variable(s).

Go's types are interesting.

.. code-block:: go
    :linenos:

    package main

    import (
        "fmt"
        "math/cmplx"
    )

    var (
        ToBe   bool       = false
        MaxInt uint64     = 1<<64 - 1
        z      complex128 = cmplx.Sqrt(-5 + 12i)
    )

    func main() {
        fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
        fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
        fmt.Printf("Type: %T Value: %v\n", z, z)
    }


And the supported types are:

.. code-block:: go

    bool

    string

    int  int8  int16  int32  int64
    uint uint8 uint16 uint32 uint64 uintptr

    byte // alias for uint8

    rune // alias for int32
         // represents a Unicode code point

    float32 float64

    complex64 complex128


Go sets initial values to variables. They are either ``0``, ``false`` or ``""`` depending
upon the type.

Go assignment between items of different type requires an **explicit conversion**.
This is done through the type functions that perform the type casting.


The ``:=`` and the ``var =`` ways of declaring variables perform type inference,
as noted above.


Go supports immutable ``const``. These can infer types as well. Constants can
be character, string, boolean, or numeric values.

-----------------------
Looney Loopy Looping
-----------------------

.. code-block:: go
    :linenos:

    package main

    import "fmt"

    func main() {
        sum := 0
        for i := 0; i < 10; i++ {
            sum += i
        }
        fmt.Println(sum)
    }

Ah, those old C-variety loops. Braces are always required. No parentheses.

Interesting. The ``for`` can be turned into a ``while``-varient by just omitting
the instantiation and the increment.

    | C's `while` is spelled `for` in Go,

LOL.

-------------
Conditionals
-------------

Interesting why loops are introduced *before* conditionals. Is it easier to
grok?

.. code-block:: go
    :linenos:

    package main

    import (
        "fmt"
        "math"
    )

    func sqrt(x float64) string {
        if x < 0 {
            return sqrt(-x) + "i"
        } else {
            return fmt.Sprint(math.Sqrt(x))
        }
    }

    func main() {
        fmt.Println(sqrt(2), sqrt(-16))
    }

Hmm. ``fmt.Sprint()`` does string typecasting, does it?

.. code-block:: go
    :linenos:

    package main

    import (
        "fmt"
        "math"
    )

    func pow(x, n, lim float64) float64 {
        if v := math.Pow(x, n); v < lim {
            return v
        }
        return lim
    }

    func main() {
        fmt.Println(
            pow(3, 2, 10),
            pow(3, 3, 20),
        )
    }

Wait, so `:=` is sort of the walrus operator!! W00t.

Loops don't need parentheses here. That's good.

.. code-block:: go
    :linenos:

    package main

    import "fmt"

    func main() {
        sum := 0
        for i := 0; i < 10; i++ {
            sum += i
        }
        fmt.Println(sum)

        for sum < 1000 {
            sum += 100
        }
        fmt.Println(sum)

        for {
            fmt.Println("lol infinite loops")
        }
    }

The initialization and increment are optional, so there is no need for a while
or a do-while loop here. Good.

    >  `C's *while* is spelled *for* in Go. <https://tour.golang.org/flowcontrol/3>`_

That's hilarious. If only my old CS teacher Vasanth could see my face now.

`**Go's Conditional's have the *walrus operator*?!** <https://tour.golang.org/flowcontrol/6>`_

.. code-block:: go
    :linenos:

    package main

    import (
        "fmt"
        "math"
    )

    func pow(x, n, lim float64) float64 {
        if v := math.Pow(x, n); v < lim {
            return v
        }
        return lim
    }

    func main() {
        fmt.Println(
            pow(3, 2, 10),
            pow(3, 3, 10),
        )
    }


I am sold.

The variable defined in the ``if`` statement isn't accessible outside the statement,
but variables defined within the blocks are accessible outside the blog.
Such a weird decision. I mean, even Python does this but it is very weird.
