var_data = [
    ['a', 'c', 'b', 'e', 'd'],
    ['s', 'f', 'w', 'z'],
    ['g', 'e', 'f'],
    ['w', 's'],
]

len_var = len(var_data)
count = 0
while (count < len_var):
    count = count + 1
    for i in range (0, len_var-1):
        if len(var_data[i])> len(var_data[i+1]):
            c = var_data[i]
            var_data[i] = var_data[i+1]
            var_data[i+1] = c

for k in range (0, len(var_data)):
    kosong = []
    j = 0
    while j <= len(var_data[k])-1:
        for i in range (0, len(var_data[k])):
            z = var_data[k][i]
            asc = ord(z)
            kosong.append(asc)
            j += 1

        count = 0
        while (count < len(var_data[k])):
            count = count + 1
            for i in range (0, len(var_data[k])-1):
                if kosong[i]> kosong[i+1]:
                    c = kosong[i]
                    kosong[i] = kosong[i+1]
                    kosong[i+1] = c

        arr_baru = kosong
        
        for k in range (0, len(arr_baru)-1):
            emp = []
            itr = 0
            while itr <= len(arr_baru)-1:
                for n in range (0, len(arr_baru)):
                    q = arr_baru[n]
                    alph = chr(q)
                    emp.append(alph)
                    itr += 1
        print(emp)