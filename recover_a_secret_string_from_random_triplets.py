#Solution to Codewars kata https://www.codewars.com/kata/53f40dff5f9d31b813000774 

def recoverSecret(trips):
    s = [True] + list(set([l for t in trips for l in t]))
    while s[0]:
        s[0] = False
        for t in trips:
            for i in range(1,-1,-1):
                a, b = s.index(t[i]), s.index(t[i+1])
                if( a > b):
                    s[0]=True
                    s.insert(b, s.pop(a))
    return ''.join(s[1:])
