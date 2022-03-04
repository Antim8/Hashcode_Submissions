# Goodness = n_i where first not last etc


def calc_KG(s):
    c = 0
    for i in range(s.__len__()//2):
        if not s[i] == s[s.__len__()-i]:
            c += 1
    return c

def swap(c):
    if c == 'Z':
        return chr(ord('Z')-1)
    return chr(ord(c)+1)

def do_stuff(s, k_shall):
    
    k_curr = calc_KG(s)
    c = 0
    if k_curr < k_shall:
        s_new = s
        for i in range(s.__len__()//2):
            s_new[i] = swap(s_new[i])
            k_new = calc_KG(s_new)
            if k_new <= k_curr:
                s_new[i] = s[i]
                continue()
            k_curr = k_new
            c += 1
            if k_curr == k_shall
                return c
                
        
    else:
        i = 0
        while k_curr > k_shall:
            s[i] = s[s.__len__()-i]
            if calc_KG(s) == k_curr continue()
            c +=1
            
        return c
            
    

T = int(input())

for i in range(T):
    N, K = [int(j) for j in input().split()]
    S = input()
    if K == calc_KG(S) print(0)
    