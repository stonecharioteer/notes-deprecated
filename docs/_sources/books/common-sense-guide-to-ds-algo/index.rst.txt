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
