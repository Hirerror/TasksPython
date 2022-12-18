class Task:
    def sort_list(list):
        if list == []:
            return list
        lMin = []
        lMax = []
        for i in range(0,(len(list))):
            if min(list) == list[i]:
                lMin.append(i)
            if max(list) == list[i]:
                lMax.append(i)
        zMin = list[lMin[0]]
        zMax = list[lMax[0]]

        for n in range(0,(len(lMin))):
            list[lMin[n]] = zMax
        for f in range(0,(len(lMax))):
            list[lMax[f]] = zMin
        list.append(zMin)
        return list
T = Task
print(T.sort_list([1,2,1,3]))
print(T.sort_list([1]))
print(T.sort_list([]))
print(T.sort_list([2, 4, 6, 8]))