import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# Global veri yapıları
kitaplar = []
uyeler = []

# Fonksiyonlar
def kitap_ekle():
    """Yeni kitap ekleme fonksiyonu"""
    kitap_adi = entry_kitap_adi.get()
    yazar = entry_yazar.get()
    isbn = entry_isbn.get()
    adet = entry_adet.get()
    
    # Koşul yapısı - Boş alan kontrolü
    if kitap_adi == "" or yazar == "" or isbn == "" or adet == "":
        messagebox.showwarning("Uyarı", "Lütfen tüm alanları doldurun!")
        return
    
    # Koşul yapısı - Sayı kontrolü
    if not adet.isdigit():
        messagebox.showerror("Hata", "Adet sayı olmalıdır!")
        return
    
    # Sözlük veri yapısı kullanımı
    yeni_kitap = {
        "kitap_adi": kitap_adi,
        "yazar": yazar,
        "isbn": isbn,
        "adet": int(adet),
        "eklenme_tarihi": datetime.now().strftime("%d.%m.%Y")
    }
    
    # Liste veri yapısı - Kitap ekleme
    kitaplar.append(yeni_kitap)
    
    # Alanları temizle
    entry_kitap_adi.delete(0, tk.END)
    entry_yazar.delete(0, tk.END)
    entry_isbn.delete(0, tk.END)
    entry_adet.delete(0, tk.END)
    
    messagebox.showinfo("Başarılı", f"'{kitap_adi}' kitabı başarıyla eklendi!")
    kitaplari_listele()

def kitaplari_listele():
    """Tüm kitapları listbox'ta gösterme fonksiyonu"""
    # Önceki listeyi temizle
    listbox_kitaplar.delete(0, tk.END)
    
    # Döngü - Tüm kitapları ekrana yazdır
    for i in range(len(kitaplar)):
        kitap = kitaplar[i]
        liste_metni = f"{i+1}. {kitap['kitap_adi']} - {kitap['yazar']} (ISBN: {kitap['isbn']}) - Adet: {kitap['adet']}"
        listbox_kitaplar.insert(tk.END, liste_metni)

def kitap_sil():
    """Seçili kitabı silme fonksiyonu"""
    # Koşul yapısı - Seçim kontrolü
    if not listbox_kitaplar.curselection():
        messagebox.showwarning("Uyarı", "Lütfen silmek için bir kitap seçin!")
        return
    
    secilen_index = listbox_kitaplar.curselection()[0]
    kitap_adi = kitaplar[secilen_index]["kitap_adi"]
    
    # Onay mesajı
    cevap = messagebox.askyesno("Onay", f"'{kitap_adi}' kitabını silmek istediğinizden emin misiniz?")
    
    if cevap:
        kitaplar.pop(secilen_index)
        kitaplari_listele()
        messagebox.showinfo("Başarılı", "Kitap silindi!")

def kitap_ara():
    """Kitap arama fonksiyonu"""
    arama_metni = entry_arama.get().lower()
    
    if arama_metni == "":
        messagebox.showwarning("Uyarı", "Arama için bir metin girin!")
        return
    
    listbox_kitaplar.delete(0, tk.END)
    bulunan = 0
    
    # Döngü ve koşul yapısı - Arama işlemi
    for i in range(len(kitaplar)):
        kitap = kitaplar[i]
        # Operatörler - in operatörü kullanımı
        if arama_metni in kitap["kitap_adi"].lower() or arama_metni in kitap["yazar"].lower():
            liste_metni = f"{i+1}. {kitap['kitap_adi']} - {kitap['yazar']} (ISBN: {kitap['isbn']}) - Adet: {kitap['adet']}"
            listbox_kitaplar.insert(tk.END, liste_metni)
            bulunan += 1
    
    if bulunan == 0:
        messagebox.showinfo("Sonuç", "Aradığınız kriterlere uygun kitap bulunamadı!")
        kitaplari_listele()
    else:
        messagebox.showinfo("Sonuç", f"{bulunan} adet kitap bulundu!")

