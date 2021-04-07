dwarf_list = []
for _ in range(9):
    dwarf_list.append(int(input()))

find = False
x, y = 0, 0
for i in range(9):
    for j in range(i+1, 9):
        if sum(dwarf_list) - (dwarf_list[i] + dwarf_list[j]) == 100:
            find = True
            x, y = dwarf_list[i], dwarf_list[j]

        if find:
            break
    if find:
        break

dwarf_list.remove(x)
dwarf_list.remove(y)
for i in sorted(dwarf_list):
    print(i)