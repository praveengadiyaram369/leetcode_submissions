# _686. Repeated String Match


class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:

        if B in A:
            return 1

        repeat_cnt = 1
        base = A
        limit = int(len(B)/len(A)) + 3

        if len(set(A)) == len(set(B)):
            while repeat_cnt < limit:

                if B in base:
                    return repeat_cnt

                repeat_cnt += 1
                base += A

        return -1
