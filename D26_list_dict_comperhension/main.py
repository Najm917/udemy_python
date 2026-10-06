import turtle
import pandas
screen = turtle.Screen()

screen.setup(width=650, height=850)
screen.title("Coordinate Tracker - Click on States")
screen.title("Indian States Guessing Game")

image = "indian_map.gif"
screen.addshape(image)

map_show = turtle.Turtle()
map_show.shape(image)

# ____________________________
# this method known as x and y axis value

# def get_mouse_click_coor(x, y):
#     print(f"x axis:{x},y axis:{y}")
# screen.onscreenclick(get_mouse_click_coor)
# screen.mainloop()
# ____________________________


country_data=pandas.read_csv("indian_statees.csv")
all_state=country_data["state"].to_list()
guessed_states=[]

while len(guessed_states)<len(all_state):
  answer_map_guess=screen.textinput(title=f"{len(guessed_states)}/{len(all_state)} Statte Correct",prompt=" Guess the country's state name or ('Exit' to exit)").title()
  if answer_map_guess=="Exit":
    # list comperhension
    missing_state=[state for state in all_state if state not in guessed_states ]
    
    new_data=pandas.DataFrame(missing_state)
    new_data.to_csv("states_to_lern.csv")
    break
  if answer_map_guess in all_state:
    guessed_states.append(answer_map_guess)
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data=country_data[country_data.state==answer_map_guess]
    t.goto(state_data.x.item(),state_data.y.item())
    t.write(answer_map_guess)
    
    



# screen.exitonclick()
