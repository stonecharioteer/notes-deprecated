==============================
How Linux Works by Brian Ward
==============================

Author: Brian Ward
Timeline: 2020-10-25 till date.

------------
Objective
------------

I have been using Linux since 2007, but I have not dived into
the depths of the topic. I would like in-depth Linux Kernel
knowledge, so that I can both appreciate the system better
and be a more powerful developer.

However, I would like objective goals:

1. Be able to analyse system performance.
2. Be able to compile kernels from source and boot them.
3. Be able to edit the grub bootloader config.
4. Be able to debug a running process using syslogs.

The fact that I do not yet know what I would like to do is
proof that I lack definitive knowledge of the system.

---------------------------
Chapter 1 The Big Picture
---------------------------

The Linux Kernel provides libraries and interfaces with which
programs can interact with devices. Although, as this book
details later, what the Kernel considers to be devices is
quite interesting.

--------------------
Process Management
--------------------

Linux Process Management involves the starting, pausing, resuming
and termination of processes.

Linux processes share compute time by performing operations within
allocated **time slices**. These time slices give processes enough time
for some significant computation, and are extremely small.

This time-sharing is perceived as multi-tasking. And it is called
*context switching*.

Questions I have on the topic:

1. Can kernel time slice lengths be configured?
2. How does a kernel record the status of a process before context-switching?
3. And when ready to context-switch, how does the kernel know which to pick next?
4. What is CPU user mode?
5. How does a process get *interrupted*?
6. What is kernel mode?

The Kernel runs inbetween processes during a context-switch.


Memory Management
---------------------

The Commandments for Memory Management:

1. The Kernel Keepeth its own private, inaccessible memory space.
2. Unto each process is its own section of memory.
3. Thou shalt not covet thy neighbour's memory space.
4. If thou chooseth, some sections of thine memory may not be altered.
5. The System may useth the disks as though they were like unto memory, should it need to.

Device Drivers and Management
------------------------------

A device is typically accessible only in Kernel mode, so as to prevent
improper access.

So can I think of *kernel mode* as what the CPU does inbetween
time slices so that it can execute kernel commands? Like when a
process asks to access a disk, the kernel has to respond during
the context switching?

System Calls and Support
------------------------------

System calls (:code:`syscalls`) perform specific tasks that a user process
alone cannot do well or at all. Opening files, reading or writing to
files, all qualify.

:code:`fork` and :code:`exec` are very important.

:code:`fork` instructs the kernel to create a nearly identical copy of the process.

:code:`exec` instructs the kernel to start a :code:`program` that is passed to
:code:`exec` and replace the current process.

*All* user processes, except :code:`init` start through :code:`fork`. You run :code:`exec`
to start a new program instead of running a copy of an existing
process.

Interestingly, this must be how virtualenvs cannot be sourced within
a shell script. Trying: :code:`ls` in a terminal, the shell calls :code:`fork` to
create copy of the current shell, start this, and then exit.

User Space
------------

The user-space or :code:`userland` is main memory that the kernel allocates
for user processes.

Users
--------

A user is an entity that can run processes and own files. A user is
associated with a username, but the kernel uses userids to identify
a user. User space processes are owned by a user, and processes
are run as a user.

:code:`root` is a privileged user which can terminate any other user's
processes and read/write any file on the file system.

:code:`root` might be powerful, but it *still runs in User mode, not kernel
mode*.

Groups are sets of users.

----------------------------------------------
Basic Commands and Directory Heirarchy
----------------------------------------------

The Bourne Shell :code:`/bin/sh`
-----------------------------------

A shell is a program that runs commands. The Bourne Shell, was
developed at Bell Labs. Linux uses the *Bourne-Again shell*,
commonly known as :code:`bash`.

Use :code:`chsh` to change the default shell on a Linux system.

Using the Shell
---------------------

:code:`echo` does not need quotes.

:code:`cat` performs concatenations on a list of files or input streams.

Standard Input and Standard Output
=====================================

Unix processes use I/O streams to read and write data. Streams are
very flexible: their source can be a file, a device, a terminal,
or even the output stream from another process.

Using :code:`cat` without an argument puts you into :code:`STDIN` mode, where
:code:`cat` will echo back everything you type into it. When you type,
you are sending inputs to :code:`STDIN`. :code:`cat` reads this and redirects
it to :code:`STDOUT`. (Use :code:`CTRL-D` to exit).

:code:`CTRL-D` stops :code:`STDIN` input on a terminal, and depending on the
program, terminates it. :code:`CTRL-C` terminates a program, irrespective
of the input or output.

Each process gets an :code:`STDOUT` stream to write to. :code:`cat` writes to
:code:`STDOUT`.

:code:`STDERR` is covered later.

Both these can be *redirected*.

Basic Commands
-------------------

