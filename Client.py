import socket


def get_operation_input():
    while True:
        op = input("pick operations (+, -, *, /): ")
        if op.strip() in ['+', '-', '*', '/']:
            return op.strip()
        else:
            print("Invalid symbol!")


def get_number_input(prompt):
    while True:
        number = input(prompt)
        if number.strip().replace('.', '').isdigit():
            return float(number.strip())
        else:
            print("first number invalid")


def send_expression(client_socket):
    while True:
        op = get_operation_input()
        client_socket.send(op.encode())

        a = get_number_input("pick first number: ")
        client_socket.send(str(a).encode())

        b = get_number_input("pick second number: ")
        client_socket.send(str(b).encode())

        result = client_socket.recv(1024).decode()
        print("Result:", result)

        while True:
            choice = input("wanna continue? (yes/no): ")
            if choice.lower() == 'yes' or choice.lower() == 'no':
                break
            else:
                print("Bruh, you should pick a correct answer")

        if choice.lower() != 'yes':
            break


def main():
    server_address = ('127.0.0.1', 10000)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(server_address)
    except ConnectionRefusedError:
        print("Server inactive")
        return

    send_expression(client_socket)

    client_socket.close()


if __name__ == "__main__":
    main()