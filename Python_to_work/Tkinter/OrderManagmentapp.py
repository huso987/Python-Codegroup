import tkinter as tk
from tkinter import messagebox, Toplevel, Menu, Listbox, Scrollbar
from tkinter import ttk

class OrderManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sipariş Yönetim Sistemi")
        self.root.geometry("300x200")
        self.root.configure(bg='#f0f8ff')

        # login sayfasını başlatma
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.login_screen()

    def login_screen(self):
        tk.Label(self.root, text="Kullanıcı Adı", bg='#f0f8ff', font=('Helvetica', 12)).pack(pady=5)
        tk.Entry(self.root, textvariable=self.username, font=('Helvetica', 12)).pack(pady=5)
        tk.Label(self.root, text="Şifre", bg='#f0f8ff', font=('Helvetica', 12)).pack(pady=5)
        tk.Entry(self.root, textvariable=self.password, show="*", font=('Helvetica', 12)).pack(pady=5)
        tk.Button(self.root, text="Giriş", command=self.login, bg='#7fffd4', font=('Helvetica', 12)).pack(pady=20)

    def login(self):
        user = self.username.get()
        pwd = self.password.get()
        if user == "admin" and pwd == "sifre12":
            self.root.withdraw()
            self.dashboard()
        else:
            messagebox.showerror("Giriş Hatası", "Geçersiz kullanıcı adı veya şifre")

    def dashboard(self):
        dashboard = Toplevel(self.root)
        dashboard.title("Menü")
        dashboard.geometry("500x400")
        dashboard.configure(bg='#f5f5dc')

        menubar = Menu(dashboard)
        dashboard.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Menü", menu=file_menu)
        file_menu.add_command(label="Sipariş Ekle", command=self.add_order_screen)
        file_menu.add_command(label="Siparişleri Listele", command=self.list_orders_screen)
        file_menu.add_command(label="Siparişleri Sil", command=self.delete_order_screen)

        tk.Label(dashboard, text="Sipariş Yönetim Sistemi", bg='#f5f5dc', font=('Helvetica', 16)).pack(pady=20)
        tk.Button(dashboard, text="Sipariş Ekle", command=self.add_order_screen, bg='#7fffd4', font=('Helvetica', 14)).pack(pady=10)
        tk.Button(dashboard, text="Siparişleri Listele", command=self.list_orders_screen, bg='#7fffd4', font=('Helvetica', 14)).pack(pady=10)
        tk.Button(dashboard, text="Siparişleri Sil", command=self.delete_order_screen, bg='#7fffd4', font=('Helvetica', 14)).pack(pady=10)

    def add_order_screen(self):
        add_order_window = Toplevel(self.root)
        add_order_window.title("Sipariş Ekle")
        add_order_window.geometry("300x200")
        add_order_window.configure(bg='#ffe4e1')

        self.new_order = tk.StringVar()

        tk.Label(add_order_window, text="Sipariş Adı", bg='#ffe4e1', font=('Helvetica', 12)).pack(pady=5)
        tk.Entry(add_order_window, textvariable=self.new_order, font=('Helvetica', 12)).pack(pady=5)
        tk.Button(add_order_window, text="Ekle", command=self.add_order, bg='#7fffd4', font=('Helvetica', 12)).pack(pady=20)

    def add_order(self):
        order = self.new_order.get()
        if order:
            with open('orders.txt', 'a') as file:
                file.write(f"{order}\n")
            messagebox.showinfo("Başarılı", "Sipariş başarıyla eklendi")
        else:
            messagebox.showwarning("Girdi Hatası", "Lütfen sipariş adını giriniz")

    def list_orders_screen(self):
        list_orders_window = Toplevel(self.root)
        list_orders_window.title("Siparişleri Listele")
        list_orders_window.geometry("300x400")
        list_orders_window.configure(bg='#f5f5dc')

        scrollbar = Scrollbar(list_orders_window)
        scrollbar.pack(side="right", fill="y")

        listbox = Listbox(list_orders_window, yscrollcommand=scrollbar.set, font=('Helvetica', 12))
        listbox.pack(fill="both", expand=True)
        scrollbar.config(command=listbox.yview)

        with open('orders.txt', 'r') as file:
            orders = file.readlines()
            for order in orders:
                listbox.insert("end", order.strip())

    def delete_order_screen(self):
        delete_order_window = Toplevel(self.root)
        delete_order_window.title("Sipariş Sil")
        delete_order_window.geometry("300x400")
        delete_order_window.configure(bg='#ffa07a')

        self.listbox = Listbox(delete_order_window, font=('Helvetica', 12))
        self.listbox.pack(fill="both", expand=True)

        scrollbar = Scrollbar(self.listbox)
        scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        with open('orders.txt', 'r') as file:
            self.orders = file.readlines()
            for order in self.orders:
                self.listbox.insert("end", order.strip())

        tk.Button(delete_order_window, text="Sil", command=self.delete_order, bg='#ff6347', font=('Helvetica', 12)).pack(pady=10)

    def delete_order(self):
        selected = self.listbox.curselection()
        if selected:
            order_to_delete = self.listbox.get(selected[0])
            self.orders = [order for order in self.orders if order.strip() != order_to_delete]
            with open('orders.txt', 'w') as file:
                file.writelines(self.orders)
            messagebox.showinfo("Başarılı", "Sipariş başarıyla silindi")
            self.listbox.delete(selected[0])
        else:
            messagebox.showwarning("Seçim Hatası", "Lütfen silmek istediğiniz siparişi seçin")

if __name__ == "__main__":
    root = tk.Tk()
    app = OrderManagementApp(root)
    root.mainloop()
