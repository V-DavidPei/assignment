import turtle
from PIL import Image
# Set up the turtle screen



def draw_branch(branch_length):
    '''
        绘制分型树
        :param branch_length:
        :return:
    '''
    if branch_length > 5:
        if branch_length > 10:
            turtle.pensize(10)
            turtle.color('brown')
        else:
            turtle.pensize(5)
            turtle.color('green')

        # 绘制右侧树枝
        turtle.forward(branch_length)


        print('向前',branch_length)
        turtle.right(20)
        print('右转 20')
        draw_branch(branch_length-15)

        # 绘制左侧树枝
        turtle.left(40)
        print('左转 40')
        draw_branch(branch_length-15)

        #返回之前的树枝上
        print('右转 20')
        turtle.right(20)

        turtle.penup()
        turtle.backward(branch_length)
        turtle.pendown()

        print('向后',branch_length)

def main():
    '''
        主函数
    '''
    screen = turtle.Screen()
    screen.bgcolor("white")
    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.color('brown')
    print('左转 90')
    turtle.speed(5000)
    draw_branch(100);
    img = turtle.getscreen()
    img.getcanvas().postscript(file="out.eps")
    im=Image.open("out.eps")
    im.save("out.png")
# Close the turtle graphics window on click
    turtle.exitonclick()

if __name__ == '__main__':
    main()



