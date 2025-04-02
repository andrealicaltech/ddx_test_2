# Instructions
In this assignment, you'll be writing a "symbolic differentiator".  In the first hw, you implemented an approximation of a derivative (and integral) using **numerical methods**.  This time, we'll manipulate functions as *strings* which is both weird and wonderful!

# Writing d/dx
In this part of the hw, you'll be helping finish the `ddx()` function that we've started for you in `main.py`.

Both the **arguments** and the **return** values of `ddx` are going to be strings.  For example, we should get the following results:
- `ddx("5") = "0"`
- `ddx("1") = "0"`
- `ddx("x") = "1"`

These examples correspond to the following derivative rules in math notation:
- $\displaystyle\frac{\mathrm{d}}{\mathrm{d} x} \left(\vphantom{\frac{x}{y}}x\right) = 1$
- $\displaystyle\frac{\mathrm{d}}{\mathrm{d} x}\left(\vphantom{\frac{x}{y}}c\right) = 0$

And we can translate these rules into code that looks like the following:

```python
if is_x(f):
    return "1"
```

```python
elif is_number(f) or not has_x(f):
    return "0"
```



## Remaining Derivative Rules
We've already implemented the two cases above for you in the `ddx` function in `main.py`.  Your first task is to implement a bunch of other common derivative rules as follows:

### Addition Rule
Recall the addition rule below.  Then, implement this case in the `ddx` code.

$\displaystyle\frac{\mathrm{d}}{\mathrm{d} x}\left(\vphantom{\frac{x}{y}}u + v\right) = \frac{\mathrm{d} u}{\mathrm{d} x} + \frac{\mathrm{d} v}{\mathrm{d} x}$

An example run of the code using the three cases so far might look like the following:

`ddx("5" + "x") => ddx("5") + ddx("x") => "0 + 1" > "1"`

### Subtraction Rule
Recall the similar subtraction rule below.  Then, implement this case in the `ddx` code.

$\displaystyle\frac{\mathrm{d}}{\mathrm{d} x}\left(\vphantom{\frac{x}{y}}u - v\right) = \frac{\mathrm{d} u}{\mathrm{d} x} - \frac{\mathrm{d} v}{\mathrm{d} x}$

### Multiplication Rule
Recall the similar multiplication rule below.  Then, implement this case in the `ddx` code.

$\displaystyle\frac{\mathrm{d}}{\mathrm{d} x}\left(\vphantom{\frac{x}{y}}u \times v\right) =u \times\frac{\mathrm{d} v}{\mathrm{d} x} + v\times \frac{\mathrm{d} u}{\mathrm{d} x}$

### Division Rule
Recall the similar division rule below.  Then, implement this case in the `ddx` code.

$\displaystyle\frac{\mathrm{d}}{\mathrm{d} x}\left(\vphantom{\frac{x}{y}}\frac{u}{v}\right)=\frac{\mathrm{d}}{\mathrm{d} x}\left(\vphantom{\frac{x}{y}}u \times v^{-1}\right)$

### Power Rule
Recall the similar power rule below.  Then, implement this case in the `ddx` code.

$\displaystyle\frac{\mathrm{d}}{\mathrm{d} x} \left(\vphantom{\frac{x}{y}} x^{n}\right) = n \times x^{n-1}$

### Chain Rule???
For fun, if you have time, try to implement the chain rule!

## Writing `taylor`
Implement the `taylor` function (which represents a taylor series for `f` which goes out to `N` terms, centered around `A`) according to the formula below:

$$\text{taylor}(f, N, A) = \displaystyle\sum_{n=0}^N \frac{\left[{\left(\frac{\mathrm{d}^n}{\mathrm{d}x^n}f(A)\right) \times (x - A)^n}\right]}{\text{factorial}(n)}$$
