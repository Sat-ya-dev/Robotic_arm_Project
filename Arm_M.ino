#include <Servo.h>

Servo myservo1;
Servo myservo2;

//actual vals of theta1 and theta2 generated from python code sent earlier
//float theta1[] = {142.1334866855322, 139.73669409977163, 137.45740523729745, 135.29662477627494, 133.27132554277912, 131.38333618307448, 129.64841793714547, 128.0692066200934, 126.66026447954954, 125.42565816394077, 125.03059198753455, 124.94359461643165, 125.16265635416008, 125.66447931739472, 126.4590517197303, 127.53849779534114, 128.9160654477667, 130.574492984206, 132.52703473598436, 128.5385421916289, 124.5262598664413, 120.4941819395668, 116.46071680475302, 112.4402698194902, 108.4682649541196, 104.56985708712142, 100.77561350730954, 97.1152031633315, 99.22884902160092, 101.61728106211896, 104.28552029528007, 107.21516625307073, 110.40197300948003, 113.81340945398185, 117.43455420810025, 121.22000575476314, 125.14718840136695};
//float theta2[] = {82.97896900468992, 82.85936017651932, 82.50120468310081, 81.90261048228044, 81.0646206868111, 79.98242107636514, 78.65718635104008, 77.08014531277426, 75.25126171359248, 73.15588338293308, 78.07326221661008, 82.60067023233577, 86.77886462103744, 90.65059782316679, 94.23026724229999, 97.5258670309475, 100.53784990965893, 103.28303758760438, 105.75199655278858, 107.93917865741487, 109.83887824057139, 111.43399868229727, 112.73478609481947, 113.72213526932083, 114.39358628364572, 114.73187683609686, 114.75514522819066, 114.44873413137974, 116.68384303486606, 118.68930925080313, 120.46213755044744, 121.98501105626413, 123.2523344153446, 124.24907513842317, 124.96964429220553, 125.40430414677797, 125.55006099359476};

//straight line - check
// float theta1[]={142.0, 140.0, 137.0, 135.0, 133.0, 131.0, 130.0, 128.0, 127.0};
// float theta2[]={83.0, 83.0, 83.0, 82.0, 81.0, 80.0, 79.0, 77.0, 75.0};

//new values after rounding off -> values in nt1 and nt2 in python code
int theta1[] = {142, 140, 137, 135, 133, 131, 130, 128, 127, 125, 125, 125, 125, 126, 126, 128, 129, 131, 133, 129, 125, 120, 116, 112, 108, 105, 101, 97, 99, 102, 104, 107, 110, 114, 117, 121, 125};
int theta2[] = {83, 83, 83, 82, 81, 80, 79, 77, 75, 73, 78, 83, 87, 91, 94, 98, 101, 103, 106, 108, 110, 111, 113, 114, 114, 115, 115, 114, 117, 119, 120, 122, 123, 124, 125, 125, 126};

void setup() {
  //signal from arduino to servos
  myservo1.attach(9);
  myservo2.attach(10);
  //initializing from start point
  myservo1.write(142);
  myservo2.write(83);
  delay(1000);
}

void loop(){
  for(int i=0; i<37; i++){
    myservo1.write(theta1[i]);
    myservo2.write(theta2[i]);
    delay(50);
    }
  for(int i=36;i>=0;i--){
    myservo1.write(theta1[i]);
    myservo2.write(theta2[i]);
    delay(50);
  }
  //second loop for retracing M from last points
}
