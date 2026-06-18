import os, socket

HOST = os.getenv("MC_HOST", "dynamic-10.magmanode.com")
PORT = int(os.getenv("MC_PORT", "25768"))

print(f"Ping enviado para {HOST}:{PORT}", flush=True)

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    s.sendto(b'\x01\x00', (HOST, PORT))
    s.close()
    print("OK", flush=True)
except Exception as e:
    print(f"erro: {e}", flush=True)
