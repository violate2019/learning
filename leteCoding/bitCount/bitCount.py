class Solution1(object):
    '''暴力法O(n*size(n))'''
    def countBits(self, num):
        return [self.nBits(i) for i in range(num+1)]

    def nBits(self, num):
        cnt = 0
        while num:
            num &= (num-1)
            cnt += 1
        return cnt

print(Solution1().countBits(5))

class Solution(object):
    #思路一： 偶数的二进制的1 的个数正好等于这个数除以2的数字1 的个数， 奇数的二进制的1 的个数正好是奇数除以2 数字1 的个数+1
    def countBits(self,num):
        res=[0] * (num+1)
        for i in range(num+1):
           res[i] = res[i>>1] + i%2
        return res
    #思路二： i&(i-1) 数1 的个数 + 1 正好是i 数1 的个数
    def countBits1(self,num):
        dp = [0]*(num+1)
        dp[0] =0
        for i in range(1,num+1):
            dp[i] = dp[i&(i-1)] +1
        return dp




if __name__ == "__main__":
    print(Solution().countBits(5))
    print(Solution().countBits1(5))
    print(max(1,3,6,9))

