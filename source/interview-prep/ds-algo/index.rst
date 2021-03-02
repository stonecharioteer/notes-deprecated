=======================================
Data Structures and Algorithms
=======================================

This repository will hold my Python implementations of various data structures
and algorithms.

.. toctree::
    :maxdepth: 2

    algorithms/index

-----------------
Resources
-----------------

1. MIT 6.006 Introduction to Algorithms
2. Problem Solving with Algorithms and Data Structures using Python
3. Grokking Algorithms
4. MIT 6.046 Design and Analysis of Algorithms





.. _big-o-chart:

----------------------
Big O Chart
----------------------

.. plot::

   import matplotlib.pyplot as plt
   size = 5
   O_1 = [1 for _ in range(size)]
   O_N = list(range(size))
   O_N_2 = [x**2 for x in range(size)]
   O_N_3 = [x**3 for x in range(size)]
   O_N_4 = [x**4 for x in range(size)]

   plt.plot(O_1, label=r"O(1)")
   plt.plot(O_N, label=r"O(N)")
   plt.plot(O_N_2, label=r"O(N^2)")
   plt.plot(O_N_3, label=r"O(N^3)")
   plt.plot(O_N_4, label=r"O(N^4)")
   plt.legend()
   plt.ylabel("Steps Involved")
   plt.xlabel("Size of Input to the Algorithm")
   plt.grid()
   plt.title("Big O Performance")
   plt.show()