Covers standard commands you should already know:
:code:`ls, cp, mv, touch, rm & echo`.

Navigating Directories
========================

Unix directory hierarchy begins at :code:`/`, called the root dir.
:code:`.` refers to the current diredctory. Paths can be *absolute*
(:code:`/usr/lib`) or *relative* (:code:`code/file1.txt` or :code:`./code/file1.txt`).

Covers :code:`cd, mkdir` and :code:`rmdir`.

The shell natively supports *simple* patterns, or *globs*.
Globs are *expanded before* running the commands.

:code:`*` (match anything, any length), and :code:`?` (match anything, 1 character)
are the most noteworthy in the beginning.

Intermediate Commands
------------------------

Use :code:`grep` to find a string within a directory. Note: *ripgrep* (:code:`rg`)
and *the_silver_searcher* (:code:`ag`) are *much, much faster.*

:code:`grep <find what> <find where>`

Note: If you use shell expansions (globbing) in the :code:`<find what>`
section, these are *expanded first*, and might not be what you want.

:code:`less` provides a scrolling view on :code:`stdout`. :code:`less` is :code:`more`, enhanced.

:code:`less` supports the :code:`/` search mechanism that :code:`vim` uses.

:code:`pwd` prints the current working directory. Use :code:`pwd -P` to resolve
symbolic links as well.

:code:`diff` is used to spot the differences between 2 files.
:code:`diff -u` provides a way for other programs to analyse the output.

:code:`file` can be used to guess the *file type* of a given file.

:code:`find <directory> -name <filename> -print` can be used to find a
certain file in a directory tree. Remember, if you must use :code:`*`,
enclose it in :code:`''` quotes. :code:`find <directory> -iname <filename>`
will turn off case-sensitivity.

:code:`locate` uses a cached file index for a file, and is faster
for this reason. However, if the file is newer than the index,
:code:`locate` won't find it.

:code:`head` and :code:`tail` return the top and bottom :code:`n` lines of a stream
respectively. :code:`head -<n>` will show :code:`<n>` number of lines.
:code:`tail +<n>` will print everything from line number :code:`<n>`.

Changing Your Password and Shell
-------------------------------------

:code:`passwd` can change the password, and :code:`chsh` can change the default
shell.

Dot Files
-------------

Files beginning with a :code:`.` are *configuration* files.
Linux programs use text based files for configuration.

Environment and Shell Variables
----------------------------------

:code:`STUFF=blah` is how you assign a value to a variable in the shell.
*Note the absence of spaces around the :code:`=`*. A shell variable is
local to the current process. However, an environment variable is
passed to processes spawned by this process as well.

Note that *all* environment variables are passed to child processes.


Child Processes and Inherited Environments
============================================

This creates interesting problems, such as needing to start a Python2
process from a Python3 environment. If you activate a virtualenv
and use :code:`subprocess.check_output` to run :code:`python`, the default Python
will be the same as the parent process (Python 3 here). If you
have a weird use case where you would want to do this, ensure you *don't*
source the *virtualenv*, instead, run the parent python script
using the *absolute path* to the virtual environment's python
executable (found in :code:`<envdir>/bin/python`). Again, note that
this is not the Python executable that was used to make the virtualenv.


The Command Path
------------------

:code:`PATH` is a very important Environment variable. It contains a :code:`:`
separated list of directories where the current shell will search
for commands.

This is an interesting scenario. Carefully, try :code:`export PATH=`,
to clear the value of :code:`PATH`. Now try running commands you've learnt
so far. If they execute, these are native unix commands. If they do not,
these are binaries that were possibly available in some of the library
folders such as :code:`/usr/bin`, :code:`/usr/local/bin` or :code:`/bin`.

When appending to the path, use :code:`export PATH=$PATH:<dir>`.

Command-Line Editing
------------------------

The default is :code:`emacs` mode. Sacrilege. Turn on :code:`vi mode`.

Text Editors
-----------------------


"[vi] plays a bit like a video game." LOL.

Getting Online Help
----------------------

:code:`man -k <keyword>` can be used when you want to search for a manual
page by a keyword.

:code:`man <section> command` can go to a section of a command.

:code:`man` sections
===================

1. User commands
2. System calls
3. Higher-level Unix programming library documentation
4. Device interface and driver information
5. File descriptions (system configuration files)
6. Games
7. File formats, conventions, and encodings (ASCII, suffixes, and so on)
8. System commands and servers

:code:`info` is a more detailed format for online manuals, adopted by the GNU Project.

Documentation can be sometimes found in :code:`/usr/share/doc`. However, :code:`man`
and :code:`info` do not read these.

Shell Input and Output
------------------------

:code:`command > file` can send the output of a file to a file, *clobbering* (erasing) the
contents of the original file. :code:`set -C` can prevent clobbering in bash.

