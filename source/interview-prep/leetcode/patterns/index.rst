.. _leetcode-patterns:

===============================
Problem Patterns
===============================

When solving leetcode-style problems, it becomes simple to just assume you
need to brute-force your way through problems. However you will struggle if you
make this assumption. Instead, you should use some common problem solving methods
to make your life easier.

This section of my notes will go through some common patterns of problem solving.

.. _leetcode-patterns-sliding-window:

--------------------------------------------------
Sliding Window Pattern or Rolling Window Pattern
--------------------------------------------------

Whenever you need to create "groups" of consecutive items in a list,
you come to what is called a *sliding window* or *rolling window*.

What you are probably looking for is something like the maximum consecutive
matching items in a list, or max unique string. These problems become trivial if you
take the time to understand what a sliding window is.

Let's say you have the following list:

.. code-block:: python
    :linenos:

    sample = [1, 2, 3, 1, 4, 5, 8]

If you want to loop through sub-lists of this list, taking N at a time, you need to
imagine this as a sliding cursor of a particular length.

Perhaps at first go you select only one item, then two, then three. But suddenly you need to choose
only two again. This pattern allows you to do this.

In python, you can operate on a sliding window using itertools.


.. code-block:: python
    :linenos:

    from itertools import islice

    def window(sequence, n=2):
        """Returns a sliding window (of width n) over data from the iterable"""
        iterator = iter(sequence)
        result = tuple(islice(iterator, n))
        if len(result) == n:
            yield result
        for element in iterator:
            result = result[1:] + (elem, )
            yield result


Let's use this pattern to understand :ref:`leetcode-0003`.


.. literalinclude:: ../0003-longest-substring-without-repeating-characters/solution_2.py
    :caption: Longest Substring without Repeating Characters
    :linenos:
    :language: python


Consider an input string: :code:`"dvdf"`.

In the first pass, :code:`used_characters` does not contain any keys and the :code:`max_length` is set to 1.
Also, :code:`used_characters["d"]` is now set to 0, the index at which the character d was *last seen*.

In the second pass, since ``v`` is not stored in the dictionary, the ``max_length`` is
incremented and the index of this character is recorded.

In the third pass, now that ``d`` has reappeared, the *cursor* of the current *window* is shifted.

``start`` is set to *one* position *after* the *last* appearance of this character.

Hence, the window *slides* one to the right, and the ``used_characters`` dictionary is updated
for ``d`` to reflect ``2``, now the index at which ``d`` was *last seen*.

This repeats again, and the final character, ``f`` is registered. And this
yields the ``max_length`` of ``3``, which is the answer for this case.

This method of moving a *window* forward is useful because it lets us loop through a list
*once*, but also keeps a cursor that tells us where to begin the current range from.

This can be applied to :ref:`leetcode-0485` as well.
