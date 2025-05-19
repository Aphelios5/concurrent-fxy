import multiprocessing

def calculate_fx(x, queue):
    if x == 1:
        queue.put(1)
        return
    result = 1
    for i in range(2, x + 1):
        result *= i
    queue.put(result)

def calculate_fy(y, queue):
    if y == 1 or y == 2:
        queue.put(1)
        return
    
    a, b = 1, 1
    for _ in range(3, y + 1):
        a, b = b, a + b
    queue.put(b)

if __name__ == '__main__':
    x = int(input("请输入x的值(x > 0): "))
    y = int(input("请输入y的值(y > 0): "))
    
    queue = multiprocessing.Queue()
    
    p1 = multiprocessing.Process(target=calculate_fx, args=(x, queue))
    p2 = multiprocessing.Process(target=calculate_fy, args=(y, queue))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    fx = queue.get()
    fy = queue.get()
    
    fxy = fx + fy
    
    print(f"f({x}) = {fx}")
    print(f"f({y}) = {fy}")
    print(f"f({x},{y}) = {fx} + {fy} = {fxy}")
