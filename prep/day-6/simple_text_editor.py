# https://www.hackerrank.com/challenges/one-week-preparation-kit-simple-text-editor/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-six
# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_action_map():
    actions_taken = []

    def append(string, string_to_add):
        actions_taken.append((1, lambda x: x[:-len(string_to_add)]))
        return string+string_to_add

    def delete(string, chars_to_delete):
        chars_to_delete = int(chars_to_delete)
        actions_taken.append((2, lambda x: x+string[-chars_to_delete:]))
        return string[:-chars_to_delete]

    def print_char_at(string, idx_to_print):
        idx_to_print = int(idx_to_print) - 1
        print(string[idx_to_print])
        return string

    def undo(s):
        _, last_action = actions_taken.pop()
        return last_action(s)
    actions = {
        1: append,
        2: delete,
        3: print_char_at,
        4: undo
    }
    return actions


if __name__ == "__main__":
    q = int(input())
    s = ""
    actions = get_action_map()
    for _ in range(q):
        act, *rest = str(input()).split(" ")
        s = actions[int(act)](s, *rest)
