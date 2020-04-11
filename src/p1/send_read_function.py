import struct

def socket_send( s, text ):
    #print("SEND len: {} text: {}".format(len(text), text), flush=True)
    text = text.encode('utf-8')
    Lb = struct.pack('>i', len(text))
    s.send( Lb )
    s.send(text)

def socket_read( s ):
    Lb = b''
    while len(Lb) < 4:
        Lb += s.recv(1)

    L = struct.unpack('>i', Lb)[0]
    text = b''
    while len(text) < L:
        text += s.recv(1)

    #print("READ len: {} text: {}".format(L, text.decode('utf-8')), flush=True)
    return text.decode('utf-8')
