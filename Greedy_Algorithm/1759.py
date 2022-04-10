import itertools
L, C = map(int,input().split())
words = sorted(list(input().split()))
possibles = itertools.combinations(words, L)
for possible in possibles:
    moum_count = 0
    jaum_count = 0
    for al in possible:
        is_moum = False
        for moum in ["a", "e", "i", "o", "u"]:
            if al==moum:
                is_moum = True
        if is_moum:
            moum_count +=1
        else:
            jaum_count += 1 
    
    if jaum_count >=2 and moum_count >=1:
        print(''.join(possible))