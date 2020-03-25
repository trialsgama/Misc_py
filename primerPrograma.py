from pwn import *
conn=remote('ftp.ubuntu.com',21)
conn.recvline()
conn.send(b'USER anonymous\r\n')
conn.recvuntil(b' ',drop=True)
conn.recvline()
conn.send(b'PASSWORD anonymous\r\n')
conn.recvuntil(b' ',drop=True)
conn.recvline()
conn.close()

wget http://xael.org/norman/python/python-nmap/pythonnmap-0.2.4.tar.gz-O nmap.tar.gz