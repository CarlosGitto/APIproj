import http.server
import socketserver
import sys



def http_run(args):
    
    """Provides a port (default or custom) and start the http server"""

    if len(args) == 1:
        port = 8888     
    elif len(args) == 2:
        try:

            port = int(sys.argv[-1])
        except:
            print("Bad port")
            return
    else:
        print("Bad sintax")
        return 

    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        print("Server started at localhost:" + str(port))
        httpd.serve_forever()

if __name__ == "__main__":
    arguments = sys.argv
    http_run(args=arguments)