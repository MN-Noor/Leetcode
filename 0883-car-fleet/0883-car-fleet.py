class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ls=[[pos,speed]for pos,speed in zip(position,speed)]
        stack=[]
        for pos,speed in sorted(ls)[::-1]:
            time=(target-pos)/speed
            stack.append(time)
            if len(stack)>=2  and stack[-1]<=stack[-2]:
                stack.pop()
        print(stack)
        return len(stack)


            
            

        