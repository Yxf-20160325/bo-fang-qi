
from datetime import datetime
from doctest import master
import shutil
import webbrowser
import tkinter as tk
from tkinter import filedialog
import pygame
import logging
import os
class MusicPlayer:
    def __init__(self, master):
        self.master = master
      

    def some_method(self):
        # 在这里使用self来访问实例变量或调用其他实例方法
        self.log_text = tk.Text(self.master, width=70, height=10)
       

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 创建 log 文件夹
log_dir = os.path.join(current_dir, 'log')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# 获取当前时间
current_time = datetime.now().strftime('%Y%m%d_%H%M')

# 配置日志记录
logging.basicConfig(filename=os.path.join(log_dir, f'music_player_{current_time}.log'), level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("音乐播放器")

        self.playlist = []
        self.current_track = 0

        # 使用 Text 部件替代 Entry 部件，并设置高度为 5 行
        self.entry = tk.Text(master, width=70, height=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '打开', '播放', '暂停', '上一曲', '下一曲', '打开日志文件夹', '清除日志','打开新播放器'
    ]
        
        print("版本号:1.0.34671")
        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.button_click(x)
            tk.Button(master, text=button, width=10, command=command).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1

        # 播放列表
        self.playlist_box = tk.Listbox(master, width=70, height=10)
        self.playlist_box.grid(row=row+1, column=0, columnspan=4, padx=10, pady=10)

        # 添加音量调节滑块
        self.volume_scale = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL, label="音量", command=self.set_volume)
        self.volume_scale.grid(row=row, column=4, columnspan=1, padx=10, pady=10)
        # 设置音量滑块默认为100
        self.volume_scale.set(100)

    pygame.mixer.init()

    def button_click(self, button):
        if button == '打开':
            self.open_file()
        elif button == '播放':
            self.play_music()
        elif button == '暂停':
            self.pause_music()
        elif button == '上一曲':
            self.previous_track()
        elif button == '下一曲':
            self.next_track()
        elif button == '打开日志文件夹':
            self.open_log_folder()
        elif button == '清除日志':
            self.clear_log()
        elif button == '打开新播放器':
            self.open_new_player()
        elif button == '命令运行beta':
            self.run_command_cmd_error()
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("音频文件", "*.mp3;*.wav;*.ogg")])
        if file_path:
            self.playlist.append(file_path)
            self.entry.delete(1.0, tk.END)
            self.entry.insert(1.0, "已添加到播放列表: " + file_path)
            # 将文件路径添加到播放列表框中
            self.playlist_box.insert(tk.END, file_path)
            logging.info(f"添加文件到播放列表: {file_path}")

    def play_music(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()
            self.entry.delete(1.0, tk.END)
            self.entry.insert(1.0, "正在播放: " + self.playlist[self.current_track])
            logging.info(f"正在播放: {self.playlist[self.current_track]}")

    def pause_music(self):
        pygame.mixer.music.pause()
        self.entry.delete(1.0, tk.END)
        self.entry.insert(1.0, "音乐已暂停")
        logging.info("音乐已暂停")

    def previous_track(self):
        if self.playlist:
            self.current_track = (self.current_track - 1) % len(self.playlist)
            self.play_music()
            logging.info(f"播放上一曲: {self.playlist[self.current_track]}")

    def next_track(self):
        if self.playlist:
            self.current_track = (self.current_track + 1) % len(self.playlist)
            self.play_music()
            logging.info(f"播放下一曲: {self.playlist[self.current_track]}")

    def set_volume(self, volume):
        # 将音量值从 0-100 映射到 0.0-1.0
        pygame.mixer.music.set_volume(float(volume) / 100)
        logging.info(f"设置音量为: {volume}")

    def open_log_folder(self):
        # 使用默认文件管理器打开日志文件夹
        import subprocess
        subprocess.Popen(f'explorer.exe {log_dir}')
        logging.info("已打开日志文件夹")

    def clear_log(self):
        # 清空日志文件夹
        for file in os.listdir(log_dir):
            file_path = os.path.join(log_dir, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    logging.info(f"已清除文件: {file_path}")
            except Exception as e:
                print(f"无法清除文件: {file_path}, 原因: {e}")
                logging.error(f"无法清除文件: {file_path}, 原因: {e}")

    def open_new_player(self):
        # 打开第二播放器
        root = tk.Tk()
        debug_player = MusicPlayer(root)
        root.mainloop()
        logging.info("已打开第2个播放器")
    def run_command_cmd(self):
        import subprocess
         # 获取当前目录
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # 构建文件的路径
        run_command_file_path = os.path.join(current_dir, 'dist', '1', '_internal', 'beta_run_command.py')

        # 使用subprocess模块打开文件
        subprocess.Popen(['python', run_command_file_path])

        logging.info("已打开命令运行器")

        def run_command_cmd_error(self):
            print ("命令运行器正在开发中，请使用beta版本。")
            logging.error("命令运行器正在开发中，请使用beta版本。")
           
logging.info("程序已启动")
root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
logging.info("程序已关闭")
