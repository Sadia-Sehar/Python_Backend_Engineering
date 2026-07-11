def area_of_rectangle(width=1,length=2):
    area=width*length
    perimeter=2*(width+length)
    return area, perimeter

area,perimeter=area_of_rectangle()
print(f"Area: {area}, Perimeter: {perimeter}")    
print(f"(Area,Permiter): {area_of_rectangle(4,5)}")

def check(age):
    if age<0:
        print("Invalid Age")
        return False
    print("Valid Age")
    return True
while True:
    age=int(input("Enter age: "))
    if check(age):
        print("Running function again.....")
        check(age)
        print(check(age))
        break

def test():
    print("Hi")
test()
response=test()
print(response)

def make_total():
    subtotal=100
    return subtotal
print(make_total())

x = 10
def test():
    global x #without this-error #But not recommended as a professional programmer
    print(x)
    x = 20
test()

