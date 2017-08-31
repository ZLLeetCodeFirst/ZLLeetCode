C = [1,2,3,4,5]
print(C[:3])
class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        print('两个数组长度之和整除:l//2=',l//2)
        if l%2 == 1:
            return self.findKth(A,B,l//2)
        else:
            return (self.findKth(A,B,l//2 - 1) + self.findKth(A,B,l//2)) / 2.0

    def findKth(self, A, B, k):
        print('=======k=,len(A)+len(B)=', k, len(A) + len(B) - 1)
        if len(A) > len(B):
            A, B = B, A
        if not A:
            return B[k]
        if k == len(A) + len(B) - 1:
            return max(A[-1], B[-1])
        i = len(A) // 2
        j = k - i
        print('i,k,j,A[i],B[j]',i,k,j,A[i],B[j])
        if A[i] > B[j]:
            # Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
            return self.findKth(A[:i], B[j:], i)
        else:
            print('A[i:]=,B[:j]=',A[i:],B[:j])
            return self.findKth(A[i:], B[:j], j)

if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1,3,5,7],[2,4,5,6]))

