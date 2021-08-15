class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if(x>0):
            a = str(x)
            a = a[::-1]
            return int(a) if int(a)<=2**31-1 else 0
        else:
            x=-1*x
            a = str(x)
            a = a[::-1]
            return int(a)*-1 if int(a)<=2**31 else 0 