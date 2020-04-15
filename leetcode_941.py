# _941. Valid Mountain Array

# _Approach 1:


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:

        if len(A) < 3:
            return False

        peak_cnt = 0

        temp = A[0]
        for index in range(1, len(A)):
            temp_1 = A[index]
            A[index] -= temp
            temp = temp_1

            if A[index] < 0:
                A[index] = 'F'
            elif A[index] > 0:
                A[index] = 'T'

            if A[index] == 0:
                return False
            elif index > 1 and A[index] == 'F' and A[index-1] == 'T':
                peak_cnt += 1

                if peak_cnt > 1:
                    return False

            if index == 1:
                repeat = A[1]
                comp_a = A[1]
            else:
                if repeat != A[index]:
                    repeat = A[index]
                    comp_a += repeat

                    if len(comp_a) >= 2 and comp_a[:2] != 'TF':
                        return False

        if peak_cnt == 0:
            return False
        if comp_a == 'TF':
            return True
        return False


# _Approach 2

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:

        n = len(A)

        if n < 3:
            return False

        i = 0

        while i < n-1 and A[i] < A[i+1]:
            i += 1

        if i in (0, n-1):
            return False

        while i < n-1 and A[i] > A[i+1]:
            i += 1

        return i == n-1
