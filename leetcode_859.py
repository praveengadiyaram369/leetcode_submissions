# _859. Buddy Strings


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:

        if len(A) != len(B) or (len(A) == len(B) < 2):
            return False

        mismatch_cnt = 0
        missing_char = []

        for i in range(len(A)):
            if A[i] != B[i]:
                mismatch_cnt += 1
                missing_char.append(A[i])
                missing_char.append(B[i])

                if mismatch_cnt > 2:
                    return False

        if mismatch_cnt == 1:
            return False
        elif mismatch_cnt == 2 and missing_char[0] == missing_char[3] and missing_char[1] == missing_char[2]:
            return True
        elif mismatch_cnt == 2 and (missing_char[0] != missing_char[3] or missing_char[1] != missing_char[2]):
            return False
        elif mismatch_cnt == 0 and len(set(A)) != len(A):
            return True

        return False
