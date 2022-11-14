Coding Test
===========

Approximate time allowed: 1 hour

You will write a function that takes as arguments a file path specifying a source text
and a search term. The function should search the source text for matches of the search term, 
and return a string with all the matches in the format defined below.

Feel free to write unit tests as you go along or at the end, whichever you prefer.

Source text
-----------
The source text consists of lines of strings, with each line containing three words embedded in symbols,
numbers and spaces.

For example the line  
`this is one`  
contains the words: `this` , `is` and `one`. And the line:  
`908^)-234 923this-++-23is./<.";][}"another-=&^5`  
contains the words: `this` , `is` and `another`  

Search term
-----------
The search term is always on the last line of the file, and contains a single word.

Match
-----
A line from the source text is considered a match if any word on the line contains the search 
term as a substring.

For example the line  
`this is one`  
would match the search terms `this`, `is`, `one`, `his`, `on`, `s` amongst many others, but would not 
match the search terms `siht`, `b`, `iso`, `thisisone` amongst many, many others.

Output
------
You are expected to output the words on a matching line formatted as single space separated
square-bracket-enclosed lists. 

Example:  
`[this is ok]`  
is correct, but all of:  
`[this, no, good]`  
`{this no good}`  
`[this,no,good]`  
`[this  no  good]` (multiple spaces)  
are not correctly formatted.

If there are multiple lines that match, you should output them in the order they 
appear in the source text.

Examples
--------
The following examples are also provided as potential test cases.

### Example 1

Given the input file:
```
cat sees me
mary likes trees
up the hill
ee
```
Your program should output:
```
[cat sees me]
[mary likes trees]
```

### Example 2

Given the input file:
```
"Alice was beginning...
to_get9_!very
1111tired1111of1111sitting1111
by her_sister.
on9the bank,
and""of""having
nothing to do!!!
er
```
Your program should output:
```
[to get very]
[by her sister]
```


Solution delivery
-----------------

We will start by working on the core functionality and if there is time we'll add features towards
release to production - unit tests, support for very large files, turning the function into a 
standalone program, documentation, etc.
