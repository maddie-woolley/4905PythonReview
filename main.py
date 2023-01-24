# Maddie Woolley -- GEOG 4590 Lab 1

# Question 1: Calculate 1+2+3... +100
# maddie woolley
def calculate_sum():
    sum = 0
    for i in range(101):
        sum = sum + i
    print(sum)


calculate_sum()

# ---------------------------------------------------------------
# Question 2: You are counting 1000 apples, print a message when you have completed 10, 20, 30% of the apples
# Maddie Woolley
for i in range(1,1000):
    if i % 100 == 0:
        print(i/10, "% done")
# ---------------------------------------------------------------
# Question 3: myStringList = ["this is a GIS class"]. Write a code to count the number of 's'
# Madison Woolley
myStringList = "this is a GIS class"
s = myStringList.count("s")
print(s)
# ---------------------------------------------------------------
# Question 4: For every 5 numbers, calculate the means of every five numbers.
# Maddie Woolley
InputList = [2, 1, 3, 5, 2, 7, 3, 7, 4, 6, 9, 1, 0, 2, 4, 8, 9, 2, 0, 1, 3]

for i in range(len((InputList))):
    sub = InputList[i:i + 5]
    addup = sum(sub)
    mean = float(addup / 5)
    if (len(sub) == 5):
        print(mean)

# ---------------------------------------------------------------
# question 5 - calculate the medians of every 5 numbers
# maddie woolley
InputList = [0, 1, 9, 2, 2, 8, 3, 0, 4, 5, 9, 1, 0, 2, 4, 5, 9, 2, 1, 0, 6]
i = 0
for i in range(len(InputList)):
    sub = InputList[i:i + 5]
    sub.sort()
    if(len(sub)==5):
        print(sub[2])