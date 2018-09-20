## idea

两个指针，一个for里面consecutively移动，一个只在两element不一样的时候移动，且不一样的时候把前面的substitute后面那个。

## In-place algorithm

ransforms input using no __auxiliary data structure__, while a small amount of extra storage space is allowed for __auxiliary variables__.

input is usually __overwritten__ by the output.

the strict definition of in-place algorithms includes all algorithms with __O(1)__ space complexity.



## always first check if input is valid

        if not A:
            return 0
            
            
