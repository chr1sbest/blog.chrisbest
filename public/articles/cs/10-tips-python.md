#10 Tips for Cleaner Python

1) Slice Syntax
----
Python's syntactic sugar at it's finest. Accessing specific slices in an array has never been easier! Using array[begin:end] gives you a slice of everything from **begin** up to, but not including, **end**.

As a bonus, you can optionally include an interval to step through the array using [begin:end:step].

2) String Formatting
----
String concatenation with + is pretty nifty, but it's easy to forget punctuation, spaces, and +'s when concatenating multiple strings. 

str.format() lets you build a readable format, and uses the \__str\__ representation of all variables passed in as parameters (as opposed to calling str() on every non-string parameter manually).

3) Single Line Variable Assignment
----
This isn't that big of a deal in itself, but it's convenient to be able to declare similar variables on the same line. The real bonus in single line variable declaration is in the next tip.

4) Swap
----
Swapping elements typically requires a temporary variable to hold onto one of the elements. With single line variable assignment, we can bypass this.

5) Enumerate
----
Enumerate is a super useful function if you need access to the index and value of an iterable object.

6) Zip
----
Zip can be useful when you need to iterate over two lists at the same time.

7) Keyword Arguments
----
Keyword arguments are typically used to supply default arguments to a function, but they give the added benefit of clarity to function calls that take multiple parameters.

8) Lambdas & List Comprehensions
----
Higher order functions allows for some fancy footwork using functional programming. For example, passing anonymous functions, or lambdas in Python, can let you do things like simplify certain "for loop" iterations to build a list with a single line.

An alternative to using map/filter would be to use the Pythonic **List Comprehension**. For building new lists/tuples/dictionaries, Guido recommends using list comprehensions over map/filter due to it's readability (and very very slight edge in performance).

9) Switch Object
----
Python does not have Switch/Case for logic handling. Fortunately, the if/elif/else syntax is very clean. However, you can sacrifice a negligible amount of space to build a switch object to save a negligible amount of time (and have better readability and reusability!)

10) XOR
----
If you have two conditions in an if statement and want to run specific logic if one is True while the other is False (but don't care which is which), this handy XOR hack can simplify things. 
