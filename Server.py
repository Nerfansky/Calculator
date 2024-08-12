import socket


def handle_client(client_socket, address):
    while True:
        operation = client_socket.recv(1024).decode()
        if not operation:
            client_socket.close()
            break

        a = float(client_socket.recv(1024).decode())
        b = float(client_socket.recv(1024).decode())

        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            if b != 0:
                result = a / b
            else:
                result = "u can not divide for 0"
        else:
            result = "symbol invalid"

        client_socket.send(str(result).encode())


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 10000))
    server_socket.listen(5)

    print("Server started, waiting for clients...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}. You're connected.")
        handle_client(client_socket, address)


if __name__ == "__main__":
    main()
