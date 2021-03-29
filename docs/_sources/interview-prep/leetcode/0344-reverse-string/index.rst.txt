.. _leetcode-0344:

=============================
0344. Reverse String
=============================

--------------------------------
Problem Statement
--------------------------------
`Leetcode Link <https://leetcode.com/problems/reverse-string/>`_

Write a function that reverses a string. The input string is given as an array
of characters ``char[]``.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with :math:`O(1)` extra memory.

You may assume all the characters consist of printable ascii characters.

-------------------------------
Examples
-------------------------------

.. code-block::
    :caption: Example 1

    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

.. code-block::
    :caption: Example 2

    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

----------------------
Solution
----------------------

.. literalinclude:: solution.py
    :caption: Solution
    :linenos:
    :language: python

.. note::

    Python specific advice, when you need to do this, just do ``list[::-1]``.
