print("COLOR MIXER ")

color_mixes = {
    ('red','blue'):'purple',
    ('red','yellow'):'orange',
    ('blue','yellow'):'green',
    ('blue','green'):'teal',
    ('white','red'):'pink',
    ('red','green'):'brown'
}
while True:
    color1 = input("Enter your first color: \n").lower().strip()
    color2 = input("Enter your second color: \n").lower().strip()
    mix = None
    if (color1,color2) in color_mixes:
        mix = color_mixes[(color1,color2)]
    elif (color2,color1) in color_mixes:
        mix = color_mixes[(color2,color1)]
    if mix:
        print(f"When you mix {color1} and {color2} you got {mix}")
    else:
        print("I dont know that color ")
    if not input("\ntry again (y/n)?").lower().startswith('y'):
        print("Goodbye!")
        break
