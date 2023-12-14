def calculate_area(length:float,width:float):
	if length == width:
		return "This is a square!"
	return length*width


length = float(input('Enter length: '))
width = float(input('Enter width: '))

area = calculate_area(length,width)

print(area)