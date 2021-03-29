.. _leetcode-0004:

=========================================
0004. Median of Two Sorted Arrays
=========================================

-------------------------
Problem Statement
-------------------------

`Leetcode Link <https://leetcode.com/problems/median-of-two-sorted-arrays/>`_

Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

Constraints
================

.. code-block:: javascript

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

Follow up: The overall run time complexity should be :math:`O(log (m+n))`.


.. tip::

    Remember that the *median* of a list is *that* item
    that divides the list into two equal halves, by population.

--------------------------
Examples
--------------------------


---------------------
Solution
---------------------

This is a good explanation targetting this problem: `Binary Search - Median of Two Sorted Arrays <https://youtu.be/LPFhl65R7ww>`_.

.. literalinclude:: solution.py
    :caption: Solution
    :linenos:
    :language: python
