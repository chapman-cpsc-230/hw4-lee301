# Instructions

This assignement is due on Friday March 19 at 8:00AM. I will start grading on Friday morning. I suggest you plan to submit the work no later than Thursday evening.

## This Assignment

### From the text

From the text, do the following exercises:

* 3.23 -- you submit a file named `Heaviside.py`.
* 3.24 -- you submit a fle named `smoothed_Heaviside.py`

* 3.35 -- you submit a file named `count_pairs.py`

* 3.28 and 3.29 -- you do not need to submit anything, but these are valuable exercises for test prep.

### Histograms

Define `histogram()`, a procedure that takes a list of positive integers and prints a histogram. For example, `histogram([4, 9, 13, 5])` should print the following:

```
****
*********
*************
*****
```

### Length of an integer

Define a function `digits(n)` that calculates the number of digits (plus the sign for negative numbers) in an integer. For example `digits(521)` should return `3`; `digits(-4530)` should return `5`.

### Enhanced histogram

Using the `digits(n)` function you have written to improve the histogram procedure to print a title and the number of asterisks in each row. For example, `histogram("Data", [4, 9, 13, 5])` should print the following:

```
 n  | Data
---+------------------
 4 | ****
 9 | *********
13 | *************
 5 | *****
```
name files as: histogram.py, digits.py, histogram2.py

## General


* Edit the README.md file:
    * Change _\<your name\>_ and _\<date\>_ at the beginning of the file
    * Reread the __Honor Pledge__ again and 'sign' it with your name at the end
    * Add your own text in the __Description__ and __What I Learned__ sections

* Correctly document each source file
    * At the top of each source file (```.py``` file), include a docstring in te following format

    ```
    """
    File: <filename>

    Copyright (c) 2016 <your name>

    License: MIT

    <brief description of the code>
    """    
    ```
