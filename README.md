##Caching Mini Project 
###Created as an example for my blog
####Author: Kenneth R Hancock

You can find the post here.  https://medium.com/@ryanhancock/cache-me-if-you-can-d9815c9e2b35#.ze72nduvp

## Tail Recursion version of Fibb

I'd like to make a side note here that a better fibbonacci sequence if needed would be the tail call optimized version
(Stack friendly!)

```python
def fib(n):
  def fib_help(a, b, n):
    return fib_help(b, a+b, n-1) if n > 0 else a
  return fib_help(0, 1, n)
```
