t = int(input())
            
for i in range(t):
    k = int(input())
    n = int(input())
    k_list = []
    
    for i in range(k+1):
        k_list.append([])
        for j in range(n):
            k_list[i].append(0)
    
    for i in range(n):
        k_list[0][i] = i+1
    
    temp = 0
    for i in range(1,k+1):
        for j in range(1,n+1):
            for l in range(j):
                temp += k_list[i-1][l]
            k_list[i][l] += temp
            temp = 0
    print(k_list[k][n-1])