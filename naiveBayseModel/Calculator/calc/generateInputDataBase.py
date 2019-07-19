import math
import numpy as np

# Criando inputs:
powers_of_2 = [ index**2 for index in range(1,101) if  index**2<100 and  index**2>0]
powers_of_3 = [ index**3 for index in range(1,101) if  index**3<100 and  index**3>0]
powers_of_4 = [ index**4 for index in range(1,101) if  index**4<100 and  index**4>0]
powers_of_5 = [ index**5 for index in range(1,101) if  index**5<100 and  index**5>0]
powers_of_6 = [ index**6 for index in range(1,101) if  index**6<100 and  index**6>0]
powers_of_7 = [ index**7 for index in range(1,101) if  index**7<100 and  index**7>0]
powers_of_8 = [ index**8 for index in range(1,101) if  index**8<100 and  index**8>0]
powers_of_9 = [ index**9 for index in range(1,101) if  index**9<100 and  index**9>0]
powers_of_10 = [ index**10 for index in range(1,101) if  index**10<100 and  index**10>0]

even =  [ 2*index for index in range(1,101) if  2*index<100 and  2*index>0]
odd =  [ 2*index-1 for index in range(1,101) if  2*index-1<100 and  2*index-1>0]

factorial = [ math.factorial(index) for index in range(1,101) if  math.factorial(index)<100 and  math.factorial(index)>0]
ends_in_0 = [ (index)*10 + 0 for index in range(1,101) if  (index)*10 + 0<100 and  (index)*10 + 0>0]
ends_in_1 = [ (index-1)*10 + 1 for index in range(1,101) if  (index-1)*10 + 1<100 and  (index-1)*10 + 1>0]
ends_in_2 = [ (index-1)*10 + 2 for index in range(1,101) if  (index-1)*10 + 2<100 and  (index-1)*10 + 2>0]
ends_in_3 = [ (index-1)*10 + 3 for index in range(1,101) if  (index-1)*10 + 3<100 and  (index-1)*10 + 3>0]
ends_in_4 = [ (index-1)*10 + 4 for index in range(1,101) if  (index-1)*10 + 4<100 and  (index-1)*10 + 4>0]
ends_in_5 = [ (index-1)*10 + 5 for index in range(1,101) if  (index-1)*10 + 5<100 and  (index-1)*10 + 5>0]
ends_in_6 = [ (index-1)*10 + 6 for index in range(1,101) if  (index-1)*10 + 6<100 and  (index-1)*10 + 6>0]
ends_in_7 = [ (index-1)*10 + 7 for index in range(1,101) if  (index-1)*10 + 7<100 and  (index-1)*10 + 7>0]
ends_in_8 = [ (index-1)*10 + 8 for index in range(1,101) if  (index-1)*10 + 8<100 and  (index-1)*10 + 8>0]
ends_in_9 = [ (index-1)*10 + 9 for index in range(1,101) if  (index-1)*10 + 9<100 and  (index-1)*10 + 9>0]

multiples_of_3 = [ index*3 for index in range(1,101) if  index*3<100 and  index*3>0]
multiples_of_4 = [ index*4 for index in range(1,101) if  index*4<100 and  index*4>0]
multiples_of_5 = [ index*5 for index in range(1,101) if  index*5<100 and  index*5>0]
multiples_of_6 = [ index*6 for index in range(1,101) if  index*6<100 and  index*6>0]
multiples_of_7 = [ index*7 for index in range(1,101) if  index*7<100 and  index*7>0]
multiples_of_8 = [ index*8 for index in range(1,101) if  index*8<100 and  index*8>0]
multiples_of_9 = [ index*9 for index in range(1,101) if  index*9<100 and  index*9>0]

powers_of_2 = [ 2**index for index in range(1,101) if  2**index<100 and  2**index>0]
powers_of_3 = [ 3**index for index in range(1,101) if  3**index<100 and  3**index>0]
powers_of_4 = [ 4**index for index in range(1,101) if  4**index<100 and  4**index>0]

