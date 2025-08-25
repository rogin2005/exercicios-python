def fibonacci(n):
    print('_'*50)
    
    a, b = 0, 1
    
    sequence =[]
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
        
    return sequence
    
ola = int(input('Digite quantos números fibonacci vc quer: '))
print(fibonacci(ola))