import math
def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    print(f"You'll need {number_of_cans} cans of paint.")

h = int(input('Enter the height of the wall in meters: '))
w = int(input('Enter the width of the wall in meters: '))
coverage = 7

paint_calc(height=h, width=w, cover=coverage)
