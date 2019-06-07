from funs import *
import time

if __name__ == "__main__":
    
    #x = "ABCBDAB"
    #y = "BDCABA"
    
    x = "acbcf"
    y = "abcdaf"

    print("x=", x)
    print("y=", y)

    start_time = time.perf_counter()
    m = LCS(x, len(x) - 1, y, len(y) - 1)
    end_time = time.perf_counter() - start_time
    print("Iter LCS:", m, "Duration: ", end_time)

    start_time = time.perf_counter()
    (c, b) = LCS_Length(x, y)
    end_time = time.perf_counter() - start_time
    print("Dynm LCS duration: ", end_time)
    print("LCS:", end = "")
    print_LCS(b, x, len(x), len(y))
    print()
    print_matrix(c, b)
    print()
    
    for t in range(5, 18):
        (x, y) = gen_rand_string(t, t-1)
        print("Length:", t)
        print("x=", x)
        print("y=", y)

        start_time = time.perf_counter()
        m = LCS(x, len(x) - 1, y, len(y) - 1)
        end_time = time.perf_counter() - start_time
        print("Iter LCS:", m, "Duration: ", end_time)

        start_time = time.perf_counter()
        (c, b) = LCS_Length(x, y)
        end_time = time.perf_counter() - start_time
        print("Dynm LCS duration: ", end_time)
        print("LCS:", end = "")
        print_LCS(b, x, len(x), len(y))
        print()
        print("-------------")