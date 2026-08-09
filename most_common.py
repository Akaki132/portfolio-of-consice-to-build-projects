location = input("please input files name: ")
count = {}
ammount = 0
some = []
times = 0

with open(f"{location}") as file:
    text = file.readlines()
    for word in text:
        word = word.strip()
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    
    sorted_dict = sorted(count.items(), key=lambda x: x[1], reverse=True)
    for key, value in sorted_dict:
        if times == 5:
            break
        else:
            print(f"{key} was mentioned {value} times")
            times += 1