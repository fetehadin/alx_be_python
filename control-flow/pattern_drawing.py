size = int(input("Enter the size of the pattern:"))
i = 1
j = 1
while i <= size:
    while j <= size:
        print(f"*"*size)
        j += 1
    i += 1
        