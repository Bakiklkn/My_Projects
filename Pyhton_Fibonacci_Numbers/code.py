fibonacci = [1]
y = 1
for i in range(1,10):
  fibonacci.append(y)
  y = fibonacci[i-1]+ fibonacci[i]
  i += 1
print(fibonacci)
