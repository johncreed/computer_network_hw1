import struct
from socket import *
from time import sleep

def read_byte( s ):
    text = s.recv(1)
    if text == b'':
        raise IOError
    return text

def parse_header( headers ):
    tokens = headers.strip().split('\r\n')
    result = {}
    for t in tokens:
        name, value = t.split(':', maxsplit=1)
        result[name] = value.strip()
    return result

def parse_status_line(status_line):
    tokens = status_line.strip().split()
    result = {}
    result['version'] = tokens[0]
    result['code'] = int(tokens[1])
    result['phrase'] = tokens[2]
    return result

def parse_request_line(request_line):
    tokens = request_line.strip().split()
    result = {}
    result['method'] = tokens[0]
    result['url'] = tokens[1]
    result['version'] = tokens[2]
    return result

def read_headers_body( s ):
    # Read Headers
    headers = b''
    while headers.rfind(b'\r\n\r\n') == -1:
        headers += read_byte(s)
    #print(headers)
    headers_dict = parse_header( headers.decode() )

    # Read body entity
    body = b''
    if( "Content-Length" in headers_dict.keys() ):
        L = int(headers_dict["Content-Length"])
        while len(body) < L:
            body += read_byte(s)
    #print(body)

    return (headers_dict,  body.decode())

def respond_read( s ):
    # Read status line
    status_line = b''
    while status_line.rfind(b'\r\n') == -1:
        status_line += s.recv(1)
    status_dict = parse_status_line(status_line.decode())

    headers_dict, body =  read_headers_body(s)

    return (status_dict, headers_dict, body)

def request_read( s ):
    # Read request line
    request_line = b''
    while request_line.rfind(b'\r\n') == -1:
        request_line += read_byte(s)
    request_dict = parse_request_line(request_line.decode())

    headers_dict, body =  read_headers_body(s)

    return (request_dict, headers_dict,  body)
