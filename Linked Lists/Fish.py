def FibbCalc(last, this, i):
    print(last)
    i += 1
    if i == final:
        return
    FibbCalc(this, this + last, i)

if __name__ == "__main__":
    final = int(input("How many digits would you like printed?"))
    FibbCalc(0, 1, 0)