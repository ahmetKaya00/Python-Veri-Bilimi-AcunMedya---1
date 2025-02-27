import os
if os.path.exists("ornek.txt"):
    os.remove("ornek.txt")
    print("Dosya silindi!")
else:
    print("Dosya bulunamadı!")