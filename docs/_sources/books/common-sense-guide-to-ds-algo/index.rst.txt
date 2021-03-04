.. _common-sense-guide:

====================================================================================
A Common Sense Guide to Data-Structures and Algorithms - Jay Wengrow
====================================================================================


.. _common-sense-guide-why-data-structures-matter:

---------------------------------------
Chapter 1 - Why Data Structures Matter
---------------------------------------

The Array
------------

An array is a contiguous dataset. While we might say, in Python:

.. code-block:: python
    :linenos:

    some_array = [10, 21, 2, 0, 8, 72, 8]
    print(some_array[3])

Internally, the *machine* stores the length of the array, and the position of the first item.

Then, the computer can access the nth item by offsetting from the first. So to get the first item,
you offset 0, to get the second, you offset 1.

This is why you get the 0-based indexing everywhere. Makes a lot of sense now that I think about it.
I wonder how Visual Basic manages the 1-based index.

So for the computer, to access an item in a list, it is a single step. If you ask for the nth item,
all the program needs to do is offset the memory position by n and return the value.

.. note::

    If the array's length < n, then you have a stack overflow. The program is trying to access memory that is
    not its own. It's like trying to overdraw from your bank vault and reaching into the vault next to yours.


In a data structure, you perform the following operations:

#. Read
#. Search
#. Insert
#. Delete

When we want to measure the speed of these operations, this is where the entire idea of how a data structure
is organized comes in. This is why some data structures are suitable for some usages, while some are not.

.. note::

    This book's section on data structures and why Array indexing is O(1) is quite good. Do give it a reread
    again.


For an array of size N:

#. Getting item at index n: 1 step
#. Setting item at index n: 1 step
#. Appending 1 item to the end: 1 step
#. Prepending 1 item to the beginning: N+1 steps
#. Deleting an item in the list: N steps (1 step is the best case scenario, when you delete the last item)


.. admonition:: Protip
    :class: info

    For algorithmic speed measurement, always be a pessimist.
    Consider only the worst case scenario.


The Set
--------

A set is an array of unique values. There are no duplicates.

.. note::

    This is a generalization, but we'll get to that in time.


Most set operations are *identical* to arrays. However, **insertion** is where sets and arrays
differ.

Appending or prepending and item into a set of N items will take N steps. That's because a set
needs to fulfil its prime objective: no duplicates. To insert an item ``i`` into a set N,
you will first need to search the *entire* set for the occurrence of ``i``, and only when it
doesn't exist, do you insert it into the set.

------------------------------------
Chapter 2 - Why Algorithms Matter
------------------------------------

While data-structures have their own performance attributes, so do algorithms in general.

Ordered Arrays
----------------

An ordered array is almost identical to the *classic* array*, but the one caveat is that in an
ordered array, the items are *in order*.

This has its benefits, but let's look at its performance.

#. Read - 1 step
#. **Insertion - N + 2 steps**
#. Deletion - N steps

Insertion again takes N + 2 steps because *the item needs to be inserted into the right location.*
You cannot just insert an item at the very end.

Searching Ordered Arrays
============================

While searching normal arrays is a matter of looking at *each and every* item, this is not necessarily
so with an ordered array. Instead, we can use :ref:`binary-search`.

.. note::

    All source is going to be placed in their respective topic folder.

Binary Search will *halve* its steps each time it compares values to the search value.
So there will be :math:`log_2N` steps involved. It *narrows* its results down into a *binary*
answer, hence the name.

.. admonition:: Protip
    :class: info

    To understand what :math:`log_2N` means, or what :math:`log_MN` means, read
    :ref:`The Algorithm Design Manual's chapter on Logarithms <algorithm-design-manual-logarithms>`.


**Q**: For an ordered array with 100 elements, binary search takes 7 steps. How many steps does it take for 200 elements?

**A**: 8 steps

.. admonition:: Protip
    :class: info

    *Every time* the number of elements doubles, the steps involved in Binary Search increases by 1.

.. admonition:: Protip
    :class: info

    The Logarithm of N to the base M shows how many times N can be divided by M.

    :math:`log_2N` shows how many times N can be *halved*.

    :math:`log_{10}N` shows how many times N can be divided into tenths.


-----------------------------------
Chapter 3 - O Yes! Big O Notation
-----------------------------------

