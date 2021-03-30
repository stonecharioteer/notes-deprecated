.. _leetcode-0003:

================================================================
MEDIUM-🤔 0003. Longest Substring Without Repeating Characters
================================================================

-------------------------
Problem Statement
-------------------------

`Leetcode Link <https://leetcode.com/problems/longest-substring-without-repeating-characters/>`_

--------------------------
Examples
--------------------------


---------------------
Solution
---------------------

.. tab:: O(N^2) Time and O(N) Space complexity

    .. literalinclude:: solution_1.py
        :caption: Solution
        :linenos:
        :language: python

.. tab:: Sliding Window Implementation

    This implementation uses what is called a
    `Sliding Window Iterator <https://stackoverflow.com/questions/6822725/rolling-or-sliding-window-iterator>`_
    This is used when there are problems using a substring.

    .. literalinclude:: solution_2.py
        :caption: Solution
        :linenos:
        :language: python
