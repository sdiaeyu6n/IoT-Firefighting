# IR camera: Waveshare MLX90640 IR Array Thermal Imaging Camera
import time
import board
import busio
import math
import adafruit_mlx90640

# Motor: Micro Servo SG90 (9g)
import RPi.GPIO as GPIO # use RPi.GPIO library as GPIO

# IR camera setting
i2c = busio.I2C(board.SCL, board.SDA, frequency=800000)
mlx = adafruit_mlx90640.MLX90640(i2c)
print("MLX addr detected on I2C", [hex(i) for i in mlx.serial_number])
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

# Motor setting
servoPin          = 18
SERVO_MAX_DUTY    = 12   # duty for max degree(180 degree)
SERVO_MIN_DUTY    = 3    # duty for min degree(0 degree)

GPIO.setmode(GPIO.BCM) 
GPIO.setup(servoPin, GPIO.OUT)
servo = GPIO.PWM(servoPin, 50)  # set servo pin as PWM mode, 50Hz (50Hz > 20ms)
servo.start(0)  # servo PWM starting duty = 0 (if duty==0, servo not work)

#### Motor program ####

def setServoPos(degree):
  # max degree = 180 degree
    if degree > 180:
        degree = 180

  # calculate duty from degree
    duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)

  # apply duty value to servo PWM
    servo.ChangeDutyCycle(duty)

#### IR camera program ####

frame = [0] * 768

x_drone=16	# X coordinate of the drone's location : fixed
y_drone=12	# Y coordinate of the drone's location : fixed

count=0 # number of all case
detect_count=0 # number of fire detected case
no_detect_count=0 # number of no fire detected case

time.sleep(3)

while True:
    count+=1
    graph = [[0 for i in range(32)] for _ in range(24)] # graph size = IR cam frame size
    x_Coor = [] # fire x coordinate list
    y_Coor = [] # fire y coordinate list

    try:
        mlx.getFrame(frame)
    except ValueError:
        continue # retry

    for h in range(24):
        for w in range(32):
            t = int(frame[h*32 + w]) # IR value
            if t > 50: # if t>50, fire 
                t = '██' # fire symbol
                y_Coor.append(h) # add to fire x coordinate list
                x_Coor.append(31-w) # add to fire y coordinate list
            graph[h][31-w] = t 
            
    
    # drone location(x_drone, y_drone) = graph[12][16] -> fixed
    graph[12][16]='▓▓' # drone location symbol -> fixed
    
    num = len(x_Coor) # = len(y_Coor): num of fire pixels

    # fire detected
    try: 
        x_avg = sum(x_Coor) // num # average x coordinate of fire pixels
        y_avg = sum(y_Coor) // num # average y coordinate of fire pixels
        
        graph[y_avg][x_avg] = "░░" # symbol for average coordinate of fire values 
        
        
        # set drone location(x_drone, y_drone) as (0,0)
        # distance is calculated by subtracting fire average coordinate from drone location
        # moving downwards/backwards = minus
        # moving upwards/forwards = plus
        
        # if drone location is (1,6) and fire average coordinate is (4,2), next movement is (3,-4)
        
        x_move = x_avg - x_drone # next x movement of drone 
        y_move = -(y_avg - y_drone) # next y movement of drone 
        z_move = 0 # altitude of drone. Initial value is 0. 
									 # If altitude change needed, value is +k or -k (when k is constant value)
        
        avrg_coor = [x_avg, y_avg] # average coordinate of fire pixels
        next_move = [x_move, y_move, z_move] # next movement of drone
    
    # fire not detected - altitude change needed
    except:
        print("**************************** fire not detected ****************************")
        no_detect_count+=1
        next_move = [0,0,3] # set k=+3. drone has to go higher to capture more pixels(wider view)
        
        if no_detect_count > 4: # not problem of altitude. Sensor error
            print("!!!!! Sensor Error !!!!!")
            break # escape loop(quit program)
        else:
            time.sleep(1)
            print(str(no_detect_count)+") Next Movement = " + str(next_move))
            print()
            continue

    detect_count+=1 #number of fire detected cases
    
    for i in range(24):
        for j in range(32):
            print(graph[i][j], end=" ")
        print()

    if (0 <= abs(x_move) < 6) and (0 <= abs(y_move) < 6):
        detect_count+=1
        print()
        print("------------------------------ Drop the ball ------------------------------")
        print()

        time.sleep(2) # wait until drone go right above fire
        # open box to drop ball
        setServoPos(0) # servo 0 degree
        print("Dropping - box opening")
        time.sleep(2) # wait 2s
        # close box
        setServoPos(180) 
        print("Finished - box closing")
        time.sleep(2) # wait 2s
      # stop servo PWM
        servo.stop()
      # reset GPIO mode
        #GPIO.cleanup()
        break
    
    if detect_count > 1: # if fire not detected at first capture, altitude change needed 
        next_move[2] = -3 # lower altitude(drone go downwards)

    print()
    print("Center of Fire = " + str(avrg_coor))
    print(str(detect_count)+") Next Movement = " + str(next_move))
    print()
    
    time.sleep(3)