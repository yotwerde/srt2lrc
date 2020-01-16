# WHEN SEPARATING FILENAME AND PATH
# I'M USING / AS SEPARATOR
# IS THIS GONNA MAKE PROBLEMS WHEN RUN ON A WINDOWS MACHINE?

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class Converter:
    def __init__(self, master):
        # Variables holding the filepath and save directory
        self.filepath = ''
        self.savedir = ''

        # StringVars
        # No initialization to text needed
        self.filepath_var = tk.StringVar()
        self.savedir_var = tk.StringVar()
        
        # Labels
        self.filepath_label = tk.Label(master, text = 'SRT File to convert: ')
        self.savedir_label = tk.Label(master, text = 'LRC Save Directory: ')
        self.filepath_displaybox_label = tk.Label(master, bd = 5, textvariable = self.filepath_var, width = 30, justify = tk.LEFT)
        self.savedir_displaybox_label = tk.Label(master, bd = 5, textvariable = self.savedir_var, width = 30, justify = tk.LEFT)

        # Buttons
        self.button_browse_text = 'Browse'
        self.file_browse_button = tk.Button(master, text = self.button_browse_text, command = self.get_filepath)
        self.dir_browse_button = tk.Button(master, text = self.button_browse_text, command = self.get_savedir)
        self.convert_button = tk.Button(master, text = 'Convert', command = self.convert)
        self.quit_button = tk.Button(master, text = 'Quit', command = master.destroy)

        # Layout
        self.filepath_label.grid(row = 0)
        self.filepath_displaybox_label.grid(row = 0, column = 1, sticky = tk.W)
        self.file_browse_button.grid(row = 0, column = 2)
        self.savedir_label.grid(row = 1)
        self.savedir_displaybox_label.grid(row = 1, column = 1, sticky = tk.W)
        self.dir_browse_button.grid(row = 1, column = 2)
        self.convert_button.grid(row = 2)
        self.quit_button.grid(row = 2, column = 2)

    def get_filepath(self):
        self.filepath = filedialog.askopenfilename(filetypes = [('SubRip', '.srt')])
        self.filepath_var.set(self.filepath) # Update label displaying the file path

    def get_savedir(self):
        self.savedir = filedialog.askdirectory(mustexist = 1)
        self.savedir_var.set(self.savedir) # Update label displaying the save directory for the converted file

    def convert_allowed(self):
        if self.filepath != '' and self.savedir != '':
            return True
        return False

    def convert(self):
        if not self.convert_allowed():
            messagebox.showerror(title='Error', message='Both Source .srt file and Save Directory are needed to proceed!')
            return
        # Separate filename from path in filepath
        c = -1
        while self.filepath[c] != '/':
            c -= 1
        filename = self.filepath[c + 1:]
        # The actual conversion
        self.to_lrc(self.filepath, filename, self.savedir)

    def to_lrc(self, filepath, filename, savedir):
        srt = open(filepath, 'r')
        lrc = open(savedir + '/' + filename[:-4] + '.lrc', 'w')

        lrc_lines = []
        srt_lines = srt.readlines()
        index = 1
        while index < len(srt_lines):
            temp_time = srt_lines[index][3:12]
            temp_time = temp_time.replace(',', '.', 1)
            index += 1
            temp_lyric = srt_lines[index]
            temp_line = '[' + temp_time  + ']' + temp_lyric
            lrc_lines.append(temp_line)
            index += 3

        for line in lrc_lines:
            lrc.write(line)

        srt.close()
        lrc.close()

title = 'SRT2LRC Converter'
root = tk.Tk()
root.title(title)
root.resizable(False, False)

converter = Converter(root)

root.mainloop()