def tum_kitaplari_goster():
    """Tüm kitapları yeniden gösterme fonksiyonu"""
    entry_arama.delete(0, tk.END)
    kitaplari_listele()

def istatistik_goster():
    """Kütüphane istatistiklerini gösterme fonksiyonu"""
    toplam_kitap = len(kitaplar)
    toplam_adet = 0
    
    # Döngü - Toplam adet hesaplama
    for kitap in kitaplar:
        toplam_adet += kitap["adet"]
    
    # Koşul yapısı
    if toplam_kitap == 0:
        messagebox.showinfo("İstatistik", "Henüz kütüphanede kitap bulunmuyor!")
    else:
        mesaj = f"📊 KÜTÜPHANE İSTATİSTİKLERİ\n\n"
        mesaj += f"Toplam Kitap Türü: {toplam_kitap}\n"
        mesaj += f"Toplam Kitap Adedi: {toplam_adet}\n"
        mesaj += f"Ortalama Adet: {toplam_adet/toplam_kitap:.1f}"
        messagebox.showinfo("İstatistik", mesaj)

def kitap_detay_goster():
    """Seçili kitabın detaylarını gösterme fonksiyonu"""
    if not listbox_kitaplar.curselection():
        messagebox.showwarning("Uyarı", "Lütfen bir kitap seçin!")
        return
    
    secilen_index = listbox_kitaplar.curselection()[0]
    kitap = kitaplar[secilen_index]
    
    detay = f"📚 KİTAP DETAYLARI\n\n"
    detay += f"Kitap Adı: {kitap['kitap_adi']}\n"
    detay += f"Yazar: {kitap['yazar']}\n"
    detay += f"ISBN: {kitap['isbn']}\n"
    detay += f"Adet: {kitap['adet']}\n"
    detay += f"Eklenme Tarihi: {kitap['eklenme_tarihi']}"
    
    messagebox.showinfo("Kitap Detayı", detay)

# Ana pencere oluşturma
pencere = tk.Tk()
pencere.title("📚 Kütüphane Yönetim Sistemi")
pencere.geometry("900x600")
pencere.configure(bg="#f0f0f0")

# Başlık
baslik = tk.Label(pencere, text="🏛️ KÜTÜPHANE YÖNETİM SİSTEMİ", 
                  font=("Arial", 20, "bold"), bg="#2c3e50", fg="white", pady=15)
baslik.pack(fill=tk.X)

# Ana frame
ana_frame = tk.Frame(pencere, bg="#f0f0f0")
ana_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Sol panel - Kitap ekleme
sol_frame = tk.LabelFrame(ana_frame, text="📖 Kitap Ekle", font=("Arial", 12, "bold"),
                          bg="#ecf0f1", fg="#2c3e50", padx=10, pady=10)
sol_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

