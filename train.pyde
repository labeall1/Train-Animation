#Animation - Train
#Laura Beall
#February 10th, 2017

time = 0; #use time to move objects from one frame to next

def setup():
    size(800, 800, P3D) #3D shapes
    perspective(60 * PI / 180, 1, 0.1, 1000) #60 degree field of view
    #perspective(fov, aspect, zNear, zFar)
    
def draw():
    global time
    time += 0.01
    
    camera(0, 0, 100, 0, 0, 0, 0, 1, 0)
    
    background(255, 255, 255)
    
    #create a directional light source
    
    ambientLight(50, 50, 50) #Changes color of shapes?
    lightSpecular(255, 255, 255) #Creats the shiny spot on the shapes
    directionalLight(100, 100, 100, -0.3, 0.5, -1) #Where the light is shining and how much
    
    noStroke()
    specular(180, 180, 180) #How bright to shine light?
    shininess(15.0) #How shiny to make an object
    
    #---------------TRAIN---------------#
    pushMatrix()
    rotateY(time)
    #body
    body()
    smokeStack()
    #wheels
    bigWheel(-9.5, 3.7, 5)
    bigWheel(-9.5, 3.7, -5)
    #front left
    wheel(-21, 5, 5)
    #back left
    wheel(-16, 5, 5)
    #front right
    wheel(-21, 5, -5)
    #back right
    wheel(-16, 5, -5)
    #front
    front()
    car(0, 0, 255, 5, 0)
    car(0, 255, 0, 20, 15)
    car(255, 255, 0, 35, 30)
    popMatrix()
    #---------------TRAIN---------------#
    
def body():
    
    #train body
    fill(255, 0, 0)
    pushMatrix()
    translate(-15, 0, 0)
    #rotateY(time)
    box(20, 10, 10)
    popMatrix()
    
    #top of train body
    fill(255, 0, 0)
    pushMatrix()
    translate(-10, -8, 0)
    #rotateY(time)
    box(10, 6, 10)
    popMatrix()
    
    #maybe adjust z values
    window(-10, -7, 5)
    window(-10, -7, -5)
    
def window(x, y, z):
    fill(0, 0, 0)
    pushMatrix()
    translate(x, y, z)
    box(5, 5, .2)
    popMatrix()

#front of train
def front():
    fill(0, 255, 0)
    pushMatrix()
    translate(-25, 5, -1)
    triangularPrism()
    popMatrix()
    
    #green sphere
    fill(0, 0, 255)
    pushMatrix()
    translate(-25, -1, 0) #makes ball move up/down or "bounce"
    sphereDetail(60) #controls how many polygons are used ot make the sphere
    sphere(2.5)
    popMatrix()
    
#used to make the big wheels on the train
#same as wheels but scaled differently
def bigWheel(x, y, z):
    fill(169, 169, 169)
    pushMatrix()
    translate(x, y, z)
    rotateX(radians(180))
    #rotateY(time)
    scale(3.5, 3.5, .5)
    cylinder(64)
    popMatrix()
    
    #left wheels
    fill(0, 0, 0)
    pushMatrix()
    translate(x, y, z+.5)
    rotateX(radians(180))
    scale(1.5, 1.5, .2)
    cylinder(64)
    popMatrix()
    
    #right wheels
    fill(0, 0, 0)
    pushMatrix()
    translate(x, y, z-.5)
    rotateX(radians(180))
    scale(1.5, 1.5, .2)
    cylinder(64)
    popMatrix()
    
#make wheels of train
def wheel(x, y, z):    
    
    fill(169, 169, 169)
    pushMatrix()
    translate(x, y, z)
    rotateX(radians(180))
    #rotateY(time)
    scale(2, 2, .5)
    cylinder(64)
    popMatrix()
    
    #left wheels
    fill(0, 0, 0)
    pushMatrix()
    translate(x, y, z+.5)
    rotateX(radians(180))
    scale(.8, .8, .2)
    cylinder(64)
    popMatrix()
    
    #right wheels
    fill(0, 0, 0)
    pushMatrix()
    translate(x, y, z-.5)
    rotateX(radians(180))
    scale(.8, .8, .2)
    cylinder(64)
    popMatrix()
    
def car(r, g, b, x, x2):
    fill(r, g, b)
    pushMatrix()
    translate(x, 0, 0)
    #rotateY(time)
    box(10, 10, 10)
    popMatrix()
    
    #connector
    fill(105, 105, 105)
    pushMatrix()
    translate(x2, 3, 0)
    box(10, 1, 0)
    popMatrix()
    
    wheel(2.5 + x2, 5, 5)
    wheel(7.5 + x2, 5, 5)
    wheel(2.5 + x2, 5, -5)
    wheel(7.5 + x2, 5, -5)
    
def smokeStack():
    fill(0, 0, 0)
    pushMatrix()
    translate(-21, -7, 0)
    rotateX(radians(90))
    scale(2, 2, 2)
    cylinder(64)
    popMatrix()
    
    fill(255, 0, 0)
    pushMatrix()
    translate(-21, -9, 0)
    rotateX(radians(90))
    scale(2.3, 2.3, .3)
    cylinder(64)
    popMatrix()
    
    smoke(-21.7, -11, 0)
    smoke(-19.5, -12, 0)
    smoke(-22, -14, 0)

def smoke(x, y, z):
    fill(211, 211, 211)
    pushMatrix()
    translate(x, y, z)
    sphereDetail(60) 
    sphere(1)
    popMatrix()
    
#cylinder with radium = 1, z in range [-1, 1]
def cylinder(sides):
    #first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2* PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex(x, y, -1)
    endShape(CLOSE)
    
    #second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex(x, y, 1)
    endShape(CLOSE)
    
    #sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal(x1, y1, 0) #makes the shape smooth
        vertex(x1, y1, 1)
        vertex(x1, y1, -1)
        
        normal(x2, y2, 0) #makes the shape smooth
        vertex(x2, y2, -1)
        vertex(x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2

def triangularPrism():
    x1 = 0
    y1 = 0
    
    x2 = x1
    y2 = y1-5
    
    x3 = x1-5
    y3 = y1
    
    #makes layers of triangles
    i = 0;
    while (i < 2): #make i larger to increase size of triangle
        beginShape(TRIANGLES)
        vertex(x1, y1, i)
        vertex(x2, y2, i)
        vertex(x3, y3, i)
        endShape(CLOSE)
        i +=.01 #more layers 
        
    
    