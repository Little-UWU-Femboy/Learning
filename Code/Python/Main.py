def start():
    n = int( input("Enter number of doors: "))
    doors = []

    for x in range(n):
        doors.append(False)

    for i in range(1, n+1):
        for j in range(i-1, n, i):
            print(f"i:{i} j:{j+1} door {j+1} is toggled")
            if doors[j]:
                doors[j] = False
            else:
                doors[j] = True

    for i in range(n):
        if doors[i]:
            print(f"Door {i+1} is open")
        else:
            print(f"Door {i+1} is closed")

    opened = []
    closed = []
    
    for i in range(0, n):
        if doors[i]:
            opened.append(True)
        else:
            closed.append(False)

    print(opened)
    print(closed)

if __name__ == "__main__":
    start()
