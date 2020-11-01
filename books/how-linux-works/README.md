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


## Later Reading
1. Operating System Concepts by Abraham Silberschatz et. al.
2. Modern Operating Systems by Andrew S. Tanenbaum et al.



