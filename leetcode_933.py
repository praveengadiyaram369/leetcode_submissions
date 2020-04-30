# _933. Number of Recent Calls


class RecentCounter:

    def __init__(self):
        self.queue = []

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while len(self.queue) > 1:
            if self.queue[0] < (t - 3000):
                self.queue.pop(0)
            else:
                break

        return len(self.queue)
