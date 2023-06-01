for i in range(1, 101):
    print(f"{(i - 1) // 10 + 1} x {i % 10 or 10} = {i * ((i - 1)//10+1)}")