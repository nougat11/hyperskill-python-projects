
def input_matrix(word):
    n, m = [int(x) for x in input(f"Enter size of {word} matrix: ").split()]
    matrix = []
    print(f"Enter {word} matrix:")
    for _ in range(n):
        matrix.append([int(x) if x.count('.') == 0 else float(x) for x in input().split()])
    return matrix
def print_matrix(a):
    for i in range(len(a)):
        print(*a[i], sep = ' ')
def addition_matrix():
    a = input_matrix("first ")
    b = input_matrix("second ")
    n1, m1 = len(a), len(a[0])
    n2, m2 = len(b), len(b[0])
    if n1 == n2 and m1 == m2:
        for i in range(n1):
            for j in range(m1):
                a[i][j] += b[i][j]
        print("The result is:")
        print_matrix(a)
    else:
        print("The operation cannot be performed.")
def scalar_multiplication():
    a = input_matrix("")
    b = float(input("Enter constant:"))
    n, m = len(a), len(a[0])
    for i in range(n):
            for j in range(m):
                a[i][j] *= b
    print("The result is:")
    print_matrix(a)
def multiplication():
    a = input_matrix("first ")
    b = input_matrix("second ")
    n1, m1 = len(a), len(a[0])
    n2, m2 = len(b), len(b[0])
    matrix = [[] for _ in range(n1)]
    if m1 == n2:
        for i in range(n1):
            for j in range(m2):
                ram = 0
                for k in range(m1):
                    ram += a[i][k] * b[k][j]
                matrix[i].append(ram)
        print("The result is:")
        print_matrix(matrix)
    else:
         print("The operation cannot be performed.")
def transpose_main(a):
    for i in range(len(a)):
        for j in range(i + 1):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a
def transpose_horizontal(a):
    for i in range(len(a)):
        a[i] = a[i][::-1]
    return a
def transpose_vertical(a):
    for i in range(len(a) // 2):
        a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
    return a
def determinant(a):
    if len(a) == 1:
        return a[0][0]
    if len(a) == 2:
        return a[0][0] * a[1][1] - a[1][0] * a[0][1]
    sum = 0
    for i in range(len(a)):
        sum += (-1) ** i * a[0][i] * determinant([a[j][:i]+a[j][i+1:] for j in range(1,len(a))])
    return sum
def minor_matrix(a):
    b = [0 for _ in range(len(a))] * len(a)
    
    q=-1
    for i in range(len(a)):
        q+=1
        for j in range(len(a)):
            mm = []
            for k in range(len(a)):
                if k == i:
                    continue
                else:
                    mm.append(a[k][:j] + a[k][j+1:])
                    
               
            matrix = determinant(mm)
            
            b[i*len(a)+j]=((-1) ** (i + j) * matrix)
            
    return b
def inverse_matrix(a):
    deter = determinant(a)
    if deter == 0:
        print("This matrix doesn't have an inverse.")
        return
    const = 1 / deter
    a = transpose_main(a)
    b = minor_matrix(a)
   
    for i in range(len(a) * len(a)):
        b[i] = round(b[i] * const, 4)
    print("The result is:")
    n = len(a)
    for i in range(n):
        for j in range(n):
            print(b[i*n+j], end = " ")
        print('',end="\n")
            
    
        
                    
        
    
    
    
while True:
    print("1. Add matrices") 
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix.')
    print("0. Exit")
    action = int(input('Your choice: '))
    if action == 1:
        addition_matrix()
    elif action == 2:
        scalar_multiplication()
    elif action == 3:
        multiplication()
    elif action == 4:
        
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        action = int(input('Your choice: '))
        a = input_matrix("")
        if action == 1:
            a = transpose_main(a)
        elif action == 2:
            a = transpose_main(a)
            a = transpose_horizontal(a)
            a = transpose_vertical(a)
        elif action == 3:
            a = transpose_horizontal(a)
        elif action == 4:
            a = transpose_vertical(a)
        
        print("The result is:")
        print_matrix(a)
        
    elif action == 0:
        break
    elif action == 5:
        a = input_matrix("")
        print("The result is \n",determinant(a))
    elif action == 6:
        a = input_matrix("")
        inverse_matrix(a)
        
        
   
       
