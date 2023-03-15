# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    res = sum([mark for mark in student_marks[query_name]])
    print("{:.2f}".format((res / len(student_marks[query_name]))))
