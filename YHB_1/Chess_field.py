def multiplication_matrix(N):
    MM = [
        [1 if j % 2 == 0 else 0 for j in range(0, N)]
        if i % 2 == 0 else
        [0 if j % 2 == 0 else 1 for j in range(0, N)]
        for i in range(0, N)
    ]
    print('[', end='')
    for mm in MM:
        if mm is MM[-1]:
            print("[", *mm, "]]")
        else:
            print("[", *mm, "]")
    return MM

multiplication_matrix(8)
# print(*multiplication_matrix(8), sep='\n')

