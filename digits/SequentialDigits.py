class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits='123456789'
        minlen =len(str(low))
        maxlen=len(str(high))
        res=[]
        for i in range(minlen,maxlen+1):
            for j in range(0, 10 -i):
                substr = digits[j:j+i]
                if low<=int(substr)<=high:
                    res.append(int(substr))
        return res
                    
