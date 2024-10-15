import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

def download_video(resolution=None, audio_only=False):
    url = url_entry.get()
    try:
        # Configurações do yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best' if audio_only else f'bestvideo[height<={resolution}]+bestaudio/best',
            'outtmpl': filedialog.askdirectory() + '/%(title)s.%(ext)s'  
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Sucesso", "Download concluído!")
    except Exception as e:
        messagebox.showerror("Erro", f"Falha no download: {e}")


app = tk.Tk()
app.title("QuickTube - Baixar Vídeos e Músicas do YouTube")
app.geometry("800x300")  


window_width = 800
window_height = 370  


screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()


x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)


app.geometry(f"{window_width}x{window_height}+{x}+{y}")


app.configure(bg='black')


logo_path = "C:/Users/Euler/Documents/QuickTube/LogoQuickTube/LogoQuickTube.png"  # Substitua pelo caminho da sua imagem
logo_image = tk.PhotoImage(file=logo_path).subsample(4)  # Reduz a imagem para 50x50
logo_label = tk.Label(app, image=logo_image, bg='black')  # Cor de fundo do label
logo_label.pack(pady=5)


url_label = tk.Label(app, text="Insira a URL do vídeo/música:", bg='black', fg='white')  # Texto branco
url_label.pack()


url_entry = tk.Entry(app, width=100, bg='white', fg='black')  # Fundo branco e texto preto
url_entry.pack()


button_frame = tk.Frame(app, bg='black')  # Cor de fundo do frame
button_frame.pack(pady=10)


video_720p_button = tk.Button(button_frame, text="Baixar em 720p", command=lambda: download_video("720"), bg='grey', fg='black')
video_720p_button.grid(row=0, column=1, padx=5)

video_1080p_button = tk.Button(button_frame, text="Baixar em 1080p", command=lambda: download_video("1080"), bg='grey', fg='black')
video_1080p_button.grid(row=0, column=2, padx=5)


audio_button = tk.Button(app, text="Baixar Áudio", command=lambda: download_video(audio_only=True), bg='grey', fg='black')
audio_button.pack(pady=10)


app.mainloop()
