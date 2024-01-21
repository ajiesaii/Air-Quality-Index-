#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>
#include <NTPClient.h>
#include <WiFiUdp.h>

// Kredensial WiFi
const char* ssid = "";
const char* pass = "";

// Kredensial Firebase
const char* firebaseHost = "";
const char* firebaseAuth = "";

// Waktu
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org", 25200, 60000);

float CO2;
float CO;
String data;

void connectWiFi() {
  // Inisialisasi timeClient
  timeClient.begin();
  timeClient.update();
  
  Serial.print("Menghubungkan ke ");
  Serial.println(ssid);
  WiFi.begin(ssid, pass);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi terhubung");
}

void connectFirebase() {
  Firebase.begin(firebaseHost, firebaseAuth);
  Serial.println("Firebase terhubung");
}

void setup() {
  Serial.begin(4800);
  connectWiFi();
  connectFirebase();
}

void loop() {
  // Memperbarui waktu
  timeClient.update();
  Serial.print("WAKTU ");
  Serial.print(timeClient.getFormattedTime());

  // Membuat dokumen baru di Firebase
  String docPath = "/DATA/" + timeClient.getFormattedTime();
  Firebase.setString(docPath + "/waktu", timeClient.getFormattedTime());
  Firebase.setInt(docPath + "/CO", CO);
  Firebase.setInt(docPath + "/CO2", CO2);
  Firebase.setInt("CO", CO);
  Firebase.setInt("CO2",CO2);

  while(Serial.available()>0){
  data  = Serial.readStringUntil('\n');
  Serial.println(data);
  int comma = data.indexOf(",");
    if (comma != -1){
      CO = data.substring(0, comma).toFloat();
      CO2 = data.substring(comma+1).toFloat();
      Serial.print(CO);
      Serial.println(CO2);
    }
  }
  delay(20000);
}
