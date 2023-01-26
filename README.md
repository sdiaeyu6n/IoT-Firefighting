
# IoT Farm Fire Fighting System using Simplified Data Transmission with UAV and LoRa
### team member
> Sieun Choi, *Information & Communication Engineering, Dongguk Univ*

> Youngseo Kang, *Computer Science & Engineering, Dongguk Univ*

> Hyoungjoo Lee, *Computer Engineering, Dankook Univ*

> Yunji Kim, *Information & Communication Engineering, Dongguk Univ*

> Jiawei Chang, *Computer & Information Technology, Purdue Univ*

> Jason Su, *Computer & Information Technology, Purdue Univ*

> Ricardo Gonzalez, *Computer & Information Technology, Purdue Univ*

> Shixuan Mao, *Computer & Information Technology, Purdue Univ*


## 1. Research problem statement
In existing researches, fire is detected using image data. 
but in this case, the amount of data to be processed increases and the fire cannot be prevented in the early stages due to time.

## 2. Research novelty (Significance)
This research detects fires with small data and reduces the amount of data that can finally be processed.
  
## 3. Overview
![figure 1](https://user-images.githubusercontent.com/68414594/144302050-4656850d-4f77-4e0d-8462-fbc862e132fd.PNG)
  
## 4. Environment settings
####  a. experimental field : 
+ consists of a square with side lengths of 48 inches, a grid of 4 by 4 lines on the field.

<img src="https://user-images.githubusercontent.com/89725142/144628195-fc2ad780-6401-4755-a8f6-3f600e693424.png" width="400" height="400"/>

    
####  b. sensor board :
+ equipped in each corner
+ connected to the Arduino to detect fire attached to sensor towers
+ using Arduino MKR WAN 1310 supported by LoRa 
+ Developing Environment : Windows / Arduino IDE 1.8.16 with LoRa Library

<img src="https://user-images.githubusercontent.com/68414594/144308588-edb7ac0f-7d64-4aa5-9165-37f7388f78fe.png" width="400" height="400"/>


####  c. concentrator : 
+ Arduino MKR WAN 1310 supported by LoRa
+ Raspberry Pi 4 Model B
+ Developing Environment : Windows / Arduino IDE 1.8.16

####  d. UAV : 
+ Kiwi Drone (CL2HD2) : Based on Arduino Leonardo board
+ Developing Environment : Mac OS / Arduino IDE 1.8.16

<img src="https://user-images.githubusercontent.com/68414594/144305586-d5d5479a-babf-45ba-a8cf-81c4f6e18db8.png" width="400" height="350"/>


####  e. IR camera : 
+ Waveshare MLX90640-D110 IR Array Thermal Imaging Camera
+ Raspberry Pi 4 Model B
+ Python3 with Thonny

####  f. motor : 
+ SG90 Micro Servo Motor (9g)

####  g. IoT platform for reporting : 
+ NodeRED

## 5. Animation for the Process Description

![Process animation_(With CV)](https://user-images.githubusercontent.com/89725142/214887602-5e50036c-8be1-4474-b1e2-1d1d64a0dfef.gif)
