# Assignment 1. Distributed Systems and Nentwork Programming

DigiJED Course: Introduction to the concepts of distributed systems and communication between remote processes, distributed architectures, and distributed file systems. TCP and UDP socket programming and implementation of network applications in Python.

## Task #1

Write a program in Python that will load two numbers (n and m) provided via input by the user, that indicate the sides of a rectangle, and then as output print the largest square, in the form a\*a, with even side length contained in the provided rectangle.

## Task #2

Write a program in Python that will ask the user to provide names of two cities and the distance between them. This information should be placed in a dictionary of dictionaries. A dictionary will contain a city name as an item key and a new dictionary as an item value. Each of these nested dictionaries will contain pairs of city name (key) and location (value). This distance indicates the distance between the city in the second dictionary and the city in the first dictionary.

## Task #3

Create a module in Python with a function definition that will check if a certain IP address belongs to the appropriate network. When starting the module, check if the specified IP addresses belongs to the appropriate network:

- 193.10.10.1 to 193.10.10.0/29
- 193.10.10.9 to 193.10.10.0/29
- 194.20.20.5 to 194.20.20.0/29
- 194.20.20.5 to 194.20.20.0/30.

## Task #4

Create a Python module called mixed_cipher. In this assignment, we’ll be implementing a small program which takes in a filename as a command-line argument and then performs simple substitution on the file contents with a mixed alphabet. A mixed alphabet can be created by prompting the user for the keyword, removing repeated letters in the keyword, and then writing the remaining letters of the alphabet in the usual order. For example, if my keyword is “computer”, then I have the following:

Plaintext: ABCDEFGHIJKLMNOPQRSTUVWXYZ

Ciphertext: COMPUTERABDFGHIJKLNQSVWXYZ

Your program should output the encrypted text to the screen. Here’s an example execution. Let’s say I have a file called test.txt which has the following contents:

This is a file. This file has some WORDS in it.

A sample run of mixed cipher.py with this test file would produce the following output. Note that capitalization and punctuation are kept as-is in the encrypted text.

$ python mixed_cipher.py test.txt

Please enter a keyword for the mixed cipher: Motherboard Plaintext: abcdefghijklmnopqrstuvwxyz

Cipherte: motherbadcfgijklnpqsuvwxyz

Sadq dq m rdge. Sadq rdge amq qkie WKPHQ dj ds.
