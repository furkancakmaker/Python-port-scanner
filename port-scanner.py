import socket
import termcolor

# Bu fonksiyon, belirtilen hedef IP adresi ve taramak istenilen port sayısını alır
def scan(target, ports):
    print(f"\n Şunun için tarama başlatılıyor: {str(target)}")
    for port in range(1, ports): # 1'den kullanıcının girdiği porrt sayısına kadar tarama yapar
        scan_port(target, port) #  Her bir port için scan_port adında bir fonksiyon çağırılır

# Bu fonksiyon, belirtilen IP adresi ve port numarasını alır
def scan_port(ipAdress, port):
    # Belirtilen IP adresi ve port numarasına bağlanmayı dener
    try:
        sock = socket.socket() # Yeni bir socket oluşturulur
        sock.connect((ipAdress, port)) # Oluşturulan soket belirtilen IP adresine ve port numarasına bağlanmaya çalışır
        print(termcolor.colored((f"[+] Açık Port {str(port)}"), "green")) 
        sock.close() # soket kapatılır
    # Eğer bağlantı başarısız olursa, yani port kapalıysa veya başka bir hata oluşursa kapalı port yazar
    except:
        print(termcolor.colored((f"[-] Kapalı Port {str(port)}"), "red"))

targets = input("[*] Taranacak IP adresini girin (bunları virgül(,) ile bölün): ")
ports = int(input("[*] Taramak istediğiniz port sayısını girin: "))

# Birden fazla IP adresi girildiyse if bloğuna girer
if "," in targets:
    print(termcolor.colored(("\n[*] Birden çok hedefi tarama"), "blue"))
    for ip_adress in targets: # Her IP adresi için döngü başlatır
        scan(ip_adress.strip(" "), ports) # Her IP adresi scan fonksiyonuna gönderilir ancak IP adresi üzerindeki boşluklar strip ile silinir 
else: 
    scan(targets, ports) 