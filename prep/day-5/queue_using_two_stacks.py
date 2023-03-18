# https://www.hackerrank.com/challenges/one-week-preparation-kit-queue-using-two-stacks/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-five&h_r=next-challenge&h_v=zen
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Queue:
    queue_elements: list = []

    def __init__(self):
        pass

    def enqueue(self, n):
        self.queue_elements.append(n)

    def dequeue(self):
        n = self.queue_elements[0]
        self.queue_elements = self.queue_elements[min(
            1, len(self.queue_elements)):]
        return n

    def get_head(self):
        return self.queue_elements[0]


if __name__ == "__main__":
    n = int(input())
    queue = Queue()
    for _ in range(n):
        q = str(input())
        if int(q[0]) == 1:
            queue.enqueue(int(q[2:]))
            pass
        elif int(q[0]) == 2:
            queue.dequeue()
        else:
            print(queue.get_head())
