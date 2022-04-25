#First import math modules to use sine and cosine functions
import math           

i = 0
#While loop is used to make a loop of each 15degree angles

while i <= 345:        
    sine = math.sin(math.radians(i))
    cosine = math.cos(math.radians(i))
    
    print("sin:", round(sine, 4),",", "Cos:", round(cosine, 4))
    i+= 15
