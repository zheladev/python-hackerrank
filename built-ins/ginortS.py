# https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_char_custom_type(char):
    # type 3 = even number, type 2 = odd number, type 1 = uppercase, type 0 = lowercase
    ord_char = ord(char)
    lc_a_int_value, lc_z_int_value = ord('a'), ord('z')
    uc_A_int_value, uc_Z_int_value = ord('A'), ord('Z')
    if ord_char >= lc_a_int_value and ord_char <= lc_z_int_value:
        return 0
    elif ord_char >= uc_A_int_value and ord_char <= uc_Z_int_value:
        return 1
    else:
        # odd -> 2; even -> 3
        return 3 if int(chr(ord_char)) % 2 == 0 else 2


def merge_substrings(sub1, sub2):
    new_list = []
    while (len(sub1) > 0 and len(sub2) > 0):
        if is_higher(sub1[0], sub2[0]):
            new_list.append(sub1[0])
            sub1 = sub1[1:]
        else:
            new_list.append(sub2[0])
            sub2 = sub2[1:]
    for char in sub1:
        new_list.append(char)
    for char in sub2:
        new_list.append(char)
    return "".join(new_list)


def is_higher(comp1, comp2):
    type1, type2 = get_char_custom_type(comp1), get_char_custom_type(comp2)
    if type1 != type2:
        return type1 < type2
    else:
        return ord(comp1) < ord(comp2)


def ginorts(to_sort):
    sorted_str = to_sort
    if len(to_sort) == 2:
        # flip
        sorted_str = to_sort if is_higher(
            to_sort[0], to_sort[1]) else to_sort[::-1]
    if len(to_sort) < 2:
        # already sorted since there's only 1 / 0 elements
        pass
    else:
        # recursively call ginorts on both subsequences
        substr1 = ginorts(to_sort[:len(to_sort)//2])
        substr2 = ginorts(to_sort[len(to_sort)//2:])
        sorted_str = merge_substrings(substr1, substr2)
    return sorted_str


if __name__ == "__main__":
    string_to_sort = str(input())
    sorted_string = ginorts(string_to_sort)
    print(sorted_string)
