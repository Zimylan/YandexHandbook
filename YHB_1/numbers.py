a = input("fff")
b = input('fff')
a = f"{a:0>3}"
b = f"{b:0>3}"
A = list(a)
B = list(b)
broken_summ = [0] * 3
for i in range(0, 3):
    broken_summ[i] = (int(A[i]) + int(B[i])) % 10
print("".join(map(str,broken_summ)))