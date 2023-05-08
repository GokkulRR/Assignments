'''import the math library'''
import math
class Shapes:
    '''create a function as display shape'''
    def display_shape(self,choice):
        '''create the class as the display'''
        if choice == 1:
            print('\nSelected Shape is Circle')
            radius = float(input('\nEnter the radius of Circle: '))
            print('Area of Circle : ',round(math.pi* radius * radius,2))
            print('Perimeter of Circle : ',round (2 * math.pi * radius,2))

        elif choice == 2:
            print('Selected Shape is Square')
            side = float(input('Enter the side of square: '))
            print('Area of Square : ',round(side * side,2))
            print('Perimeter of Square : ',round (4 * side, 2))

        elif choice == 3:
            print('Selected Shape is Rectangular')
            length = float(input('Enter the length of Rectangular: '))
            width = float(input('Enter the width of Rectangular: '))
            print('Area of Rectangular : ',round(length * width,2))
            print('Perimeter of Rectangular : ',round (2 * (length * width), 2))

        elif choice == 4:
            print('Selected Shape is Triangular')
            height = float(input('Enter the height of triangle: '))
            base = float(input('Enter the Base of triangle: '))
            side_1 = float(input('Enter the Side-1 of triangle: '))
            side_2 = float(input('Enter the Side-2 of triangle: '))

            print('Area of Triangle : ',round((height * base) / (2), 2))
            if base + side_2 > side_1:
                print('Perimeter of Triangle : ',round( side_1 + base + side_2, 2))
            else:
                print('Enter valid input! Rule ( Base + side-2 > side -1)')

        elif choice == 5:
            print('Selected Shape is Cylinder')
            radius = float(input('Enter the radius of Cylinder: '))
            height = float(input('Enter the height of Cylinder: '))
            print('Area of Cylinder:',round((2*math.pi*radius*height)+(2*math.pi*radius*radius),2))
            print('Perimeter of Cylinder : ',round( 2 * (2 * radius + height), 2))

        elif choice == 6:
            print('Selected Shape is Rhombus')
            vertical = float(input('Enter the Vertical diameter of Rhombus: '))
            horizontal = float(input('Enter the Horizontal diameter of Rhombus: '))
            side = float(input('Enter the Side of Rhombus: '))
            print('Area of Cylinder : ',round((vertical * horizontal) / 2, 2))
            print('Perimeter of Cylinder : ',round(4 * side, 2))

        elif choice == 7:
            print('Selected Shape is Cube')
            edge = float(input('Enter the Edge of Cube: '))
            side_length = float(input('Enter the side length of Cube: '))
            print('Area of Cube : ',round((6 * edge * edge),1))
            print('Perimeter of cube : ',round((12 * side_length),1))

        elif choice == 8:
            print('Selected Shape is Cuboid')
            length = float(input('Enter the Length of the Cuboid: '))
            width = float(input('Enter the Width of the Cuboid: '))
            height = float(input('Enter the Height of the Cuboid: '))
            print('Area of Cuboid:',round((2*length*width)+(2*length*height)+(2*height*width),2))
            print('Perimeter of Cuboid : ',round(4 * length * width * height, 2))
        elif choice == 9:
            print('Selected Shape is Pentagon')
            side = float (input('Enter the side of Pentagon: '))
            print('Area of Pentagon:',round((1/4)*math.sqrt(5*(5+2*math.sqrt(5)))*side*side,2))
            print("perimeter of Pentagon : ",round(5 * side, 2))

        elif choice == 10:
            print('Selected Shape is Hexagon')
            side = float(input('Enter the side of hexagon: '))
            print('Area of hexagon : ',round(((5.196) / (2)) * (side * side), 2))
            print('Perimeter of hexagon : ',round(6 * side, 2))

        else:
            print('Enter Option is Invalid')
print("""
1. Circle
2. Square
3. Rectangular
4. Triangular
5. Cylinder
6. Rhombus
7. Cube
8. Cuboid
9. pentagon
10. Hexagon""")

user_input = int(input('\nEnter the Option based on Shape: '))

access = Shapes()
access.display_shape(user_input)
