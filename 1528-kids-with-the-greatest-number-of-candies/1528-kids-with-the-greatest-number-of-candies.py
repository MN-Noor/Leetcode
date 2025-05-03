class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bool_array=[]
        max_candy=candies[0]
        for candy in candies:
            if candy>= max_candy:
                max_candy=candy

        for candy in candies:
            total_candy=candy+extraCandies
            if total_candy>=max_candy:
                bool_array.append(True)
            else:
                bool_array.append(False)
        return bool_array
                   

        