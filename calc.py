 print("best calculator ever!")


x = int(input("X: "))
y = int(input("Y: "))

print(f"sum: {x + y}")
print(f"sub: {x - y}")
print(f"mul: { x * y}")
if y == 0:
	print("can't do it!")
else:
	print(f"div: {x / y}")
