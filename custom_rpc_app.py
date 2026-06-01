import tkinter as tk
from tkinter import messagebox
from pypresence import Presence
import time
import threading

rpc = None
running = False


def start_rpc():
    global rpc, running

    client_id = entry_client_id.get()
    details = entry_details.get()
    state = entry_state.get()
    large_image = entry_large_image.get()
    large_text = entry_large_text.get()
    small_image = entry_small_image.get()
    small_text = entry_small_text.get()

    if not client_id:
        messagebox.showerror("Błąd", "Musisz podać Client ID!")
        return

    try:
        rpc = Presence(client_id)
        rpc.connect()
        running = True

        def update_loop():
            while running:
                rpc.update(
                    details=details,
                    state=state,
                    large_image=large_image,
                    large_text=large_text,
                    small_image=small_image,
                    small_text=small_text,
                    start=time.time()
                )
                time.sleep(15)

        threading.Thread(target=update_loop, daemon=True).start()
        messagebox.showinfo("Sukces", "Custom RPC uruchomione!")

    except Exception as e:
        messagebox.showerror("Błąd", f"Nie udało się połączyć:\n{e}")


def stop_rpc():
    global running, rpc
    running = False
    if rpc:
        rpc.close()
    messagebox.showinfo("Zatrzymano", "Custom RPC wyłączone!")


# GUI
root = tk.Tk()
root.title("Discord Custom RPC App")
root.geometry("400x450")

tk.Label(root, text="Client ID:").pack()
entry_client_id = tk.Entry(root, width=40)
entry_client_id.pack()

tk.Label(root, text="Details (górny tekst):").pack()
entry_details = tk.Entry(root, width=40)
entry_details.pack()

tk.Label(root, text="State (dolny tekst):").pack()
entry_state = tk.Entry(root, width=40)
entry_state.pack()

tk.Label(root, text="Large Image name:").pack()
entry_large_image = tk.Entry(root, width=40)
entry_large_image.pack()

tk.Label(root, text="Large Image text:").pack()
entry_large_text = tk.Entry(root, width=40)
entry_large_text.pack()

tk.Label(root, text="Small Image name:").pack()
entry_small_image = tk.Entry(root, width=40)
entry_small_image.pack()

tk.Label(root, text="Small Image text:").pack()
entry_small_text = tk.Entry(root, width=40)
entry_small_text.pack()

tk.Button(root, text="START RPC", bg="green", fg="white", command=start_rpc).pack(pady=10)
tk.Button(root, text="STOP RPC", bg="red", fg="white", command=stop_rpc).pack()

root.mainloop()