10 Tips for Cleaner Python
===
One of the core ideologies behind the Python language is that people spend more time reading code than writing code, thus, code clarity is of utmost importance.

Below are ten of my favorite improvements I've made on my own code during my time as a novice Pythonista. Some are specific to Python's syntactic sugar, but a few can benefit code structure in other languages.

1) Slice Syntax
----
Python's syntactic sugar at it's finest. Accessing specific slices in an array has never been easier! Using array[begin:end] gives you a slice of everything from **begin** up to, but not including, **end**.

As a bonus, you can optionally include an interval to step through the array using [begin:end:step].
<script src="https://gist.github.com/chr1sbest/1cf748f8724647a1baf4.js"></script>

2) String Formatting
----
String concatenation with + is pretty nifty, but it's easy to forget punctuation, spaces, and +'s when concatenating multiple strings. 

str.format() lets you build a readable format, and uses the \__str\__ representation of all variables passed in as parameters (as opposed to calling str() on every non-string parameter manually).
<script src="https://gist.github.com/chr1sbest/757ed01921fda88f7373.js"></script>

3) Single Line Variable Assignment
----
This isn't that big of a deal in itself, but it's convenient to be able to assign similar variables on the same line. The real bonus in single line variable assignment is in the next tip.
<script src="https://gist.github.com/chr1sbest/75e6caa0e99163037b76.js"></script>

4) Swap
----
Swapping elements typically requires a temporary variable to hold onto one of the elements. With single line variable assignment, we can bypass this.
<script src="https://gist.github.com/chr1sbest/c343d15d394ffad69e8e.js"></script>

5) Enumerate
----
Enumerate is a super useful function if you need access to the index and value of an iterable object.
<script src="https://gist.github.com/chr1sbest/f77122664489e3af1764.js"></script>

6) Zip
----
Zip can be useful when you need to iterate over two lists at the same time.
<script src="https://gist.github.com/chr1sbest/a96392e2eda21d958a13.js"></script>

7) Keyword Arguments
----
Keyword arguments are typically used to supply default arguments to a function, but they give the added benefit of clarity to function calls that take multiple parameters.
<script src="https://gist.github.com/chr1sbest/1a988c30f5198bc951e2.js"></script>

8) Lambdas & List Comprehensions
----
Higher order functions allows for some fancy footwork using functional programming. For example, passing anonymous functions, or lambdas in Python, can let you do things like simplify certain "for loop" iterations to build a list with a single line.

An alternative to using map/filter would be to use the Pythonic **List Comprehension**. For building new lists/tuples/dictionaries, Guido recommends using list comprehensions over map/filter due to it's readability (and very very slight edge in performance).
<script src="https://gist.github.com/chr1sbest/52b1b28f96b9075a770a.js"></script>

9) Switch Object
----
Python does not have Switch/Case for logic handling. Fortunately, the if/elif/else syntax is very clean. However, you can sacrifice a negligible amount of space to build a switch object to save a negligible amount of time (and have better readability and reusability!)
<script src="https://gist.github.com/chr1sbest/cf8eddd9ce78c58eccc7.js"></script>

10) Decorators
----
Python decorators allow you to elegantly wrap a function around a different function. The clever usage of decorators warrants an entire article on it's own, but simple use cases are with memoization and keeping track of the time it takes for a function to execute.
<script src="https://gist.github.com/chr1sbest/7936197828e432dcbfcd.js"></script>

