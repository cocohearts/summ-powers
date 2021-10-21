from fractions import Fraction
import math
import numpy as np
"""
Remember:

sum_{n=1}^k (n^c) is what we want to find. Let sum_{n=1}^k (n^c) = P_c(k)
sum_{n=1}^k ((n+1)^{c+1}-n^{c+1}) = (k+1)^{c+1} - 1 = sum_{n=1}^k (sum_{i=0}^c binom(c+1,i)n^i) = sum_{i=0}^c (binom(c+1,i)P_i(k))
"""
"""
#Test
with open("data.txt",'w') as f:
    f.write("[Fraction(0,1),Fraction(1,1)]")
with open("formatted.txt","w") as f:
    f.write("\\[\\sum_{k=1}^xk^0=x\\]")
"""

class Polynomial:
    def __init__(self,coefficients):
        """
        self.coefficients is labeled from 0; self.coefficients[0] is x^0 coefficient
        """
        self.coefficients = coefficients

    def subtract(self,polynomial):
        subtracted = np.array(polynomial.coefficients)
        for r in range(len(self.coefficients) - len(subtracted)):
            subtracted = np.append(subtracted,0)
        self.coefficients -= subtracted

def main(input_polynomials):
    """
    input: list of polynomials, of np arrays
    output: polynomial
    """
    def binom(a,b):
        return int(math.factorial(a)/(math.factorial(b)*math.factorial(a-b)))

    c = len(input_polynomials)
    return_polynomial = [Fraction(0,1)]

    for index in range(1,c+2):
        return_polynomial.append(Fraction(int(binom(c+1,index)),1))

    return_poly = Polynomial(np.array(return_polynomial))

    for k in range(c):
        return_poly.subtract(Polynomial(input_polynomials[k].coefficients * int(binom(c+1,k))))
        #subtracted = input_polynomials[k].coefficients * binom(c+1,k)
        #return_poly.coefficients -= subtracted

    return_poly.coefficients /= c+1

    return return_poly
    
def my_input(degree):
    polynomials = []
    length = 0
    with open("data.txt", 'r') as f:
        for line in f:
            length += 1
    if length - 1 >= degree:
        return None
    with open("data.txt", 'r') as f:
        for line in f:
            if type(eval(line)) == int:
                raise ValueError
            else:
                polynomials.append(Polynomial(np.array(eval(line))))

    return polynomials

def my_output(polynomial):
    with open("data.txt", 'a') as fout:
        fout.write("\n"+str(polynomial))
        #print("\n"+str(polynomial))
        
    with open("formatted.txt", 'a') as fout:
        written = ""
        for index in range(len(polynomial)):
            if polynomial[index] < 0:
                if polynomial[index].numerator == -1:
                    num = ""
                else:
                    num = str(-polynomial[index].numerator)
                written += " - \\frac{" + num + "x^{" + str(index) + "}}{" + str(polynomial[index].denominator) + "}"
            elif polynomial[index] > 0:
                if polynomial[index].numerator == 1:
                    num = ""
                else:
                    num = str(polynomial[index].numerator)
                written += " + \\frac{" + num + "x^{" + str(index) + "}}{" + str(polynomial[index].denominator) + "}"
        fout.write("\n\\[\\sum_{k=1}^x k^{" + str(len(polynomial)-2) + "}=" + written[2:]+"\\]")


for degree in range(int(input)):
    polynomials = my_input(degree)
    if polynomials:
        my_output(list(main(polynomials).coefficients))
