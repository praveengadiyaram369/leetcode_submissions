# _605. Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        if n == 0:
            return True
        elif len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False
            return True
        
        for index in range(len(flowerbed)):
            if n < 1:
                break
            elif flowerbed[index] == 0:
                if (index == 0 and flowerbed[index +1] == 0) or (index == len(flowerbed)-1 and flowerbed[index -1] == 0) or (flowerbed[index - 1] == 0 and flowerbed[index +1] == 0):
                    flowerbed[index] = 1
                    n -= 1
        if n > 0:
            return False
        else:
            return True