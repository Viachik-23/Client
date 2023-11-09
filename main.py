import tkinter as tk
import socket
from threading import Thread

clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def window_id():
    def get_ip():
        ip = entry.get()
        print(ip)
        clients.connect((ip, 2908))
        window.destroy()

    window = tk.Tk()

    label = tk.Label(window, text="Введите IP:")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()

    button = tk.Button(window, text="Далее", command=get_ip)
    button.pack()

    window.mainloop()
def button():
    def send_telegram():
        clients.send("telegram".encode("utf-8"))
        print("telegram")

    window1 = tk.Tk()

    button = tk.Button(window1, text="Telegram", command=send_telegram)
    button.pack()

    window1.mainloop()

Thread(target=window_id()).start()
Thread(target=button()).start()