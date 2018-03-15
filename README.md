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
  
   1. Raspberry Pi
   2. Python
   3. Tensor Flow
   4. Keras
        
## Steps Taken
### 1. Build Car
   At the beggining, after watching Ryan Zotti's [talk](https://www.youtube.com/watch?v=QbbOxrR0zdA&t=3355s) at PyData conference I decided to buy a remote controlled car and try to connect it to the Raspberry Pi. I ordered one from Amazon but I accidentally broke it. After that I decided to build the car myself. I found this [tutorial](https://www.youtube.com/watch?v=LlFkybEQFFA) on youtube which I modified to fit my needs. Instead of using several AA batteries I used a single 9V battery and made my car with a protoboard and cardboard. But it helped me understand how you can intereact with motors via the Raspberry Pi.

<img src="https://github.com/edlgg/Self-driving-car/blob/master/images/README_images/20170605_223608.jpg" width="100" height="100">
<img src="ttps://github.com/edlgg/Self-driving-car/blob/master/images/README_images/20170607_205502.jpg" width="100" height="100">
<img src="https://github.com/edlgg/Self-driving-car/blob/master/images/README_images/20170616_201821.jpg" width="100" height="100">
<img src="https://github.com/edlgg/Self-driving-car/blob/master/images/README_images/20180310_194621.jpg" width="100" height="100">
 
### 2. Implement Car Movement
   Before starting this proyect I didnt know anything about the Raspberry Pi so I used [this Udemy course](https://www.udemy.com/from-0-to-1-raspberry-pi/learn/v4/overview) to learn how to use LED's, Proximity sensors, temperature sensors, etc. After I got used to the Pi I implemented the car movement. Since the GPIO pins on the PI are are digital (either 1 or 0) and sometimes I needed the motors to work at lower speeds I used pulse width modulation to more precisely control the movement of the car. PWM is when you decrease the duty cycle of the motor so it moves slower by turning it on and off very quickly in the proportions that you need. After that I just connected to my Pi via SSH to give the commands.
  I wasn't able to control the car using wasd controls via the command line because you had to press enter each time you issued a command. I found a library called Tkinter that allows you to use the wasd keys like if you where using a game but it required acces to the operating system's GUI. I used VNC to acces the Pi's GUI remotly from my laptop. After using it for a couple of minutes it looked like having to acces the GUI wasnt a good idea so I went back to SSH. I figured that sending one command at a time in 1 second intervals would be enough. It would make the machine learning easier to implement since it would make a prediction for a single photo in one second and not a constant video feed.
  The movement of the car is in the movement.py and car_movement.py files.
  
  ### 3. Implement Camera
   Using the propietary Pi's camera is very easy with all the libraries that are available. I just had to create some functions to fit my needs which are in the camera.py file. The functions are used to initialize the camera, take a picture of the correct size and shutting down the camera.
      
 ### 4. Create Machine Learning Model
   Learning about ML was the real goal behind building this proyect. I not only wanted to create a ML model but I also wanted to understand it. I took Andrew NG's machine learningn course and his deep learning specialization on coursera. The courses taught me a lot of theory about ML. In the courses I also learned to use Keras which allowed my to build a Neural Network with ease.  I used a simple NN that consisted of 3 layers. 2 convolutinal +  maxpooling layers and a fully connected layer.
   
```
def cModel(input_shape):

    X_input = Input(input_shape)

    # CONV -> BN -> RELU Block applied to X_input
    X = Conv2D(6, (6,6), strides=(1, 1), name='conv0', padding = 'same')(X_input)
    X = BatchNormalization(axis=3, name='bn0')(X)
    X = Activation('relu')(X)

    # MAXPOOL
    X = MaxPooling2D((2, 2), name='max_pool0')(X)

    # CONV -> BN -> RELU Block applied to X
    X = Conv2D(16, (5,5), strides=(1, 1), name='conv1', padding = 'valid')(X)
    X = BatchNormalization(axis=3, name='bn1')(X)
    X = Activation('relu')(X)

    # MAXPOOL
    X = MaxPooling2D((2, 2), name='max_pool1')(X)

    # CONV -> BN -> RELU Block applied to X
    X = Conv2D(8, (3, 3), strides=(1, 1), name='conv2', padding = 'valid')(X)
    X = BatchNormalization(axis=3, name='bn2')(X)
    X = Activation('relu')(X)

    # MAXPOOL
    X = MaxPooling2D((2, 2), name='max_pool2')(X)

    # FLATTEN X (means convert it to a vector) + FULLYCONNECTED
    X = Flatten()(X)
    X = Dense(units=4, activation='sigmoid', name='fc')(X)


    # Create model. This creates your Keras model instance, you'll use this instance to train/test the model.
    model = Model(inputs=X_input, outputs=X, name='cModel')

    return model


```
 ### 5. Gather Training Data
   To gather the test data I had to create 3 folder to create the 3 training classes forward(w), right(d) and left(a). For that I just took a picture and when I pressed the key for what the car should do the picture went to that folder and the car moved. All the code for that is in the car_train.py file.  I had a total of about 2500 images to train and test.
   Example train images:
   
   ![alt text](https://github.com/edlgg/Self-driving-car/blob/master/images/a/19-06-2017_01:10:32.jpg)
   ![alt text](https://github.com/edlgg/Self-driving-car/blob/master/images/w/12-03-2018_17:58:49.jpg)
   ![alt text](https://github.com/edlgg/Self-driving-car/blob/master/images/d/15-03-2018_12:46:29.jpg)
   
 ### 6. Train Model
 I tried different network architectures and hyper parameters. However they all seemed to work very well since its not a very complex problem. I ended up choosing the one that converged a bit faster. At the end the model was about 90% accurate on the training data and about 80% accurate on the test data. I think it was a good result since there are many images that could be classified into more than 1 category like a slight turn.
 
 ### 7. Test Car! 
   The car worked very well when I first tested. Every now and then it started to glitch and move randomly but that is mostly because of a bug in the camera which I wasnt able to fix. This is a video of the car in a track it had never seen before.
   

