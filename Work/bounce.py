# bounce.py
#
# Exercise 1.5


bounce_height = 100
num_bounces = 1

while num_bounces < 11:
    bounce_height = bounce_height * (3/5)
    num_bounces = num_bounces + 1
    print(num_bounces, bounce_height)