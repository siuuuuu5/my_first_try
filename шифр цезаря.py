a = "абвгґдеєжзиіїйклмнопрстуфхцчищьюяабвгґдеєжзиіїйклмнопрстуфхцчищьюяabcdefghiklmnopqrstvxyzabcdefghiklmnopqrstvxyz01234567890123456789"
b = input(": ")
key = 1
andriy = b.lower()
c = ""
for i in andriy:
    andriylox1 = a.find(i)
    andriylox2 = andriylox1 + key
    if i in a:
        if andriylox2 > 136:
            andriylox2 = andriylox2 - 137
    c = c + a[andriylox2]
else:
    print(c)
    andriylox1 = a.find(i)
    c = c + a[andriylox2]
