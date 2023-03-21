# https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
def is_palindromic_number(i):
    return str(i) == str(i)[::-1]


def sol(nums):
    res = any([is_palindromic_number(n)
              for n in nums]) and all([n >= 0 for n in nums])
    return res


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    print(sol(numbers))
