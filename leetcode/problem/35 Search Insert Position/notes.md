## [List Comprehensions in Python](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)

[ expression for item in list if conditional]


### eg1
```
new_list = []
for i in old_list:
    if filter(i):
        new_list.append(expressions(i))
```

to 

```
new_list = [expression(i) for i in old_list if filter(i)]
```

### eg2
```
squares = []

for x in range(10):
    squares.append(x**2)
````

to 

```
squares = [x**2 for x in range(10)]
```


### eg3
```
listOfWords = ["this","is","a","list","of","words"]

items = [ word[0] for word in listOfWords ]

print items
```

The output should be: ['t', 'i', 'a', 'l', 'o', 'w']
