/*
  DHT22 Temperature and humidity sensor
*/

/*
  Library import
*/

#include <DHT.h> //importing DHT sensor library
// constants
#define DHTPIN 2      // declaring location of Data-Pin on arduino board
#define DHTTYPE DHT22 // declaring the type of temp/pressure sensor
DHT dht = DHT(DHTPIN, DHTTYPE);

// creating variables
int chk;
float humidity;    // float used to store values for humidity
float temperature; // float used to store values for temperature

void setup()
{
  Serial.begin(9600);
  dht.begin();
}

void loop()
{
  delay(2000);

  // reading data
  humidity = dht.readHumidity();
  temperature = dht.readTemperature();

  // returning values
  // Serial.print("Humidity: ");
  // Serial.print("\b");
  Serial.print(humidity);
  Serial.print("% , ");
  // Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" °Celsius");
  Serial.print("\n");
  delay(1000); // 1000ms, or 1 sec
  // 3 second TOTAL delay when factoring in initial 2000ms delay
}

// C:\Users\ogrieco548\Pictures\Camera Roll\sketch_apr05a\sketch_apr05b\sketch_apr05b.ino:8:17: warning: extra tokens at end of #include directive
//#include <DHT.h>; //importing DHT sensor library
