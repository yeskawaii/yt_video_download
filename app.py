import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import yt_dlp
import os

def add_url():
    url = simpledialog.askstring("Agregar Video", "Ingresa el enlace del video de YouTube:")
    if url:
        listbox_urls.insert(tk.END, url)

def remove_url():
    selected = listbox_urls.curselection()
    if selected:
        listbox_urls.delete(selected)

def descargar_videos():
    urls = listbox_urls.get(0, tk.END)
    if not urls:
        messagebox.showwarning("Advertencia", "No hay enlaces para descargar.")
        return

    carpeta_destino = filedialog.askdirectory(title="Selecciona la carpeta de destino")
    if not carpeta_destino:
        messagebox.showwarning("Advertencia", "No seleccionaste una carpeta.")
        return

    for url in urls:
        try:
            opciones = {
                'outtmpl': f'{carpeta_destino}/%(title)s.%(ext)s',
                'format': 'bestvideo+bestaudio/best',
                'ffmpeg_location': os.path.join(os.path.dirname(__file__), 'ffmpeg', 'bin', 'ffmpeg.exe')
            }

            with yt_dlp.YoutubeDL(opciones) as ydl:
                ydl.download([url])

            messagebox.showinfo("Éxito", f"Video descargado en:\n{carpeta_destino}")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo descargar el video: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Descargador de YouTube")
    root.geometry("500x400")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    listbox_urls = tk.Listbox(frame, width=50, height=10)
    listbox_urls.pack(side=tk.LEFT, padx=10)

    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar.config(command=listbox_urls.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox_urls.config(yscrollcommand=scrollbar.set)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    btn_add = tk.Button(button_frame, text="Agregar URL", command=add_url)
    btn_add.grid(row=0, column=0, padx=10)

    btn_remove = tk.Button(button_frame, text="Eliminar URL", command=remove_url)
    btn_remove.grid(row=0, column=1, padx=10)

    btn_download = tk.Button(button_frame, text="Descargar Videos", command=descargar_videos)
    btn_download.grid(row=0, column=2, padx=10)

    root.mainloop()