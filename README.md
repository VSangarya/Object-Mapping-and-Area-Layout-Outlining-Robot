# Object-Mapping-and-Area-Layout-Outlining-Robot
<br/>
A Robot designed to trace the outline of an area using Ultrasonic sensors while detecting and avoiding objects in its path, and labeling the object in the final dimension layout outline using the OpenCV library and TensorFlow Lite.<br/>

A robot which uses a Raspberry Pi as the onboard computer. Components used : Raspberry Pi 3, L298N Motor Driver, 3 HC-SR04 Ultrasonic senors, 2 Standard 12v DC Motors, a USB Webcam, a power bank and an external power supply.<br/>

"RemoteConnect_turtle.py" is to establish remote connection with the Pi, execute main.py and to trace the layout of the room using Turtle and Tkinter<br/>
"robot_main.py" is the main code to be executed in the Raspberry Pi <br/>
"ImageClassify.py" makes use of OpenCV along with TensorFlow Lite to label the object in the captured image.<br/>

Pin connections also illustrated in this repository. Will be updating with the whole system's architectural diagram as well.




