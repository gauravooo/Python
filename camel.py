# Camel Case
def main():
    camelcase = input("Camelcase: ").strip()

    for i in camelcase:
        if i == i.upper():
            print(f"_{i.lower()}",end ="")
        else:
            print(i,end = "")
    print(end ="\n")
main()