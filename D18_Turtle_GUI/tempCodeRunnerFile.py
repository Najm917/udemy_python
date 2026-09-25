in range(3, 11):
    timmy.color(get_random_color())  
    angle = 360 / sides              # Exact turn angle for any regular polygon
    for _ in range(sides):
        timmy.forward(90)
        timmy.right(angle)