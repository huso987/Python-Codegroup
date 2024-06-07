import tkinter as tk
from tkinter import messagebox, Toplevel, Menu, Listbox, Scrollbar

class BookManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kitap Yönetim Sitemi")
        self.root.geometry("300x200")

        # login sayfasını başlatma
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.login_screen()

    def login_screen(self):
        tk.Label(self.root, text="Username").pack(pady=5)
        tk.Entry(self.root, textvariable=self.username).pack(pady=5)
        tk.Label(self.root, text="Password").pack(pady=5)
        tk.Entry(self.root, textvariable=self.password, show="*").pack(pady=5)
        tk.Button(self.root, text="Login", command=self.login).pack(pady=20)

    def login(self):
        user = self.username.get()
        pwd = self.password.get()
        if user == "yönetici" and pwd == "12345":
            self.root.withdraw()
            self.dashboard()
        else:
            messagebox.showerror("Giriş Hatası", "Geçersiz kullanıcı adı veya şifre")

    def dashboard(self):
        dashboard = Toplevel(self.root)
        dashboard.title("Menü")
        dashboard.geometry("400x300")
        
        
        menubar = Menu(dashboard)
        dashboard.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Menü", menu=file_menu)
        file_menu.add_command(label="Kitap Ekle", command=self.add_record_screen)
        file_menu.add_command(label="Kitapları Listele", command=self.list_records_screen)
        file_menu.add_command(label="Kitapları Sil", command=self.delete_record_screen)
        

    def add_record_screen(self):
        add_record_window = Toplevel(self.root)
        add_record_window.title("Kayıt ekle")
        add_record_window.geometry("300x200")

        self.new_title = tk.StringVar()

        tk.Label(add_record_window, text="Kitap İsmi").pack(pady=5)
        tk.Entry(add_record_window, textvariable=self.new_title).pack(pady=5)
        tk.Button(add_record_window, text="Ekle", command=self.add_record).pack(pady=20)

    def add_record(self):
        title = self.new_title.get()
        if title:
            with open('data.txt', 'a') as file:
                file.write(f"{title}\n")
            messagebox.showinfo("Başarılı", "Kayıt başarılı")
        else:
            messagebox.showwarning("Girdi Hatası", "Lütfen kitap ismi giriniz")

    def list_records_screen(self):
        list_records_window = Toplevel(self.root)
        list_records_window.title("Kayıtları Listele")
        list_records_window.geometry("300x400")

        scrollbar = Scrollbar(list_records_window)
        scrollbar.pack(side="right", fill="y")

        listbox = Listbox(list_records_window, yscrollcommand=scrollbar.set)
        listbox.pack(fill="both", expand=True)
        scrollbar.config(command=listbox.yview)

        with open('data.txt', 'r') as file:
            records = file.readlines()
            for record in records:
                listbox.insert("end", record.strip())

    def delete_record_screen(self):
        delete_record_window = Toplevel(self.root)
        delete_record_window.title("Kaydı sil")
        delete_record_window.geometry("300x400")

        self.listbox = Listbox(delete_record_window)
        self.listbox.pack(fill="both", expand=True)

        scrollbar = Scrollbar(self.listbox)
        scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        with open('data.txt', 'r') as file:
            self.records = file.readlines()
            for record in self.records:
                self.listbox.insert("end", record.strip())

        tk.Button(delete_record_window, text="Delete", command=self.delete_record).pack(pady=10)

    def delete_record(self):
        selected = self.listbox.curselection()
        if selected:
            record_to_delete = self.listbox.get(selected[0])
            self.records = [record for record in self.records if record.strip() != record_to_delete]
            with open('data.txt', 'w') as file:
                file.writelines(self.records)
            messagebox.showinfo("Başarılı", "Kayıt Silme Başarılı")
            self.listbox.delete(selected[0])
        else:
            messagebox.showwarning("Seçim Yanlış", "Sileceğin Kitabı Seç")

if __name__ == "__main__":
    root = tk.Tk()
    app = BookManagementApp(root)
    root.mainloop()
