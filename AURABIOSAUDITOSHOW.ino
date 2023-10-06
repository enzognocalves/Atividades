#include <dht11.h>
#define DHT11PIN 4
#include <Servo.h> //INCLUSÃO DA BIBLIOTECA NECESSÁRIA
 
const int pinoServo = 6; //PINO DIGITAL UTILIZADO PELO SERVO  
 
Servo s; //OBJETO DO TIPO SERVO
int pos; //POSIÇÃO DO SERVO

dht11 DHT11;

void setup()
{
  Serial.begin(9600);
   s.attach(pinoServo); //ASSOCIAÇÃO DO PINO DIGITAL AO OBJETO DO TIPO SERVO
  s.write(0); //INICIA O MOTOR NA POSIÇÃO 0º

}
void loop()
{
  Serial.println();

  int chk = DHT11.read(DHT11PIN);

  Serial.print("Humidity (%): ");
  Serial.println((float)DHT11.humidity, 2);

  Serial.print("Temperature (C): ");
  Serial.println((float)DHT11.temperature, 2);
  delay(2000);

 if (DHT11.humidity < 85){
    for(pos = 0; pos < 180; pos++){
      s.write(pos); 
      delay(15); 
    }
      delay(1000); 
  
    for(pos = 180; pos >= 0; pos--){
      s.write(pos);
      delay(15); 
    }
 }
 
}
