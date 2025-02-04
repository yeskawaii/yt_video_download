import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
import yt_dlp
import os

def descargar_video():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter

    # Pedir el enlace del video
    url = simpledialog.askstring("Descargar Video", "Ingresa el enlace del video de YouTube:")
    if not url:
        messagebox.showwarning("Advertencia", "No ingresaste un enlace.")
        return

    # Seleccionar carpeta de guardado
    carpeta_destino = filedialog.askdirectory(title="Selecciona la carpeta de destino")
    if not carpeta_destino:
        messagebox.showwarning("Advertencia", "No seleccionaste una carpeta.")
        return

    try:
        # Configuración para descargar video con la mejor calidad
        opciones = {
            'outtmpl': f'{carpeta_destino}/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best',
            'ffmpeg_location': os.path.join(os.path.dirname(__file__), 'ffmpeg', 'bin', 'ffmpeg.exe')  # Path to ffmpeg executable
        }

        with yt_dlp.YoutubeDL(opciones) as ydl:
            ydl.download([url])

        messagebox.showinfo("Éxito", f"Video descargado en:\n{carpeta_destino}")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo descargar el video: {e}")

if __name__ == "__main__":
    descargar_video()