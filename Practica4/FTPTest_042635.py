from ftplib import FTP

ftp = FTP('192.168.1.1')  # connect to host, default port
ftp.login(user='rcp', passwd='rcp')                     # user anonymous, passwd anonymous@
ftp.retrlines('LIST')           # list directory contents

with open('archivorecibido.txt', 'wb') as fp:
    ftp.retrbinary('RETR archivo.txt', fp.write)
ftp.quit()

ftp = FTP('192.168.1.2')  # connect to host, default port
ftp.login(user='rcp', passwd='rcp')

file = open('archivorecibido.txt', 'w+')
contenido = file.read()
contenido = contenido + "cualquier cosa\nOtra linea\notra\nfrdthftgh"
file.write(contenido)
file.close()

ftp.storbinary('STOR archivo.txt', open('archivorecibido.txt', 'rb'))
print("Uploaded!")
ftp.quit()
