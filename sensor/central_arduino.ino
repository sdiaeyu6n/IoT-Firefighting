//----------------------------------------------------//
//------------ Central Arduino code ------------------//
//-------------------------------------- team <beep> -//
//-------------------------------------- 2021-12-01 --//
//----------------------------------------------------//

#include <SPI.h>
#include <LoRa.h>

// packet count valables
int A = 0;
int B = 0;
int C = 0;
int D = 0;

// get packets until 10 second
int delay_time = 100000; 

// recieve sensor boards packet function
void recieve_packet(){
  
  
  int t = 10000;
  while(t-->0){
    int packetSize = LoRa.parsePacket();      // try to parse packet
    char node_name;
    if (packetSize) {
                                              // received a packet
      Serial.print("Received packet '");
                                              // read packet
      while (LoRa.available()) {              // LoRa 통신이 가능할 때
        node_name = (char)LoRa.read();        // LoRa 내장함수를 사용해서 문자 값을 저장
        Serial.print(node_name);              // 해당 값을 시리얼 모니터로 확인
        if(node_name == 'A'){ A++; }          // count packet 몇번 감지했는지 기록
        else if(node_name == 'B'){ B++; }     //
        else if(node_name == 'C'){ C++; }
        else if(node_name == 'D'){ D++; }
      }
                                              // print RSSI of packet
      Serial.print("' with RSSI ");
      Serial.println(LoRa.packetRssi());
    }
  }
}

void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("LoRa Receiver");

  if (!LoRa.begin(915E6)) {
    Serial.println("Starting LoRa failed!");
  }
}

void loop() {
  
  recieve_packet();                           // count packet fuction activate
  
  Serial.println("결과");                      // print result in serial moniter
  Serial.print("A:");Serial.println(A);              
  Serial.print("B:");Serial.println(B);
  Serial.print("C:");Serial.println(C);
  Serial.print("D:");Serial.println(D);

                                                    
  //정해진 값에 따른 경우의 수 결정
  int result = 0;
  if( A == 0 ){
    if( B == 0 ){
      if( C == 0 ){
        if ( D != 0 ){ result = 8; }            // D  ( part 8 )
      }
      else {// C != 0
        if ( D == 0 ) {result = 6;}             // C  ( part 6 )
        else {result = 7;}                      // CD ( part 7 ) 
      }
    }
    else{
      if ( D == 0 ) {result = 3;}               // B  ( part 3 )
      else { result = 5;}                       // BD ( part 5 )
    }
  }
  else {
    if( B == 0 ) {
      if( C == 0 ){ result = 1;}                // A  ( part 1 ) 
      else { result = 4; }                      // AC ( part 4 )
    }
    else { result = 2; }                        // AB ( part 2 )
  }
 
  delay(100);                                   // delay for next fire 
  A = 0; B = 0; C = 0; D = 0;                   // initialize varibles to zero
   
}