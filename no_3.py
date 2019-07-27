def cetak_gambar(num):
    if num%2 == 0:
        print("Parameter harus bilangan ganjil")
    else:
        cov = int(num/2)
        for i in range(1, cov+1):
            print("*", end = "   ")
            for j in range(1, num-2+1):
                print("=", end="   ")
            print("*")
            print()

        for i in range(1, 2):
            print("*", end = "   ")
            for j in range(1, num-2+1):
                print("*", end="   ")
            print("*")
            print()

        for k in range(1, cov+1):
            print("*", end = "   ")
            for j in range(1, num-2+1):
                print("=", end="   ")
            print("*")
            print()

cetak_gambar(5)