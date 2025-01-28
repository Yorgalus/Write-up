import socket
import math
import re

def main():
    host = "challenge01.root-me.org"
    port = 52002

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            
            data = s.recv(1024).decode()
            print("Reçu:\n", data)


            match = re.search(r"square root of (\d+) and multiply by (\d+)", data)
            if not match:
                print("Impossible de trouver les deux nombres dans le message reçu !")
                return

            n1 = float(match.group(1))  
            n2 = float(match.group(2))  
            print(f"Nombre 1 (racine): {n1}, Nombre 2 (multiplicateur): {n2}")

            result = math.sqrt(n1) * n2
            result = f"{result:.2f}"
            print("Résultat calculé :", result)

            s.sendall(f"{result}\n".encode())
            print("Réponse envoyée:", result)


            response = s.recv(1024).decode()
            print("Réponse du serveur:", response)

    except Exception as e:
        print("Erreur:", e)

if __name__ == "__main__":
    main()
