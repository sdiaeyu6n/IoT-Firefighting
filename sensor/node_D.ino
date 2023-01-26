//----------------------------------------------------//
//----------- Sensor Board Node D code ---------------//
//-------------------------------------- team <beep> -//
//-------------------------------------- 2021-12-01 --//
//----------------------------------------------------//


#include <SPI.h>
#include <LoRa.h>

//packet sending count
int counter = 0;

// analog value
int state1 = 0;
int state2 = 0;
int state3 = 0;
int state4 = 0;

// detection value
bool range1 = false;
bool range2 = false;
bool range3 = false;
bool range4 = false;

int sensorMin = 0;
int sensorMax = 1024;

//node name
char node_name = 'D';

void setup() {
  Serial.begin(9600);
  while (!Serial);
  //start communication
  Serial.println("LoRa Sender");
  if (!LoRa.begin(915E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() {
  //initialized
  range1 = false;
  range2 = false;
  range3 = false;
  range4 = false;

  // get analog signal at pin A1 ~ A4
  state1 = analogRead(A1);
  state2 = analogRead(A2);
  state3 = analogRead(A3);
  state4 = analogRead(A4);

  // divide the analog value into four parts ( 0 ~ 3 )
  range1 = map(state1, sensorMin, sensorMax, 0, 3);   // sensor set1
  range2 = map(state2, sensorMin, sensorMax, 0, 3);   // sensor set2
  range3 = map(state3, sensorMin, sensorMax, 0, 3);   // sensor set3
  range4 = map(state4, sensorMin, sensorMax, 0, 3);   // sensor set4

  // value 0 : close to fire
  //If detecting any of the four sensors,
  //Send a node_name data packet.
  if(range1 * range2 * range3 * range4 == 0 ){
    Serial.print("D: ");
    Serial.println(counter);
    // send packet
    LoRa.beginPacket();
    LoRa.print(node_name);
    LoRa.print(counter);
    LoRa.endPacket();
    counter++;
   }
   delay(500);
}