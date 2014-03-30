from ftplib import FTP


#addresse du serveur FTP (raspy)
host = "www.patoxa.com"
#Credentials pour la connexion :
user = "pi"
password = "cisco"

#FTP(host='', user='', passwd='', acct='', timeout=None, source_address=None)
#ftp = FTP(host, user, password)
ftp = FTP()
ftp.connect('www.patoxa.com',2121)
#login
ftp.login(user,password)
#affiche l'etat de la connection
print("Etat : ", ftp.getwelcome())
#Liste le dossier courrant du serveur FTP
print(ftp.retrlines('LIST'))