.. note::

    This book ignores most of the mathematical basis for Big O, and explains stuff
    rather simply. I recommend this section a lot. However, for a mathematical
    explanation, read :ref:`The Algorithm Design Manual's sections on Big O <algorithm-design-manual-big-o>`.


Big O measures how many steps an algorithm will take in relation to its input size.

    | If there are N data elements, how many steps will the algorithm take?

:math:`O(N)` says that the answer to the key question is that the algorithm will take N steps.

.. warning::

    If you have preconceived notions about Big O, please leave them at the door, *for now.*


Consider the following:

.. code-block:: python
    :linenos:

    def do_something(arr):
        length = len(arr)
        mid = arr[length // 2]
        print(f"{length=}, {mid=}")


How many steps is does this code example take?

The answer is 3.

What is Big O notation?

:math:`O(1)`.

    | The soul of Big O is what Big O is truly concerned about: how will an
    | algorithm's **performance** change as the data increases?

Big O doesn't care how many steps the algorithm *actually takes*. It instead cares about the
rate of change of an algorithm given change in the input data.

:math:`O(1)` and :math:`O(3)` mean the same to Big O. This algorithm has *no* relationship with
the input data. **It will not get slower or faster given more or less data**.

:math:`O(N)` is a different matter, however. It means that the algorithm has a *linear* relationship
with the data.


.. code-block:: python
    :linenos:

    def do_something(arr):
        length = len(arr)
        mid = arr[length // 2]
        print(f"{length=}, {mid=}")
        for element in arr:
            print(f"{element=}")
            print(f"{2*element=}")


Here, the algorithm seems to take :math:`O(2N+3)` steps.
:math:`2N+3` is a linear polynomial. Wait, I promised no mathematics. It means that it
is a statement that can be *conceived* as a straight line on a graph.

To Big O, the number next to :math:`N` *does not matter*. Neither does the value 3 that is at the end.

In Big O terms, the above program has a runtime of :math:`O(N)`.

Big O is also a *worst-case-scenario* measure. For an algorithm, always consider the **worst case scenario**
when denoting it in Big O terms. Linear search *might* take 1 step if your first item is the item you were looking for,
but in an array of size N, if it's the last item you're looking for, you need N steps. Big O in this scenario
is :math:`O(N)`, **not** :math:`O(1)`.

Big O concerns itself with Logarithms quite a lot. Logarithms are the opposite of exponents.

:math:`2^3` is 8. Then, :math:`log_28` is 3.

:math:`10*2` is 100. Then, :math:`log_{10}100` is 2.

An alternative way of thinking about logarithms is: *how many times do we need
to halve (or thirds, or tenths, depending on the :math:`log_NM` base N)
a number to get 1?*

:math:`O(log_2N)`, for brevity: :math:`O(logN)`, measures how many times we need to divide a dataset
into halves to arrive at our result in the *worst case scenario*.


------------------------------------------------
Chapter 4 - Speeding Up Your Code with Big O
------------------------------------------------

.. note::

    Read up on the implementation of :ref:`bubble-sort`.


Bubble Sort has the following steps: comparisons, and swaps. Note how many times it loops through
an array.

No, not twice. For each element, it loops through the entire array. In fact, it *doesn't*
know if an array is sorted until it loops through the array at least once.

Welcome to :math:`O(N^2)`. You do not want to be here.

Any polynomial with a power of 2 is a *quadratic* polynomial. On a graph, it would look like
a *parabola*, but not one that ever touches the ground like someone throwing a ball.
No, this is an upwards-facing parabola. That means if you have 1 million data points, your algorithm
will need to process :math:`1000000^2` items. A million *squared.*

Any algorithm wherein you loop through the entire list, or even portions of the
list but perhaps have a worst-case scenario where you loop through the entire
list is of this order. If you can avoid it, do not implement one of these.

:math:`O(N^3)` exists. Just pray that you do not meet him or his cousins.

-------------------------------------------------------
Chapter 5 - Optimizing Code With and Without Big O
-------------------------------------------------------

.. note::

    Read up on the implementation of :ref:`selection-sort`.

In :ref:`selection-sort`, you loop through the array to find the smallest item
and *swap* it with the first item. This *first* item is, in fact, a cursor
which moves ahead and marks the *sorted* part of the array.

For each item in the array, Selection Sort looks *ahead* at the rest of the
items in the array, comparing them and seeing if there's something *smaller*
than this item. It then *selects* the smallest item, if it is not the current
item, and swaps it with the current item.

This way, after the first passthrough, the smallest item is right at the front.
The algorithm ensures that at the Nth passthrough, the first N items are *in
order* at the front of the array.

So let's look at Selection Sort and Bubble Sort together.

Selection Sort has to look at the rest of the items for each item in the list.

Bubble Sort has to look at the entire list for each item in the list.

While this seems straight forward, and no one will fault you for saying
Selection Sort is *faster* (exactly *half* the runtime) than Bubble Sort,
however, **this does not matter to Big O**.

    | But here's the funny thing in the world of Big O Notation: Selection Sort
    | and Bubble Sort are described in **exactly the same way**.

.. admonition:: Protip
    :class: info

    Remember to leave your knowledge or preconceived notions of Big O at the
    door.  *All* you need to do is check this:

    Does the algorithm have nested loops?

    The exact time **does not matter**.


Why?

**Big O Notation ignores constants.**

It is easy to say Selection Sort is a :math:`O(N^2/2)` algorithm. It would seem
*common* sense.

However, consider the fact that the length of the array could grow *astronomically*.
If you have an infinitely large array, then it does not matter.

:math:`O(N^2/2)` is just :math:`O(N^2)`.

:math:`O(N/2+50000)` is just :math:`O(N)`.

:math:`O(100000)` is just :math:`O(1)`.

Big O Categories
------------------

Big O ignores the constants because it uses categories.

  | Big O Notation only concerns itself with *general categories* of algorithm speeds.

..


  | If we were to compare two buildings, one of which is a single-family home and
  | one of which is a skyscraper, it becomes almost moot to mention how many floors each one has.
  | Because the two buildings are so incredibly different in their sizes and functions.

This is the idea behind Big O. It categorizes algorithms into buckets wherein the bucket itself
is a *definitive* measure of how quickly the algorithm grows with input data.

It won't matter if your :math:`O(1)` algorithm takes 10 minutes to run or if
your :math:`O(N^2)` takes 1 :math:`{\mu}s`, *at least not to Big O*, because it
**doesn't care how long each step takes**, only how many steps there will be in
relation to larger data set sizes.

  | Talking about :math:`O(2N)` when compared to :math:`O(N^2)` is like talking
  | about a two-story house compared to a skyscraper.

..


---------------------------------------------------------------
Chapter 6 - Optimizing for Optimistic Scenarios
---------------------------------------------------------------


  | [T]he worst-case scenario isn't the *only* scenario worth considering.

..

  | :ref:`insertion-sort` is a sorting algorithm that reveals the power of analyzing
  | scenarios beyond the worst-case.


Insertion Sort involves: *removals*, *comparisons*, *shifts*, and *insertions*.

  | Big O Notation only takes into account the highest order of N when we have multiple
  | orders added together.

This means that:

:math:`O(N^2 + 2N)` = :math:`O(N^2)`

:math:`O(N^4 + N^3 + N^2)` = :math:`O(N^4)`

This is because as :math:`N` increases, the higher order values become *so much larger*
than the lower-order ones that it becomes trivial to account for them.

.. note::

    Take a look at :ref:`this chart <big-o-chart>` to understand the severity with which
    these categories vary.

In the worst-case scenario, Selection Sort is *faster* than Insertion Sort. However, it is
not the case when we look at the average case.

Best, Average and Worst cases follow a Bell Curve, showing that the worst case is, just like the
best case, an **outlier**.

.. list-table::

   * -
     - Best Case
     - Average Case
     - Worst Case
   * - Selection Sort
     - :math:`O(N^2/2)`
     - :math:`O(N^2/2)`
     - :math:`O(N^2/2)`
   * - Insertion Sort
     - :math:`O(N)`
     - :math:`O(N^2/2)`
     - :math:`O(N^2)`

..

  | Being able to discern between best-, average- and worst-case scenarios is a
  | key skill in choosing the best algorithm for your needs, as well as taking
  | existing algorithms and optimizing them further to make them significantly
  | faster. [W]hile it's good to be prepared for the worst case, average cases
  | are what happen most of the time.

---------------------------------------------------------------
Chapter 7 - Big O in Everyday Code
---------------------------------------------------------------

.. note::

    I don't have much to say about this chapter beyond that I really appreciate it being there.
    It **nails** the Big O Notation mindset into you, and so far, I've enjoyed it.

    The problems solutions are fairly easy, and it's a chapter you *should* read if you
    haven't grokked Big O yet.


.. admonition:: Protip
    :class: info

    If an algorithm has 2 inputs of length :math:`N` and :math:`M`
    and it has a nested for loop that loops through them, then what
    would have been :math:`O(NxM)` is reduced to :math:`O(N^2)`
    because in the worst-case scenario, both these arrays would
    be the same size.

---------------------------------------------------------------
Chapter 8 - Blazing Fast Lookup with Hash Tables
---------------------------------------------------------------

A **Hash Table** is a data structure in which the indices
are *hashed* and correlated with values in an array-like structure.

The example this book uses is alphabet-based hashing, using the
product of the numberic value of each alphabet.

"dog" becomes :math:`4*15*7 = 420`, and the *corresponding* value
associated with "dog" is stored in the 420 :sup:`th` location of
an array that holds the *values* of the Hash Table.

This lookup mechanism is usually designed with the following
assumptions

1. The *hashing* of a *key* **always** yields the same value. This way, there can be a 1:1
   relationship between *keys* and their *values*.
2. The hashing is non-random, and doesn't depend on execution time or machine. This enables
   the datastructure to be written to disk, if need be.

The efficiency of a hash table depends on three factors:

#. How much data we're storing in the hash table.
#. How many cells are available in the hash table.
#. Which hash function we're using.

  | A good hash function is one that distributes its data across **all**
  | available cells. The more we can spread our data, the fewer collisions
  | we will have.

..

  | A good hash table **strikes a balance of avoiding collisions while not
  | consuming lots of memory.**
  |
  | To accomplish this, computer scientists have developed the following rule of thumb:
  | for every 7 data elements stored in the hash table, it should have 10 cells.


Hash tables have a lookup efficiency of :math:`O(N)`.

Hash tables are used in places where you'd usually use plenty of ``if-else-if-else``
statements. Or, you'd use them when you want to store information about a single
entity together. This is most-visible in the ``JSON`` data format.

.. literalinclude:: anagram.py
    :language: python
    :linenos:
    :caption: Algorithm to determine whether two words are anagrams.

Using a **dictionary**, Python's implementation of a Hash Table, here,
gives us an algorithm of :math:`O(N)` order.

Exercises
------------

.. literalinclude:: intersect.py
    :language: python
    :linenos:
    :caption: Algorithm to yield the intersection of two arrays.


.. todo::

    Do the other exercises.

.. todo::

    Write an implementation of Hash Tables in Rust and Python.

---------------------------------------------------------------
Chapter 9 - Crafting Elegant Code with Stacks and Queues
---------------------------------------------------------------

Stacks
--------

A stack is *almost* an array, except:

#. Data can be inserted only at the end of a stack.
#. Data can be deleted only from the end of a stack.
#. Only the last element of a stack can be read.

The *end* of a stack is referred to as its *top*, and the *beginning* of
the stack is referred to as its **bottom**.

.. admonition:: Protip
    :class: info

    In Python, a simple list *can* be used as a Stack, since lists
    support ``pop`` and ``push`` methods. However, it is better to
    write a wrapper around a regular list since this way you can
    code checks in place so that users cannot insert an item wherever
    they want.

---------------------------------------------------------------
Chapter 10 - Recursively Recurse with Recursion
---------------------------------------------------------------

---------------------------------------------------------------
Chapter 11 - Learning to Write in Recursive
---------------------------------------------------------------

---------------------------------------------------------------
Chapter 12 - Dynamic Programming
---------------------------------------------------------------

---------------------------------------------------------------
Chapter 13 - Recursive Algorithms for Speed
---------------------------------------------------------------

---------------------------------------------------------------
Chapter 14 - Node-Based Data Structures
---------------------------------------------------------------

-------------------------------------------------------------------
Chapter 15 - Speeding Up All the Things with Binary Search Trees
-------------------------------------------------------------------

---------------------------------------------------------------
Chapter 16 - Keeping Your Priorities Straight with Heaps
---------------------------------------------------------------

---------------------------------------------------------------
Chapter 17 - It Doesn't Hurt to Trie
---------------------------------------------------------------

---------------------------------------------------------------
Chapter 18 - Connecting Everything with Graphs
---------------------------------------------------------------

---------------------------------------------------------------
Chapter 19 - Dealing with Space Constraints
---------------------------------------------------------------

---------------------------------------------------------------
Chapter 20 - Techniques for Code Optimization
---------------------------------------------------------------
