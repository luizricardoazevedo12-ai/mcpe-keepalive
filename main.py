import socket
import struct
import time
import os

HOST = os.getenv("MC_HOST", "dynamic-10.magmanode.com")
PORT = int(os.getenv("MC_PORT", "25768"))

MAGIC = b"\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78"

def ping():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)
        packet = b"\x01" + struct.pack(">Q", int(time.time()*1000)) + MAGIC + struct.pack(">Q", 12345)
        sock.sendto(packet, (HOST, PORT))
        sock.close()
        print(f"[{time.strftime('%H:%M:%S')}] Ping enviado para {HOST}:{PORT}")
    except Exception as e:
        print("Erro:", e)

if __name__ == "__main__":
    print("Keepalive 0.15.10 iniciado - modo free Fly.io")
    while True:
        ping()
        time.sleep(60)  # a cada 1 minuto
