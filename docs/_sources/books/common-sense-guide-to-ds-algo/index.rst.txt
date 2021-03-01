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
all the program needs to do is offet the memory position by n and return the value.

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

What is the Big O notation?

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
a number to get 1?

:math:`O(log_2N)`, for brevity: :math:`O(logN)`, measures how many times we need to divide a dataset
into halves to arrive at our result in the *worst case scenario*.


------------------------------------------------
Chapter 4 - Speeding Up Your Code with Big O
------------------------------------------------

.. note::

    Read up on the implementation of :ref:`bubble-sort`.


Bubble Sort has the following steps: cpmparisons, and swaps. Note how many times it loops through
an array.

No, not twice. For each element, it loops through the entire array.

Welcome to :math:`O(N^2)`. You do not want to be here.

Any polynomial with a power of 2 is a *quadratic* polynomial. On a graph, it would look like
a *parabola*, but not one that ever touches the ground like someone throwing a ball.
No, this is an upwards-facing parabola. That means if you have 1 million data points, your algorithm
will need to process :math:`1000000^2` items. A million *squared.*

Any algorithm wherein you loop through the entire list, or even portions of the
list but perhaps have a worst-case scenario where you loop through the entire
list is of this order. If you can avoid it, do not implement one of these.

:math:`O(N^3)` exists. Hope that you do not meet him.

-------------------------------------------------------
Chapter 5 - Optimizing Code With and Without Big O
-------------------------------------------------------


---------------------------------------------------------------
Chapter 6 - Optimizing for Optimistic Scenarios
---------------------------------------------------------------

---------------------------------------------------------------
Chapter 7 - Big O in Everyday Code
---------------------------------------------------------------

---------------------------------------------------------------
Chapter 8 - Blazing Fast Lookup with Hash Tables
---------------------------------------------------------------

---------------------------------------------------------------
Chapter 9 - Crafting Elegant Code with Stacks and Queues
---------------------------------------------------------------

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
