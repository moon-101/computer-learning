import certifi
import 
with open(certifi.where(), 'r') as f:
    certs = f.read()
    print("ISRG Root X1 是否存在:", "ISRG ROOT X1" in certs.upper())
    print("证书文件路径:", certifi.where())
