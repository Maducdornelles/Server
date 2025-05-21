import serial
import socket
import threading


porta_serial = '/dev/ttyAC0' 
baud_rate = 9600


arduino = serial.Serial(porta_serial, baud_rate, timeout=1)


HOST = '0.0.0.0'
PORT = 8080

def lidar_com_cliente(conexao, endereco):
    print(f"[RPi2] Conexão estabelecida com {endereco}")
    try:
        while True:
            dados = conexao.recv(1024).decode('utf-8').strip()
            if dados:
                print(f"[RPi2] Recebido: {dados}")
                if "STATUS:ALERTA" in dados:
                    arduino.write(b"ALERTA\n")
                elif "STATUS:OK" in dados:
                    arduino.write(b"OK\n")
    except:
        print(f"[RPi2] Conexão encerrada com {endereco}")
    finally:
        conexao.close()


servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind((HOST, PORT))
servidor_socket.listen()
print(f"[RPi2] Servidor TCP iniciado em {HOST}:{PORT}")

try:
    while True:
        conexao, endereco = servidor_socket.accept()
        thread = threading.Thread(target=lidar_com_cliente, args=(conexao, endereco))
        thread.start()
except KeyboardInterrupt:
    print("\n[RPi2] Encerrando servidor.")
finally:
    arduino.close()
    servidor_socket.close()
