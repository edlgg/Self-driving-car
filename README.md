## Project in Progress
# self-driving-car
 
## Introduction
  For the first month of my summer vacations I wanted to do a small project to learn about machine learning. I came upon some videos of people making their own self driving cars. I decided that I would make my own self driving car eventough I had almost no knowledge of electronics, machine learning, tensor flow, python, etc.
 
  I built the car myself from scratch. I bought some motors, a raspberry pi, a camera, and a bunch of other things. I combined youtube, udemy, and other sources to learn about the different parts of the project. I divided the project into the following steps to make it easier to handle in my head. 
        
   1. Build car
   2. Implement car movement
   3. Implement camera
   4. Create machine learning model
   5. Gather training data
   6. Train model
   7. Test car!
  
  The technologies and tools used were:
  
   1.Raspberry Pi
   2.Python
   3.Tensor Flow
        
## Steps Taken
### 1. Build Car
   At the beggining, after watching Ryan Zotti's [talk](https://www.youtube.com/watch?v=QbbOxrR0zdA&t=3355s) at PyData conference I decided to buy a remote controlled car and try to connect it to the Raspberry Pi. I ordered one from Amazon but I accidentally broke it. After that I decided to build the car myself. I found this [tutorial](https://www.youtube.com/watch?v=LlFkybEQFFA) on youtube which I modified to fit my needs. Instead of using several AA batteries I used a single 9V battery and made my car with a protoboard and cardboard. But it helped me understand how you can intereact with motors via the Raspberry Pi.
 
### 2. Implement Car Movement
   Before starting this proyect I didnt know anything about the Raspberry Pi so I used [this Udemy course](https://www.udemy.com/from-0-to-1-raspberry-pi/learn/v4/overview) to learn how to use LED's, Proximity sensors, temperature sensors, etc. After I got used to the Pi I implemented the car movement. Since the GPIO pins on the PI are are digital (either 1 or 0) and sometimes I needed the motors to work at lower speeds I used pulse width modulation to more precisely control the movement of the car. PWM is when you decrease the duty cycle of the motor so it moves slower by turning it on and off very quickly in the proportions that you need. After that I just connected to my Pi via SSH to give the commands.
  I wasn't able to control the car using wasd controls via the command line because you had to press enter each time you issued a command. I found a library called Tkinter that allows you to use the wasd keys like if you where using a game but it required acces to the operating system's GUI. I used VNC to acces the Pi's GUI remotly from my laptop. After using it for a couple of minutes it looked like having to acces the GUI wasnt a good idea so I went back to SSH. I figured that sending one command at a time in 1 second intervals would be enough. It would make the machine learning easier to implement since it would make a prediction for a single photo in one second and not a constant video feed.
  The movement of the car is in the movement.py and car_movement.py files.
  
  ### 3. Implement Camera
   Using the propietary Pi's camera is very easy with all the libraries it that are available. I just had to create some functions to fit my needs which are in the camera.py file. The functions are used to initialize the camera, take a picture of the correct size and shutting down the camera.
      
 ### 4. Create Machine Learning Model
   After a lot of research, reading and video watching I used [this tutorial](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0) called TensorFlow for poets. It is made by google employees that work in TensorFlow. To train the model quickly I used a method called transfer learning in which you take a model that has already been trained and you retrain it to solve your particular problem.
 ### 5. Gather Training Data
   To gather the test data I had to create 3 folder to create the 3 training classes forward(w), right(d) and left(a). For that I just took a picture and when I pressed the key for what the car should do the picture went to that folder and the car moved. All the code for that is in the car_train.py file.
 ### 6. Train Model
 ### 7. Test Car! 
   When I first tested my model on the Raspberry Pi it took about 6 seconds to classify an image. It was too much since making a decicion each 6 seconds would allow the car to drive itself. I figured that in order to get the car working I had to get it under 2 seconds. After searching for a little bit I found this [thread](https://github.com/samjabrahams/tensorflow-on-raspberry-pi/issues/54) which explains how making a prediction can be very slow if you start a tensorflow session each time you need to make a prediction since setting everything up to make a prediction takes time. I chaged the car code to be inside the TensorFlow code and not the other way around. That reduce the time it takes to make a prediction from 6 seconds to about 1.6 which is less than the 2 seconds I wanted. 
      


