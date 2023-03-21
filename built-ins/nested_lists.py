# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
if __name__ == '__main__':
    lowest = 0.0
    second_lowest = 0.0
    found_second_lowest = False
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append((name, score))
    records.sort(key=lambda r: r[1])
    lowest, second_lowest = list(dict.fromkeys([s for _, s in records]))[0:2]
    records = [r for r in records if r != lowest]

    names = sorted([name for name, score in records if score == second_lowest])
    print(*names, sep="\n")