:code:`command >> file` can append the output to the file.

:code:`command1 | command2` streams the :code:`stdout` of :code:`command1` to
the :code:`stdin` of :code:`command2`.

Standard Error
===================

:code:`STDERR` is an error stream. To redirect this, you need to use *stream II*
by using :code:`command 2> file`. To send :code:`STDERR` to :code:`STDOUT`, send
it to the address of :code:`stream 1`.

:code:`command 2>&1` merges both streams.

:code:`command > file 2>&1` will send both streams to a file.

Standard Input Redirection
============================

:code:`command < input` will send :code:`input` to the :code:`command` through :code:`STDIN`.

Understanding Error Messages
-----------------------------

Anatomy of a UNIX Error Message
==================================

Protip: Address errors on a first-come, first-serve basis.

Errors will have the following components:

1. The program name
2. The file name
3. The error

Example:

.. code:: bash

  $ ls /asdkl

  ls: cannot access /asdkl: No such file or directory


Common Errors
================

1. No such file or directory
2. File exists
3. Not a directory, Is a directory
4. No space left on device
5. Permission denied
6. Operation not permitted
7. Segmentation fault

Listing and Manipulating Processes
------------------------------------

A process is a running program.

:code:`ps`
===========

:code:`ps` is used to list processes.

:code:`ps x`: show all of your running processes.

:code:`ps ax`: show all processes on the system.

:code:`ps u`: include more detailed information.

:code:`ps w`: show full command names.

Killing Processes
===================

A processes can be *killed* using a *signal* from the Kernel.
Use the :code:`kill` command to send signals. A signal is a message
that the kernel sends to a process.

:code:`kill <pid>` send the :code:`TERM` signal to a process. This signal
tells the process that it needs to quit, and gives it time for
any cleanup, if needed.

:code:`kill -STOP <pid>` *freezes* a process. This way, the process can be
resumed.

:code:`kill -CONT <pid>` continues/resumes a frozen process.

:code:`kill -KILL <pid>` is the most brutal way to kill a process. This
will end the process without waiting for any cleanup.

Job Control
==============

Shells also support Job Control, a way to send :code:`TSTP` (similar to :code:`STOP`)
to a running process in the foreground using :code:`^Z`, and :code:`CONT` using
the :code:`fg` (bring to foreground) or :code:`bg` (continue in background) commands.

:code:`screen` and :code:`tmux` are good choices of programs to send noninteractive
programs to the background.

Background Processes
======================

Send any command directly to the background by suffixing the command
with :code:`&` before running it.

Note that when sending a process to the background, it is always
preferred to ensure that the :code:`stdout` and :code:`stdin` are remapped.

File Modes and Permissions
---------------------------

Every Unix file has a set of permissions that determine whether a user
can read, write, or run that file. Use :code:`ls -l` to view this information.

For example:

:code:`-rw-r--r-- 1 juser somegroup 7041 Mar 26 19:34 endnotes.html`

The mode, the first string, represents the file's permissions and some
extra information.

.. image:: images/fig-2.1.jpg
  :alt: File Modes

The file **type** indicates what this is. :code:`-` indicates a *regular* file.
:code:`d` indicates a directory. There are other types which will come up
later.

The rest of it can be summed up as groups of 3: :code:`[rwx]`, using :code:`-` where
inapplicable. The permission bits indicate what rights the user(s)
in question has. The first set is the owner, the second is the group
members, the third group is everyone else.

Modifying Permissions
=======================

:code:`chmod a+r <file>` will give everyone *read* permissions on the file.

:code:`chmod o+r <file>` will give other users (not owner and not group members)
*read* permissions on the file.

:code:`chmod +rwx <file>` will give the user *all* permissions on the file.

:code:`chmod g+rx <file>` will give the group members *read and execute* permissions on the file.

:code:`chmod g-x <file>` will *remove* *execute* access from group members.

:code:`chmod o-r <file>` will *remove* *read* access from other users.

Although you *can* use numbers to set the direct permissions, this is
much easier to read.


.. image:: images/table-2.4.jpg
  :alt: Table on absolute modes

Symbolic Links
===================

.. warning::

    This is a work in progress.



## Later Reading
1. Operating System Concepts by Abraham Silberschatz et. al.
2. Modern Operating Systems by Andrew S. Tanenbaum et al.
3. The Linux Command Line, No Starch Press
4. UNIX for the Impatient, Addison-Wesley Professional
6. Learning the UNIX Operating System, O'Reilly
7. Mastering Regular Expressions, O'Reilly
8. Programming Perl, O'Reilly
9. Introduction to Automata Theory, Languages, and Computation, O'Reilly.
10. Learning the vi and Vim Editors: Unix Text Processing, O'Reilly
11. GNU Emacs Manual
