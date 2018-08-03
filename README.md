1) will first explain the purposes and potential uses for this project.
2) will explain how it works.
3) will explain the stupidity of the creator[s] (will you ever know how many? probably not...) because there is likely already some function in some long-forgotten library that does exactly what this does. Anyway...

1) The program defines a function that when given input nonnegative integer n, then will print a polynomial in improper-fraction form that is the simplified version of a summation of the nth powers of all numbers from 1 to x, in terms of x. It will be given in two forms, and written in two different documents and not actually printed, for the sake of efficiency. One will be in a format fit for automatic transferral into a LaTeX compiler. A free one is available that renders a png at http://quicklatex.com/. The other is for the program's reference, thank you very much.

2) The program stores polynomials in this manner. x^3+2x^2+1 would be stored as [1,2,0,1]. com(x,y) is the combination function that finds (x!)/(x-y)!(y)!. For the Binomial Theorem. Anyway. Suppose our input is n. We use recursion:

	We first find the polynomial form for the summation of (x+1)^{n+1}-x^{n+1}. This produces summation of something times x^n plus something times x^{n-1} all the way down to some constant.
		Next we subtract all the other things we don't want from x^{n-1} down- slow and mediocre recursion. So we plan to save our already-computed values to a file that we can call back on.
			Finally, we use division to isolate our brand-new, shiny polynomial, and format it as needed.
				Libraries cited: fractions, numpy, math

3) Nevermind, a little research we did shows that there probably isn't. So there.
