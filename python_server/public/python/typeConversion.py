import base64

def bytes_2_B64_string(bytes):
    byte_content = bytes.getvalue()
    base64_encoded = base64.b64encode(byte_content)
    base64_string = base64_encoded.decode('utf-8')

    return base64_string