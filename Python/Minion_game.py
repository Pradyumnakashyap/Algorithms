#Kevin and Stuart want to play the 'The Minion Game'.
#Game Rules
#Both players are given the same string, S.
#Both players have to make substrings using the letters of the string S.
#Stuart has to make words starting with consonants.
#Kevin has to make words starting with vowels.
#The game ends when both players have made all possible substrings.
#Scoring
#A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

#Explanation : It's an implicit (and smart) count of occurrence.

# Es.

# BANANA (for kevin):
# For i=1 we are sure that there is an occurrence for all this substrings that start with a vowel (s[i] = 'A'):
# - A
# - AN
# - ANA
# - ANAN
# - ANANA
# So we add len(s)-i = 6-1 = 5 to kevin score. 
# For i=3:
# - A
# - AN
# - ANA
# (+3)
# For i=5:
# - A
# (+1)



def minion_game(string):
    # your code goes here
    stuart, kevin, ln, v= 0, 0, len(s), 'AEIOU'
    for i in range(ln):  
        if s[i] in v:
            kevin += ln - i
        else:
            stuart += ln - i
        
    if stuart > kevin:
        print('Stuart ', stuart)
    elif stuart == kevin:
        print('Draw')
    else:
        print('Kevin ', kevin)
    

if __name__ == '__main__':
    s = input()
    minion_game(s)