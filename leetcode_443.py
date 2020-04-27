# _443. String Compression


class Solution:

    def copy_char_cnt(self, chars, char_cnt, moving_index):
        if char_cnt == 1:
            return moving_index
        cnt_str = str(char_cnt)
        n = len(cnt_str)
        for i in range(n):
            chars[moving_index+i] = cnt_str[i]
        return moving_index + n

    def delete_tail(self, chars, prev_char, char_cnt, moving_index, repeat):
        chars[moving_index] = prev_char
        if repeat == True:
            moving_index = self.copy_char_cnt(chars, char_cnt, moving_index+1)
            del chars[moving_index:]
        else:
            del chars[moving_index+1:]

    def compress(self, chars: List[str]) -> int:

        n = len(chars)
        prev_char = chars[0]
        char_cnt = 1
        moving_index = 0

        for index in range(1, n):
            char = chars[index]
            if prev_char == char:
                char_cnt += 1
                if index == n-1:
                    self.delete_tail(chars, prev_char,
                                     char_cnt, moving_index, True)
            else:
                chars[moving_index] = prev_char
                moving_index = self.copy_char_cnt(
                    chars, char_cnt, moving_index+1)
                prev_char = char
                char_cnt = 1
                if index == n-1:
                    self.delete_tail(chars, prev_char,
                                     char_cnt, moving_index, False)
