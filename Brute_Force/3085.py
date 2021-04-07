N = int(input())
candies = ['0' for x in range(N)]
for i in range(N):
    candies[i] = [x for x in input()]

def count_candy(x,y):
    row_count = 0
    col_count = 0
    max_count = 0
    row_start = candies[0][y]
    col_start = candies[x][0]
    for i in range(N):
        if candies[i][y]==row_start:
            row_count += 1
            if max_count < row_count:
                max_count = row_count
        else:
            row_start = candies[i][y]
            row_count = 1

        if candies[x][i]==col_start:
            col_count += 1
            if max_count < col_count:
                max_count = col_count
        else:
            col_start = candies[x][i]
            col_count = 1
    return max_count


def change_candy(x1, y1, x2, y2):
    temp = candies[x1][y1]
    candies[x1][y1] = candies[x2][y2]
    candies[x2][y2] = temp

max_count = list()
for i in range(N):
    for j in range(N):
        # Right,
        if j<N-1:
            change_candy(i,j, i, j+1)
            max_count.append(count_candy(i,j))
            max_count.append(count_candy(i, j+1))
            change_candy(i, j+1, i, j)
        # Down
        if i<N-1:
            change_candy(i,j, i+1, j)
            max_count.append(count_candy(i, j))
            max_count.append(count_candy(i+1, j))
            change_candy(i + 1, j, i, j)
        # print(i, j, max(max_count))
# print(max_count)
print(max(max_count))
