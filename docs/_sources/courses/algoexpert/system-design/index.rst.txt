.. _algoexpert-system-design:

======================================
Systems Expert
======================================

.. note::
    These are my notes on the Algoexpert Systems Design material.

    I will be keeping my solutions to the problems in the :ref:`systems-design` section,
    since that houses all the systems-design problems I go through.

---------------------------------
Videos
---------------------------------

Design Fundamentals - Introduction
=====================================

This video only introduces the series.

What are Design Fundamentals
==============================

Systems Design interview questions are *intentionally* vague, such as "design
uber", so that the interviewee can convert that into a 45 minute discussion, to
understand how we gather requirements and think about use-cases through
investigation.

These rounds are also very *subjective*, a proposed solution requires a lot of
justification and convincing. It's an exercise in negotiation. The interviewer
will be *assessing* whether you can or cannot convince him.

This requires strong fundamentals.

You need strong knowledge of *foundational design principles*, *key
characteristics*, and the *actual components* that make up the system. You
will then need to translate these into actual *tech*, that you will use
to translate the discussion into a tangible design.

Client-Server Model
=====================

This video discusses how the internet works, at a very basic level.

Recommended reading topics:

1. Clients
1. Servers
1. TCP
1. HTTP Protocol
1. DNS Server
1. IP Address

A client *connects* to a server, requesting for data through an open socket. The server is
listening on a socket, and it responds with the relevant data.

The client knows where a server is through a DNS server. A DNS server has a record
of other servers which correspond to a name such as ``https://google.com``, or
it knows other servers which do. In the beginning of the Internet, there was a massive
file that was shipped around with this information.

.. tip::

    Use ``dig`` to find the IP address of a given server, in a way similar to
    how browsers do this.

Armed with the server's address, the client requests information pertaining to some data,
using the HTTP Protocol. The data that it asks for is determined by the *url route*, and the
kind of data it requests is determined by the request method (GET, POST, PUT, etc).

The *payload*, and the *response* is passed around as *packets*.

.. tip::

    Use ``nc`` to open a port and communicate with that port on your machine.
