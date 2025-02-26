import random
import turtle
# Green Red Blue Brown Orange Yellow

#starting values
scalar = 1
start_point_x = -400
start_point_y = -350
turtle.colormode(255)
turtle.speed(0)
turtle.width(5*scalar)
circle_size = 30
def create_board():
    turtle.penup()
    turtle.fillcolor(77, 57, 0)
    turtle.begin_fill()
    turtle.goto(start_point_x*scalar,start_point_y*scalar)
    turtle.pendown()
    turtle.forward(800*scalar)
    turtle.left(90)
    turtle.forward(700*scalar)
    turtle.left(90)
    turtle.forward(800*scalar)
    turtle.left(90)
    turtle.forward(700*scalar)
    turtle.end_fill()
    turtle.left(180)
    for i in range(4):
        turtle.forward((700*scalar)/8)
        turtle.right(90)
        turtle.forward(800*scalar)
        turtle.left(90)
        turtle.forward((700*scalar)/8)
        turtle.left(90)
        turtle.forward(800*scalar)
        turtle.right(90)
    turtle.right(90)
    turtle.forward((800*scalar*5)/12)
    turtle.right(90)
    turtle.forward(700*scalar)
    turtle.goto(start_point_x*scalar,start_point_y*scalar)
    turtle.right(180)
    turtle.penup()

def circle(color):   
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(circle_size*scalar)
    turtle.end_fill()
def final_circle(color1, color2, color3):
    global circle_size
    circle_size = 50
    turtle.forward((700/3)*scalar)
    turtle.right(90)
    turtle.forward(((800)/6)*scalar)
    turtle.fillcolor(color1, color2, color3)
    turtle.begin_fill()
    turtle.forward(((800*2)/3)*scalar)
    turtle.left(90)
    turtle.forward((700/3)*scalar)
    turtle.left(90)
    turtle.forward(((800)*2/3)*scalar)
    turtle.left(90)
    turtle.forward((700/3)*scalar)
    turtle.end_fill()
    turtle.left(180)
    turtle.forward(((700/3)*scalar)/5)
    turtle.right(90)
    for i in range(4):
        turtle.forward((((800*2)/3)*scalar)/5)
        circle(answer[i])
        

    
create_board()

print("Green Red Blue Brown Orange Yellow")
while True:
    
    colours = ["green", "red", "blue", "brown", "orange", "yellow"]
    answer = []
    previous_results = []

    for i in range(4):
        answer.append(colours[random.randint(0,5)])
        #sets a random answer

   
    count = 0
    while True:
        while True:
            x_formatted = []
            
           
            x = input("which sequence would you like?")
            x = x.lower()
            ####
            y = ""
           
            for i in range(len(x)):
                if x[i:i+1] != " ":
                    y = y+x[i:i+1]
                else:
                    x_formatted.append(y)
                    y = ""
            x_formatted.append(y)
            c = 0
            if len(x_formatted) == 4:
                for i in range(4):
                    if (x_formatted[i]).lower() in colours:
                        c += 1
                if c == 4:
                    break
                else:
                    print("format must use 4 colours inside the list of usable colours")
            else:
                print("format must use 4 colours")
            ####
        black = 0
        white = 0
        for i in range(len(x_formatted)):
            if x_formatted[i] == answer[i]:
                black += 1
            elif x_formatted[i] in answer:
                white += 1
        x_formatted.append("black =")
        x_formatted.append(black)
        x_formatted.append("white =")
        x_formatted.append(white)
        print(x_formatted)
        
        if count> 0:        
            for i in range(count):
                print(previous_results[count-1-i])
                
        count+= 1
        previous_results.append(x_formatted)
        # 1
        turtle.forward(700*(count-1)*scalar*(1/8) + 12.5*scalar)
        turtle.right(90)
        turtle.forward(40*scalar)
        win_condition = black
        for i in range(black+white):
            
            if black>0:
                circle("black")
                black = black -1
            else:
                circle("white")
            turtle.forward(80*scalar)
        turtle.goto(start_point_x*scalar,start_point_y*scalar)
        turtle.left(90)
        # 2
        turtle.forward(700*(count-1)*scalar*(1/8) + 12.5*scalar)
        turtle.right(90)
        turtle.forward((50 + (800*5)/12)*scalar)

        for i in range(4):
            circle(str(x_formatted[i]).lower())
            turtle.forward(120*scalar)
        turtle.goto(start_point_x*scalar,start_point_y*scalar)
        turtle.left(90)

        if win_condition == 4:
            print("YOU WINN")
            final_circle(26, 255, 26)
            turtle.goto(1000,0)
            
            
        elif count == 8:
            print("you lose:(")
            final_circle(204, 0, 0)
            turtle.goto(1000,0)
            
