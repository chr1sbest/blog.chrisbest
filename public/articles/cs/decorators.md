Python @decorators and why you should use them!
===
The **Decorator Pattern** in Object Oriented programming is defined as *a design pattern that allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.*

@decorators in Python are essentially an implementation of this pattern with a little extra syntactic elegance. Before getting mixed up with the idea of "objects" referring to instances of a class, it's important to note that functions in Python are actually objects as well! This article will hopefully serve as an introduction to **modifying the behaviors of existing functions while reducing code complexity by writing reusable @decorators.**

Let's start with basics. Imagine we have a few functions that do some arbitrary math calculations.

<script src="https://gist.github.com/chr1sbest/1a42d6c2168d3218d951.js"></script>

In this example, we have one function that takes **(1)** argument and multiplies a number by 1.1 a million times. Our second function takes **(2)** arguments and divides a number by another number a million times. Arbitrary? Yes. But let's pretend they're mission critical and the success of our business depends on finding out which function runs faster!

One way to determine the time it takes for a function to run would be to find the time delta. We can do this by declaring the start time before running the function, declaring the stop time after the function runs, and then subtracting the start time from the stop time. Python's time library will help us with this.

<script src="https://gist.github.com/chr1sbest/4d6852b7908e638ac56d.js"></script>

So it looks like we can either alter every function we've written to print out time details, or we can write new wrapper functions altogether for each function we want time details on. Surely there isn't a way to stay DRY without rewriting our functions.

Let's destroy this straw man with a @decorator. This is how our timed functions will look @decorated.

<script src="https://gist.github.com/chr1sbest/22927340698cedfcebc8.js"></script>

Here is our basic implementation of the @decorator with explanations below.

<script src="https://gist.github.com/chr1sbest/53923e83b849c3c96b9a.js"></script>

The parameters passed into the decorator and wrapped can be a little confusing.

* **func** - Remember, functions are treated as objects too! This argument is the decorated function.

* ***args** - This is a positional array of all non-keyword arguments passed to the decorated function.

* ****kwargs** This a dictionary of {keyword arguments: values} passed to the decorated function.

The time_decorator function is going to define a new function called "wrapped", run the timing code we want inside of it along with the function, and then return this new "wrapped" function. Using \*args and **kwargs allows us to handle a variable amount of positional arguments and any kwargs a function might use. All we have to do is attach @time_decorator on top of any function we want to decorate, and voila!

One last thing to throw on. For the third time, functions are objects! While our decorated function will return the correct value, it's actually returning the new function that returns the correct value. What does this mean? All the attributes on your decorated function are going to be overwritten by this new "wrapper" function -- attributes like the \_\_doc\_\_, \_\_name\_\_, etc.

Here is a simple function, functools.wraps, that you can use to make sure the attributes of your decorated function don't get overwritten by it's wrapper! This handy function is also implemented as a @decorator :D

<script src="https://gist.github.com/chr1sbest/03c0462f54e32c7daf39.js"></script>
