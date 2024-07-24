myList = ["Deji", "Solomon", "Solomon"]
myNames = ["Sarah", "John"]

print(myList)

myList.insert(0, "Daniel")

myList.extend(myNames)

myList.append("Sylvia")
myList.append([1, 2, 3])

print(myList)

print(myList.count('Solomon'))

myList.clear()

print(myList)


myNumberList = ["Zimbabwe", "South Africa", "Russia", "Nigeria", "America"]

myNumberList.sort(reverse=True)

print(myNumberList)