tk.Label(sol_frame, text="Kitap Adı:", bg="#ecf0f1", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
entry_kitap_adi = tk.Entry(sol_frame, width=25, font=("Arial", 10))
entry_kitap_adi.grid(row=0, column=1, pady=5)

tk.Label(sol_frame, text="Yazar:", bg="#ecf0f1", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
entry_yazar = tk.Entry(sol_frame, width=25, font=("Arial", 10))
entry_yazar.grid(row=1, column=1, pady=5)

tk.Label(sol_frame, text="ISBN:", bg="#ecf0f1", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
entry_isbn = tk.Entry(sol_frame, width=25, font=("Arial", 10))
entry_isbn.grid(row=2, column=1, pady=5)

tk.Label(sol_frame, text="Adet:", bg="#ecf0f1", font=("Arial", 10)).grid(row=3, column=0, sticky="w", pady=5)
entry_adet = tk.Entry(sol_frame, width=25, font=("Arial", 10))
entry_adet.grid(row=3, column=1, pady=5)

btn_ekle = tk.Button(sol_frame, text="➕ Kitap Ekle", command=kitap_ekle, 
                     bg="#27ae60", fg="white", font=("Arial", 10, "bold"), 
                     width=20, cursor="hand2")
btn_ekle.grid(row=4, column=0, columnspan=2, pady=10)

# Orta panel - Arama ve liste
orta_frame = tk.LabelFrame(ana_frame, text="📋 Kitap Listesi", font=("Arial", 12, "bold"),
                           bg="#ecf0f1", fg="#2c3e50", padx=10, pady=10)
orta_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

# Arama bölümü
arama_frame = tk.Frame(orta_frame, bg="#ecf0f1")
arama_frame.pack(fill=tk.X, pady=5)

tk.Label(arama_frame, text="🔍 Ara:", bg="#ecf0f1", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
entry_arama = tk.Entry(arama_frame, width=20, font=("Arial", 10))
entry_arama.pack(side=tk.LEFT, padx=5)

btn_ara = tk.Button(arama_frame, text="Ara", command=kitap_ara, 
                    bg="#3498db", fg="white", font=("Arial", 9), cursor="hand2")
btn_ara.pack(side=tk.LEFT, padx=2)

btn_tum_goster = tk.Button(arama_frame, text="Tümünü Göster", command=tum_kitaplari_goster,
                           bg="#95a5a6", fg="white", font=("Arial", 9), cursor="hand2")
btn_tum_goster.pack(side=tk.LEFT, padx=2)

# Listbox ve scrollbar
scrollbar = tk.Scrollbar(orta_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_kitaplar = tk.Listbox(orta_frame, width=50, height=15, 
                               font=("Courier", 9), yscrollcommand=scrollbar.set)
listbox_kitaplar.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox_kitaplar.yview)

# Sağ panel - İşlemler
sag_frame = tk.LabelFrame(ana_frame, text="⚙️ İşlemler", font=("Arial", 12, "bold"),
                          bg="#ecf0f1", fg="#2c3e50", padx=10, pady=10)
sag_frame.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

btn_detay = tk.Button(sag_frame, text="📄 Detay Göster", command=kitap_detay_goster,
                      bg="#3498db", fg="white", font=("Arial", 10), width=18, cursor="hand2")
btn_detay.pack(pady=5)

btn_sil = tk.Button(sag_frame, text="🗑️ Kitap Sil", command=kitap_sil,
                    bg="#e74c3c", fg="white", font=("Arial", 10), width=18, cursor="hand2")
btn_sil.pack(pady=5)

btn_istatistik = tk.Button(sag_frame, text="📊 İstatistikler", command=istatistik_goster,
                           bg="#9b59b6", fg="white", font=("Arial", 10), width=18, cursor="hand2")
btn_istatistik.pack(pady=5)

btn_cikis = tk.Button(sag_frame, text="❌ Çıkış", command=pencere.quit,
                      bg="#34495e", fg="white", font=("Arial", 10), width=18, cursor="hand2")
btn_cikis.pack(pady=5)

# Grid yapılandırması
ana_frame.grid_columnconfigure(1, weight=2)
ana_frame.grid_rowconfigure(0, weight=1)

# Alt bilgi
alt_bilgi = tk.Label(pencere, text="© 2024 - Lise Python Final Projesi", 
                     font=("Arial", 8), bg="#34495e", fg="white", pady=5)
alt_bilgi.pack(fill=tk.X, side=tk.BOTTOM)

# Örnek veri ekle
ornek_kitaplar = [
    {"kitap_adi": "Suç ve Ceza", "yazar": "Dostoyevski", "isbn": "978-0140449136", "adet": 3, "eklenme_tarihi": "01.01.2024"},
    {"kitap_adi": "1984", "yazar": "George Orwell", "isbn": "978-0451524935", "adet": 5, "eklenme_tarihi": "15.01.2024"},
    {"kitap_adi": "Simyacı", "yazar": "Paulo Coelho", "isbn": "978-0062315007", "adet": 2, "eklenme_tarihi": "20.02.2024"}
]

for kitap in ornek_kitaplar:
    kitaplar.append(kitap)

kitaplari_listele()

# Pencereyi başlat
pencere.mainloop()