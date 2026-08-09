import statistics
import sys

x = 9.5
list1 = []
try:
    sys.argv[1]
except IndexError:
    pass
else:
     x = float(sys.argv[1])   

def make_up(data):
    for i in data.split():
        list1.append(float(i))
    mean = statistics.mean(list1)

    if mean < x:
        while True:
            list1.append(10)
            mean = statistics.mean(list1)
            if mean >= x:
                break
    return len(list1) - len(data.split())

if __name__ == "__main__":
    try:
        data = input("შეიყვანეთ შეფასებები: (გამოყეთ ისინი ცარიალი ადგილით!) ")
        print("გამოსასწორებლად საჭიროა", make_up(data), "ათიანი")
    except:
        sys.exit()