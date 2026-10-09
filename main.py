import numpy as np
import matplotlib . pyplot as plt
def f ( x ) :
return x **6 - x - 1
def g ( x ) :
return 1 - 0.25 * np . cos ( x )
def k ( x ) :
return np . cos ( x ) - np . exp ( - x )
def h ( x ) :
return x **4 - 56.101* x **3 + 785.6561* x **2 - 72.7856* x + 0.078
def tracerFunction ( fn , a , b , fnName , i , x1 ) :
x = np . linspace (a , b , 1000)
y = fn ( x )
plt . subplot (2 , 2 , i )
plt . plot (x , y , "b-")
if isinstance ( x1 , np . ndarray ) and len ( x1 ) > 0 :
y1 = fn ( x1 )
plt . scatter ( x1 , y1 , color ="red")
plt . axhline ( y =0 , color ="k", linestyle ="-", alpha =0.3)
plt . grid ( True )
plt . title ( f"{ fnName }")
plt . figure ( figsize =(10 , 6) )
x1_f = np . array ([ -0.75 , 1.141])
x1_k = np . linspace (0 , 4 , 10)
x1_h = np . array ([ 0.1 , 30]) # Estimation des racines pour h
tracerFunction (f , -2 , 2 , "f(x)=x^6 -x -1", 1 , x1_f )
tracerFunction (g , -10 , 10 , "g(x) =1 -0.25* cos (x)", 2 , np . array ([]) )
tracerFunction (k , -5 , 5 , "k(x)=cos (x)-e^( -x)", 3 , x1_k )
tracerFunction (h , -1 , 50 , "h(x)=x ^4 -56.101 x^3+ ␣... ", 4 , x1_h )
plt . tight_layout ()
plt . show ()
