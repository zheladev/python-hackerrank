# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sortedList = list(set(arr))
    sortedList.sort()
    sortedList.reverse()
    if len(sortedList) > 1:
        print(sortedList[1])
    else:
        print(sortedList[0])
