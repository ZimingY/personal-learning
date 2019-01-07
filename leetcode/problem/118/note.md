## list
list 不能给没有创建过的位置赋值。

b = []

b.append(0)

b[0]=1 % work

b[1] =1 % wrong


b.append([1] * 3 ) ====> b=[ 0,  [1,1,1]]
