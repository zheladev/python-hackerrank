# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true
if __name__ == "__main__":
    n, x = list(map(int, input().split()))
    l = []
    for _ in range(0, x):
        l.append(list(map(float, input().split())))
    zipped_student_marks = list(zip(*l))
    student_averages = ["{:.2f}".format(sum(
        [m for m in student_marks])/len(student_marks)) for student_marks in zipped_student_marks]
    print(*student_averages, sep="\n")
