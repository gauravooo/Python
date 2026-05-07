# Problem Set 7 - Grocery List
def main():
    entry = []
    d = {}
    try:
        while True:
            i = input("").upper()
            entry.append(i)
    except EOFError:
        pass
    for j in entry:
            if j in d:
                d[j] += 1
            else:
                d[j] = 1
    for m in sorted(d):
            print(f"{d[m]} {m}")
main()

