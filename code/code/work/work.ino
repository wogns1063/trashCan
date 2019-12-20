
#include <Servo.h>

 

Servo opener;

Servo bottom;

 

int cds = A0;

int pos1;

int pos2;

 

 

void setup() {

  Serial.begin(9600);

  

  opener.attach(9);

  opener.write(60);

  

  bottom.attach(6);

  bottom.write(0);

}

 

void loop() {

 

  String s = Serial.readStringUntil('\n');

 

  if( s == "opener on" ){  // OPENER ON

    for (pos1=60;pos1<=250;pos1+=1){

      opener.write(pos1);

      delay(1);

      }

    }

  

  if( s == "return" ){  // OPENER return

    for (pos1=250;pos1>=60;pos1-=1){

      opener.write(pos1);

      delay(1);

      }

    }    

   

  if( s == "liquid" ){  // liquid

    bottom.write(0);

    }

  

  if( s == "paper" ) {  // paper

    bottom.write(90);

    }

 

  if( s == "plastic" ){  // plastic

    bottom.write(180); 

    }

      

  while( s == "ReadCdsVal" ) {   // read of sensor value

    int val = analogRead(cds);

    Serial.println(val);

    delay(1);

    String s = Serial.readStringUntil('\n');

    

    if( s == "break" ) {

      break;

    } 

  }

}
