import tkinter as tk
from tkinter import *
from tkinter import filedialog,ttk, messagebox
import pandas as pds
from geopy.geocoders import Bing
import googlemaps


def concluido():
    return messagebox.showinfo('Consultar Rota','Concluído!')
    
class Application:
    def __init__(self, master):
        self.widget1 = Frame(master,bg='black')
        self.widget1.pack()#pady=100
        
        self.msg = Label(self.widget1, text="CONSULTA DE ROTA", bg = 'black', fg = 'white')
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack ()
        
        self.primeiroContainer = Frame(master,bg='black')
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
        
        self.terceiroContainer = Frame(master,bg='black')
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        
        self.quartoContainer = Frame(master,bg='black')
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()
        
        self.segundoContainer = Frame(master,bg='black')
        #self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
        
        self.quintoContainer = Frame(master,bg='black')
        self.quintoContainer["pady"] = 20
        self.quintoContainer.pack()
        
        
        self.cabecalho = Label(self.primeiroContainer, text='         Latitude       Longitude', bg = 'black', fg = 'white',font=('helvetica', 10, 'bold')).pack(side=LEFT,padx=50)#SEPARAR EM DUAS LABELS NO MESMO CONTEINER
        
        self.inicio = Label(self.terceiroContainer, text='Início', bg = 'black', fg = 'white',font=('helvetica', 10, 'bold')).pack(side=LEFT)
        self.inicio_x = Entry(self.terceiroContainer, width=10,font=('helvetica', 10, 'bold'))
        self.inicio_x.pack(side=LEFT)
        self.inicio_y = Entry(self.terceiroContainer, width=10,font=('helvetica', 10, 'bold'))
        self.inicio_y.pack(side=LEFT,padx=10)
        
        self.fim = Label(self.quartoContainer, text='  Fim', bg = 'black', fg = 'white',font=('helvetica', 10, 'bold')).pack(side=LEFT)
        self.fim_x = Entry(self.quartoContainer, width=10,font=('helvetica', 10, 'bold'))
        self.fim_x.pack(side=LEFT)
        self.fim_y = Entry(self.quartoContainer, width=10,font=('helvetica', 10, 'bold'))
        self.fim_y.pack(side=LEFT,padx=10)
        
        self.consultar = Button(self.segundoContainer,text='Consultar',relief=GROOVE,font=('helvetica', 10, 'bold'))
        self.consultar["command"] = self.rota_google
        self.consultar.pack()
        
        self.mensagem = Label(self.quintoContainer, text="", bg = 'black', fg = 'white', font=('helvetica', 10, 'bold'))
        self.mensagem.pack()
        self.mensagem_1 = Label(self.quintoContainer, text="", bg = 'black', fg = 'white', font=('helvetica', 10, 'bold'))
        self.mensagem_1.pack()
        
        '''self.action = Button(self.widget1, command=concluido, bg='white', fg='red', font=('helvetica', 12, 'bold'),relief=GROOVE,padx=10,pady=10)#.place(x=150,y=150)
        self.action["text"] = "Consultar"
        self.action["font"] = ("Calibri", "10")
        self.action.pack()'''
        
        self.assinatura = Label(master, text="Desenvolvido por Sergio Tavora",bg='black', fg='white', font=('helvetica', 7, 'bold')).place(x=5,y=280)
        
    def rota(self):
            
        lat1 = float(self.inicio_x.get())
        lon1 = float(self.inicio_y.get())
        lat2 = float(self.fim_x.get())
        lon2 = float(self.fim_y.get())
            
        
        bing = pybingmaps.Bing('API KEY')
        start = (lat1,lon1)
        end = (lat2,lon2)
        print(start,end)
        m = 0
        try:
            bing.route(start, end)
            m = bing.travelDistance(start, end)
            t = bing.travelTime(start, end)
                
            self.mensagem['text'] = str(m) + " metros"
            self.mensagem_1['text'] = str(t) + " minutos"
                
        except:
            
            self.mensagem['text'] = "Deu ruim"
        
    def rota_google(self):
        
        lat1 = float(self.inicio_x.get())
        lon1 = float(self.inicio_y.get())
        lat2 = float(self.fim_x.get())
        lon2 = float(self.fim_y.get())
        
        origin = {'lat':lat1,'lng':lon1}
        destination = {'lat':lat2,'lng':lon2}
        
        gmaps = googlemaps.Client(key='API KEY')
        
        try:
            m = gmaps.distance_matrix(origin, destination)
            print(m)
            
            self.mensagem['text'] = str(m) + " metros"
            
        except: 
        
            self.mensagem['text'] = "Deu ruim"
        
        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('300x300')
    #root.attributes('-toolwindow',True)
    root.configure(background = 'black')
    root.title("Consulta Rota - Google")
    #root.create_text(125,295,fill="white",text="Desenvolvido por Sergio Tavora - OSP Projetos")
    Application(root)
    
    root.mainloop()