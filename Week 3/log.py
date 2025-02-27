import datetime

def log_ekleme(mesaj):
    zaman = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    with open("log.txt","a",encoding="utf-8") as dosya:
        dosya.write(f"{zaman} - {mesaj}")
    
    print("Log başarılı bir şekilde kaydedildi.")

log_ekleme("Sisteme giriş yapıldı.")