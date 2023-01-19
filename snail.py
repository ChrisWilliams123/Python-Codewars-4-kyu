#Solution to Codewars kata https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1


def snail(s_m):
    return [*s_m[0]] + snail([*zip(*s_m[1:])][::-1]) if s_m else []
