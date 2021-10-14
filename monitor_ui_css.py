from tkinter import Tk, Frame, X, Text, filedialog, Label, messagebox, scrolledtext, PhotoImage
from tkinter.ttk import Button
from tkinter.constants import END
from monitor_script import MonitorVentas
import os
import logging
class CcsUi:
    def __init__(self):
        logging.basicConfig(filename='log_scaner_css.log', format='%(asctime)s : %(levelname)s : %(message)s',filemode='a')
        self.ccs_ui=Tk()
        self.watchdog = None
        self.folder_selected = None
        imgicon = PhotoImage(file=os.path.join('ccs.png')) 
        self.ccs_ui.tk.call('wm', 'iconphoto', self.ccs_ui._w, imgicon) 
        
        ancho_windows=self.ccs_ui.winfo_screenwidth()
        alto_windows=self.ccs_ui.winfo_screenheight()
    
        self.ccs_ui.title('Monitor CCS')
        #self.MenuBar()
        self.CcsUiFrame=Frame(self.ccs_ui)
        self.CcsUiFrame.grid(sticky="wne")
        self.CcsUiFrame.pack(expand=0, fill=X)
        self.elementUI()
        self.ccs_ui.mainloop()
    
    def elementUI(self):
        self.txt_directorio=Text(self.CcsUiFrame, height=1)
        self.txt_directorio.grid(column=0, row=0)
        Button(self.CcsUiFrame, text="Elegir Directorio", command=self.select_directorio).grid(column=1, row=0)
        Label(self.CcsUiFrame, text="Monitor", font= ("Times New Roman",19)).grid(column=0, row=1, sticky="we", columnspan=2)
        # self.txt_scaner = Text(self.CcsUiFrame, height=30)
        self.txt_scaner = scrolledtext.ScrolledText(self.CcsUiFrame, height=15 ,font = ("Times New Roman",12))
        self.txt_scaner.grid(column=0, row=2, columnspan=2, sticky="we")
        self.txt_scaner.configure(state ='disabled')
        Button(self.CcsUiFrame, text="Iniciar Escaneo", command=self.start_scan).grid(column=0, row=3, padx=10, pady=10, columnspan=2)
        Button(self.CcsUiFrame, text="Detener Escaneo", command=self.stop_scan).grid(column=0, row=4,  padx=10, pady=10, columnspan=2)

    def select_directorio(self):
        self.folder_selected = filedialog.askdirectory()
        self.txt_directorio.insert("1.0", self.folder_selected)       

    def start_scan(self):        
        if self.watchdog is None:
            if self.folder_selected:
                self.watchdog = MonitorVentas(path=self.folder_selected, logfunc=self.log)
                self.watchdog.start()
                self.log('Escaneo Iniciado')
            else:
                messagebox.showerror("Incorrecto", "No ha seleccionado un directorio")   
        else:
            self.log('El servicio ya esta iniciado')
    def stop_scan(self):
        if self.watchdog:
            self.watchdog.stop()
            self.watchdog = None
            self.log('Servicio detenido')
        else:
            self.log('El servicio no esta iniciado')
    def log(self, message):        
        # logging.warning(message)
        self.txt_scaner.configure(state='normal')
        self.txt_scaner.insert(END, f"{message}\n")
        self.txt_scaner.configure(state='disabled')
        self.txt_scaner.see(END)

api=CcsUi()