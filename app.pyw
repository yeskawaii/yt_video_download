import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, ttk
import yt_dlp
import os
import threading

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

    progress_bar['maximum'] = len(urls)
    progress_bar['value'] = 0
    status_label.config(text="Descargando...")

    def download_thread():
        for url in urls:
            try:
                opciones = {
                    'outtmpl': f'{carpeta_destino}/%(title)s.%(ext)s',
                    'format': 'bestvideo+bestaudio/best',
                    'merge_output_format': format_var.get(),  # Use selected format
                    'ffmpeg_location': os.path.join(os.path.dirname(__file__), 'ffmpeg', 'bin', 'ffmpeg.exe')
                }

                with yt_dlp.YoutubeDL(opciones) as ydl:
                    ydl.download([url])

                progress_bar['value'] += 1
                root.update_idletasks()

            except Exception as e:
                messagebox.showerror("Error", f"No se pudo descargar el video: {e}")

        status_label.config(text="Descarga completada")
        messagebox.showinfo("Éxito", f"Videos descargados en:\n{carpeta_destino}")

    threading.Thread(target=download_thread).start()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Descargador de YouTube")
    root.geometry("600x450")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    label = tk.Label(frame, text="Lista de URLs de YouTube:")
    label.pack()

    listbox_urls = tk.Listbox(frame, width=60, height=10)
    listbox_urls.pack(side=tk.LEFT, padx=10)

    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar.config(command=listbox_urls.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox_urls.config(yscrollcommand=scrollbar.set)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    btn_add = ttk.Button(button_frame, text="Agregar URL", command=add_url)
    btn_add.grid(row=0, column=0, padx=10)

    btn_remove = ttk.Button(button_frame, text="Eliminar URL", command=remove_url)
    btn_remove.grid(row=0, column=1, padx=10)

    btn_download = ttk.Button(button_frame, text="Descargar Videos", command=descargar_videos)
    btn_download.grid(row=0, column=2, padx=10)
    
    format_label = tk.Label(root, text="Formato de video:")
    format_label.pack()

    format_var = tk.StringVar(value="mp4")
    format_menu = ttk.Combobox(root, textvariable=format_var, values=["mp4", "webm", "mkv"])
    format_menu.pack()

    progress_bar = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
    progress_bar.pack(pady=10)

    status_label = tk.Label(root, text="")
    status_label.pack()

    root.mainloop()