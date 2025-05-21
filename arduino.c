const int pinoLedVerde = 7;
const int pinoLedVermelho = 8;
const int pinoBuzzer = 9;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);  // Aguarda até 100ms por uma string completa

  pinMode(pinoLedVerde, OUTPUT);
  pinMode(pinoLedVermelho, OUTPUT);
  pinMode(pinoBuzzer, OUTPUT);

  digitalWrite(pinoLedVerde, LOW);
  digitalWrite(pinoLedVermelho, LOW);
  digitalWrite(pinoBuzzer, LOW);
}

void loop() {
  if (Serial.available()) {
    String comando = Serial.readStringUntil('\n');
    comando.trim(); // Remove \r, \n, espaços

  

    if (comando == "ALERTA") {
      digitalWrite(pinoLedVerde, LOW);
      digitalWrite(pinoLedVermelho, HIGH);
      digitalWrite(pinoBuzzer, HIGH);
    } else if (comando == "OK") {
      digitalWrite(pinoLedVerde, HIGH);
      digitalWrite(pinoLedVermelho, LOW);
      digitalWrite(pinoBuzzer, LOW);
    }
  }
}