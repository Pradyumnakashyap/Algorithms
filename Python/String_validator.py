#In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
#In the second line, print True if S has any alphabetical characters. Otherwise, print False.
#In the third line, print True if S has any digits. Otherwise, print False.
#In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
#In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    s = input()
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(eval("c." + test + "()") for c in s))