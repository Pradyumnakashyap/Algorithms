#Lilah has a string,s, of lowercase English letters that she repeated infinitely many times.
#Given an integer,n, find and print the number of letter a's in the first n letters of Lilah's infinite string.
#For example, if the string s='abcac' and n=10 , the substring we consider is abcacabcac, the first 10 characters of her infinite string. There are 4 occurrences of a in the substring.

s = 'a'
n = 10000000000

# "a" count of full string * number of string repeats + "a" count of last string

print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))