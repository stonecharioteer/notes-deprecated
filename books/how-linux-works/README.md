# How Linux works

Author: Brian Ward
Timeline: 2020-10-25 till date.

## Objective

I have been using Linux since 2007, but I have not dived into
the depths of the topic. I would like in-depth Linux Kernel
knowledge, so that I can both appreciate the system better
and be a more powerful developer.

However, I would like objectifiable goals:

1. Be able to analyse system performance.
2. Be able to compile kernels from source and boot them.
3. Be able to edit the grub bootloader config.
4. Be able to debug a running process using syslogs.
 
The fact that I do not yet know what I would like to do is
proof that I lack definitive knowledge of the system.

## Chapter 1 The Big Picture

The Linux Kernel provides libraries and interfaces with which
programs can interact with devices. Although, as this book
details later, what the Kernel considers to be devices is
quite interesting.

### Process Management

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

### Memory Management

The Commandments for Memory Management

1. The Kernel Keepeth its own private, inaccessible memory space.
2. Unto each process is its own section of memory.
3. Thou shalt not covet thy neighbour's memory space.
4. If thou chooseth, some sections of thine memory may not be altered.
5. The System may useth the disks as though they were like unto memory, should it need to.

### Device Drivers and Management

A device is typically accessible only in Kernel mode, so as to prevent
improper access.

So can I think of *kernel mode* as what the CPU does inbetween
time slices so that it can execute kernel commands? Like when a
process asks to access a disk, the kernel has to respond during
the context switching?

### System Calls and Support

System calls (`syscalls`) perform specific tasks that a user process
alone cannot do well or at all. Opening files, reading or writing to
files, all qualify.

`fork` and `exec` are very important.

`fork` instructs the kernel to create a nearly identical copy of the process.

`exec` instructs the kernel to start a `program` that is passed to
`exec` and replace the current process.

*All* user processes, except `init` start through `fork`. You run `exec`
to start a new program instead of running a copy of an existing
process.

Interestingly, this must be how virtualenvs cannot be sourced within
a shell script. Trying: `ls` in a terminal, the shell calls `fork` to
create copy of the current shell, start this, and then exit.

### User Space

The user-space or `userland` is main memory that the kernel allocates
for user processes.

### Users

A user is an entity that can run processes and own files. A user is
associated with a username, but the kernel uses userids to identify
a user. User space processes are owned by a user, and processes
are run as a user.

`root` is a privileged user which can terminate any other user's
processes and read/write any file on the file system.

`root` might be powerful, but it *still runs in User mode, not kernel
mode*.

Groups are sets of users.

## Basic Commands and Directory Heirarchy

### The Bourne Shell `/bin/sh`

A shell is a program that runs commands. The Bourne Shell, was
developed at Bell Labs. Linux uses the *Bourne-Again shell*,
commonly known as `bash`.

Use `chsh` to change the default shell on a Linux system.

### Using the Shell

`echo` does not need quotes.

`cat` performs concatenations on a list of files or input streams.

#### Standard Input and Standard Output

Unix processes use I/O streams to read and write data. Streams are
very flexible: their source can be a file, a device, a terminal,
or even the output stream from another process.

Using `cat` without an argument puts you into `STDIN` mode, where
`cat` will echo back everything you type into it. When you type,
you are sending inputs to `STDIN`. `cat` reads this and redirects
it to `STDOUT`. (Use CTRL-D to exit).

`CTRL-D` stops `STDIN` input on a terminal, and depending on the
program, terminates it. `CTRL-C` terminates a program, irrespective
of the input or output.

Each process gets an `STDOUT` stream to write to. `cat` writes to
`STDOUT`.

`STDERR` is covered later.

Both these can be *redirected*.

### Basic Commands

Covers standard commands you should already know: 
`ls, cp, mv, touch, rm & echo`.

### Navigating Directories

Unix directory hierarchy begins at `/`, called the root dir.
`.` refers to the current diredctory. Paths can be *absolute*
(`/usr/lib`) or *relative* (`code/file1.txt` or `./code/file1.txt`).

Covers `cd, mkdir` and `rmdir`.

The shell natively supports *simple* patterns, or *globs*.
Globs are *expanded before* running the commands.

`*` (match anything, any length), and `?` (match anything, 1 character)
  are the most noteworthy in the beginning.

### Intermediate Commands

Use `grep` to find a string within a directory. Note: *ripgrep* (`rg`)
and *the_silver_searcher* (`ag`) are *much, much faster.*

`grep <find what> <find where>`

Note: If you use shell expansions (globbing) in the `<find what>`
section, these are *expanded first*, and might not be what you want.

`less` provides a scrolling view on `stdout`. `less` is `more`, enhanced.

`less` supports the `/` search mechanism that `vim` uses.

`pwd` prints the current working directory. Use `pwd -P` to resolve
symbolic links as well.

`diff` is used to spot the differences between 2 files.
`diff -u` provides a way for other programs to analyse the output.

`file` can be used to guess the *file type* of a given file.

`find <directory> -name <filename> -print` can be used to find a
certain file in a directory tree. Remember, if you must use `*`,
enclose it in `''` quotes. `find <directory> -iname <filename>`
will turn off case-sensitivity.

`locate` uses a cached file index for a file, and is faster
for this reason. However, if the file is newer than the index,
`locate` won't find it.

`head` and `tail` return the top and bottom `n` lines of a stream
respectively. `head -<n>` will show `<n>` number of lines.
`tail +<n>` will print everything from line number `<n>`.

### Changing Your Password and Shell

`passwd` can change the password, and `chsh` can change the default
shell.

### Dot Files

Files beginning with a `.` are *configuration* files.
Linux programs use text based files for configuration.

### Environment and Shell Variables

`STUFF=blah` is how you assign a value to a variable in the shell.
*Note the absence of spaces around the `=`*. A shell variable is
local to the current process. However, an environment variable is
passed to processes spawned by this process as well.

Note that *all* environment variables are passed to child processes.


#### Child Processes and Inherited Environments

This creates interesting problems, such as needing to start a Python2
process from a Python3 environment. If you activate a virtualenv
and use `subprocess.check_output` to run `python`, the default Python
will be the same as the parent process (Python 3 here). If you
have a weird use case where you would want to do this, ensure you *don't*
source the *virtualenv*, instead, run the parent python script
using the *absolute path* to the virtual environment's python
executable (found in `<envdir>/bin/python`). Again, note that
this is not the Python executable that was used to make the virtualenv.


### The Command Path

`PATH` is a very important Environment variable. It contains a `:`
separated list of directories where the current shell will search
for commands.

This is an interesting scenario. Carefully, try `export PATH=`,
to clear the value of `PATH`. Now try running commands you've learnt
so far. If they execute, these are native unix commands. If they do not,
these are binaries that were possibly available in some of the library
folders such as `/usr/bin`, `/usr/local/bin` or `/bin`.

When appending to the path, use `export PATH=$PATH:<dir>`.


## Later Reading
1. Operating System Concepts by Abraham Silberschatz et. al.
2. Modern Operating Systems by Andrew S. Tanenbaum et al.
3. The Linux Command Line, No Starch Press
4. UNIX for the Impatient, Addison-Wesley Professional
6. Learning the UNIX Operating System, O'Reilly
7. Mastering Regular Expressions, O'Reilly
8. Programming Perl, O'Reilly
9. Introduction to Automata Theory, Languages, and Computation, O'Reilly.

