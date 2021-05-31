def main(from_f, to_f):
    with open(from_f, "r") as ff:
        lines = [line for line in ff if line.count(' ') == 0]
    with open(to_f, "w") as tt:
        tt.writelines(lines)
    return min((word for word in lines if word), key=len)


print(main("str1.txt", "str2.txt"))