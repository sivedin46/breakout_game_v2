Game has 6 speeds and 3 levels. Each level it adds new brick row to top.
It also saves record and has sounds for paddle and brick collision.
Paddle has 3 parts and bounce of x direction changes due to ball coming direction and collision part of paddle.
it detects which side of brick collide with ball and due to this ball's bounce of x and y changes
Player has 3 lives.
Every color of bricks has different points
----------------------------------------
main.py----->
first it creates, initializes screen and all player needs
time_start = time.time()-----it uses to measure  seconds for increasing game speed
temp_ball_x = ball.move() it uses this for analyzing ball coming direction in ball.detect_paddle(). difference
between new xcor and old xcor tells us where the ball coming towards to paddle(right or left). so with this info
 and collision part of paddle info we can change bounce of ball behaviour.
 -----------------------------------------
 bricks.py-------->
 we have two method and a bricks[] list.
 we create new brick for given row. for first level row=4 and for other levels we add +1 to row
 when ball collides a brick with delete_Brick we delete it from our bricks list and from screen
 -------------------------------
ball.py------>
here we detect collision with bricks. paddle and other methods for ball.
It detects which side of brick collide with ball
it detects which part of paddle collide with ball and ball's coming direction
----------------------------
paddle---->
we create 3 paddles(left,center and right) and control their move and speed
--------------------------
scoreboard------> everything that showed for user is created and updated here


