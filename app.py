

first = int(input('Enter first Number : '))
second = int(input('Enter second Number : '))

add = first + second
sub = first-second
multi = first*second
division = float(first)/float(second)
mode = float(first) % float(second)

print(" What You want Type Here, like ( add, sub, multi, division, mode) ")
select = input("Type Here = ").lower()

if select == 'add':
    print(f" First value {first} Second Value {second} & Your total Sum is = {add}")
elif select == 'sub':
    print(f" First value {first} Second Value {second} & Your total Sub is = {sub}")
elif select == 'multi':
    print(f" First value {first} Second Value {second} & Your total Multi is = {multi}")
elif select == 'division':
    print(f" First value {first} Second Value {second} & Your total Division is = {division}")
elif select == 'mode':
    print(f" First value {first} Second Value {second} & Your total Mode is = {mode}")




