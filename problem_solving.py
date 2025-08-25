def check_triangle(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not avalid  triangle"
    #type  of triangle
    if a == b== c:
        triangle_type = "equilateral"
    elif a==b or b==c or a==c:
        triangle_type="isosceles"
    else:
        triangle_type="scalene"
    # check for right angled traingle
    sides = sorted([a,b,c])
    if sides[0]**2 + sides[1]**2 ==sides[2]**2:
        triangle_type+= " and right_angled triangle"
    return triangle_type


    a=float(input("enter side 1:"))
    b=float(input("enter side 2:"))
    c=float(input("enter side 3:"))
    print(check_triangle(2,4,6))
    

        
    