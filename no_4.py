def count_substring(string):
    a = 'a' 
    i = 'i'
    u = 'u'
    e = 'e'
    o = 'o'

    n_a = 0
    n_i = 0
    n_u = 0
    n_e = 0
    n_o = 0
    
    for j in range(len(string)-len(a)+1):
        if(string[j:j+len(a)] == a):      
            n_a+=1

    for j in range(len(string)-len(i)+1):
        if(string[j:j+len(i)] == i):      
            n_i+=1

    for j in range(len(string)-len(u)+1):
        if(string[j:j+len(u)] == u):      
            n_u+=1

    for j in range(len(string)-len(e)+1):
        if(string[j:j+len(e)] == e):      
            n_e+=1

    for j in range(len(string)-len(o)+1):
        if(string[j:j+len(o)] == o):      
            n_o+=1
    
    result = n_a+n_i+n_u+n_e+n_o   
    print(result)


count_substring('programmer')