pi = [3,1,4,1,5,9,2,6,5,2,5,8,9,7,9,3,2,3,8,4,6,2,6]
fibonati = [1,1,2,3,5,8,13,21,34,55,89]
primes = [1,2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# transformando sets para o formato table:
powers_of_2 =[powers_of_2.count(i)/len(powers_of_2) for i in range(101)]
powers_of_3 =[powers_of_3.count(i)/len(powers_of_3) for i in range(101)]
powers_of_4 =[powers_of_4.count(i)/len(powers_of_4) for i in range(101)]
powers_of_5 =[powers_of_5.count(i)/len(powers_of_5) for i in range(101)]
powers_of_6 =[powers_of_6.count(i)/len(powers_of_6) for i in range(101)]
powers_of_7 =[powers_of_7.count(i)/len(powers_of_7) for i in range(101)]
powers_of_8 =[powers_of_8.count(i)/len(powers_of_8) for i in range(101)]
powers_of_9 =[powers_of_9.count(i)/len(powers_of_9) for i in range(101)]
powers_of_10 =[powers_of_10.count(i)/len(powers_of_10) for i in range(101)]
even =[even.count(i)/len(even) for i in range(101)]
odd =[odd.count(i)/len(odd) for i in range(101)]
factorial =[factorial.count(i)/len(factorial) for i in range(101)]
ends_in_0 =[ends_in_0.count(i)/len(ends_in_0) for i in range(101)]
ends_in_1 =[ends_in_1.count(i)/len(ends_in_1) for i in range(101)]
ends_in_2 =[ends_in_2.count(i)/len(ends_in_2) for i in range(101)]
ends_in_3 =[ends_in_3.count(i)/len(ends_in_3) for i in range(101)]
ends_in_4 =[ends_in_4.count(i)/len(ends_in_4) for i in range(101)]
ends_in_5 =[ends_in_5.count(i)/len(ends_in_5) for i in range(101)]
ends_in_6 =[ends_in_6.count(i)/len(ends_in_6) for i in range(101)]
ends_in_7 =[ends_in_7.count(i)/len(ends_in_7) for i in range(101)]
ends_in_8 =[ends_in_8.count(i)/len(ends_in_8) for i in range(101)]
ends_in_9 =[ends_in_9.count(i)/len(ends_in_9) for i in range(101)]
multiples_of_3 =[multiples_of_3.count(i)/len(multiples_of_3) for i in range(101)]
multiples_of_4 =[multiples_of_4.count(i)/len(multiples_of_4) for i in range(101)]
multiples_of_5 =[multiples_of_5.count(i)/len(multiples_of_5) for i in range(101)]
multiples_of_6 =[multiples_of_6.count(i)/len(multiples_of_6) for i in range(101)]
multiples_of_7 =[multiples_of_7.count(i)/len(multiples_of_7) for i in range(101)]
multiples_of_8 =[multiples_of_8.count(i)/len(multiples_of_8) for i in range(101)]
multiples_of_9 =[multiples_of_9.count(i)/len(multiples_of_9) for i in range(101)]
pi =[pi.count(i)/len(pi) for i in range(101)]
fibonati =[fibonati.count(i)/len(fibonati) for i in range(101)]
primes =[primes.count(i)/len(primes) for i in range(101)]

# criando objetos
h = Hypoteses(name = "set of powers of 2 integers",prior = 0.1, table = str(powers_of_2))
h.save()

h = Hypoteses(name = "set of powers of 3 integers",prior = 0.01, table = str(powers_of_3))
h.save()

h = Hypoteses(name = "set of powers of 4 integers",prior = 0.01, table = str(powers_of_4))
h.save()

h = Hypoteses(name = "set of powers of 5 integers",prior = 0.01, table = str(powers_of_5))
h.save()

h = Hypoteses(name = "set of powers of 6 integers",prior = 0.01, table = str(powers_of_6))
h.save()

h = Hypoteses(name = "set of powers of 7 integers",prior = 0.01, table = str(powers_of_7))
h.save()

h = Hypoteses(name = "set of powers of 8 integers",prior = 0.01, table = str(powers_of_8))
h.save()

h = Hypoteses(name = "set of powers of 9 integers",prior = 0.01, table = str(powers_of_9))
h.save()

h = Hypoteses(name = "set of powers of 10 integers",prior = 0.01, table = str(powers_of_10))
h.save()

h = Hypoteses(name = "set of even integers",prior = 0.5, table = str(even))
h.save()

h = Hypoteses(name = "set of odd integers",prior = 0.5, table = str(odd))
h.save()

h = Hypoteses(name = "set of factorial integers",prior = 0.1, table = str(factorial))
h.save()

h = Hypoteses(name = "set of ends in 0 integers",prior = 0.1, table = str(ends_in_0))
h.save()

h = Hypoteses(name = "set of ends in 1 integers",prior = 0.1, table = str(ends_in_1))
h.save()

h = Hypoteses(name = "set of ends in 2 integers",prior = 0.1, table = str(ends_in_2))
h.save()

h = Hypoteses(name = "set of ends in 3 integers",prior = 0.1, table = str(ends_in_3))
h.save()

h = Hypoteses(name = "set of ends in 4 integers",prior = 0.1, table = str(ends_in_4))
h.save()

h = Hypoteses(name = "set of ends in 5 integers",prior = 0.1, table = str(ends_in_5))
h.save()

h = Hypoteses(name = "set of ends in 6 integers",prior = 0.1, table = str(ends_in_6))
h.save()

h = Hypoteses(name = "set of ends in 7 integers",prior = 0.1, table = str(ends_in_7))
h.save()

h = Hypoteses(name = "set of ends in 8 integers",prior = 0.1, table = str(ends_in_8))
h.save()

h = Hypoteses(name = "set of ends in 9 integers",prior = 0.1, table = str(ends_in_9))
h.save()

h = Hypoteses(name = "set of multiples of 3 integers",prior = 0.1, table = str(multiples_of_3))
h.save()

h = Hypoteses(name = "set of multiples of 4 integers",prior = 0.1, table = str(multiples_of_4))
h.save()

h = Hypoteses(name = "set of multiples of 5 integers",prior = 0.1, table = str(multiples_of_5))
h.save()

h = Hypoteses(name = "set of multiples of 6 integers",prior = 0.1, table = str(multiples_of_6))
h.save()

h = Hypoteses(name = "set of multiples of 7 integers",prior = 0.1, table = str(multiples_of_7))
h.save()

h = Hypoteses(name = "set of multiples of 8 integers",prior = 0.1, table = str(multiples_of_8))
h.save()

h = Hypoteses(name = "set of multiples of 9 integers",prior = 0.1, table = str(multiples_of_9))
h.save()

h = Hypoteses(name = "set of algorithms pi integers",prior = 0.1, table = str(pi))
h.save()

h = Hypoteses(name = "set of fibonati",prior = 0.1, table = str(fibonati))
h.save()

h = Hypoteses(name = "set of primes",prior = 0.1, table = str(primes))
h.save()



