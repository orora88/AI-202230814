#레벤슈타인 거리 구하기
def cal_distance(a, b):
    if a == b:
        return 0    #문장이 동일하면 레벤슈타인 거리는 0
    a_len = len(a)
    b_len = len(b)
    if a == "":
        return b_len    #a문장이 공집합이면 레벤슈타인 거리는 b_len
    if b == "":
        return a_len    #b문장이 공집합이면 레벤슈타인 거리는 a_len
    
    #문장표 만들기
    matrix = [[] for i in range(a_len + 1)]
    for i in range(a_len + 1):
        matrix[i] = [0 for j in range(b_len + 1)]

    #0일 때 초기값 설정
    for i in range(a_len + 1):
        matrix[i][0] = i
    for j in range(b_len + 1):
        matrix[0][j] = j
    
    #표 채우기
    for i in range(1, a_len + 1):
        ac = a[i - 1]
        for j in range(1,b_len + 1):
            bc = b[j - 1]
            cost = 0 if (ac == bc) else 1
            matrix[i][j] = min([
                matrix[i-1][j] + 1, #문자 삽입
                matrix[i][j-1] + 1, #문자 제거
                matrix[i-1][j-1] + cost #문자 변경
            ])
    return matrix[a_len][b_len]
