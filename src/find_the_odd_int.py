�
h�Yc           @   s   d  Z  d �  Z d S(   s�   Kata: Find the Odd Integer - Need to find the one odd numbered integer in a list.

#1 Best Practices Solution by cerealdinner et al.

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return ic         C   sm   i  } x7 |  D]/ } | | k r2 | | c d 7<q d | | <q Wx& | D] } | | d d k rG | SqG Wd S(   s^   function finds the integer that has the odd number of values once collected into a dictionary.i   i   i    N(    (   t   seqt   countert   item(    (    sF   /Users/marcozangari/codefellows/401/code-katas/src/find_the_odd_int.pyt   find_it
   s    N(   t   __doc__R   (    (    (    sF   /Users/marcozangari/codefellows/401/code-katas/src/find_the_odd_int.pyt   <module>   s   