
def read_txt():
    with open("./data/login.txt","r",encoding="utf-8")as f:
        return f.readlines()

if __name__ == '__main__':
    print(read_txt())
    print("--" * 30)

    arrs = []
    for arr in read_txt():
        arrs.append(tuple(arr.strip().split(",")))
    print(arrs[1::])