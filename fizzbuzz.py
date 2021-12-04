# fizz buzz
skip_dic = {3: "fizz", 5: "buzz"}
start_value = 1
end_value = 15
for i in range(start_value, end_value+1):
    n = 0
    print("\n")
    for j in skip_dic:
        if i % j == 0:
            n += 1
            print(skip_dic[j], end="")
    if n == 0:
        print(i)

