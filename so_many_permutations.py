#Solution to Codewars kata: https://www.codewars.com/kata/5254ca2719453dcc0b00027d

def permutations(s):
    return set(''.join(i) for i in perm(s))
