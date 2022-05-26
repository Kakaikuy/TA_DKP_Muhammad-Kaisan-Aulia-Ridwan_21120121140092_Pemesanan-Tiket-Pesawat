import tkinter as tk                
from tkinter import *               
from tkinter import font  as tkfont 
import re                           
from tkinter import messagebox 

    
class SampleApp(tk.Tk): 

    def __init__(self):
        tk.Tk.__init__(self)

        self.title_font = tkfont.Font(font='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame): 
            
    def __init__(self, parent, controller):
        
        def status1():    
            txtdisplay1.configure(state='normal')   
            for k,v in nomor_penerbangan.items():
                v=60-v
                flight=str(k)+' Available: '  + str(v)
                txtdisplay1.insert(tk.END,'\n'+flight)
            txtdisplay1.configure(state='disabled') 
            
        def clear1():    
            txtdisplay1.configure(state='normal')   
            txtdisplay1.delete('1.0', tk.END)
            txtdisplay1.configure(state='disabled') 

            
        def Validation():   
            
            valid = False

            if len(entry_nama1.get()) == 0:    
                messagebox.showinfo("Error", "Dimohon untuk mengisi nama pertama") 
            elif  entry_nama1.get().isalpha() == False:
                messagebox.showinfo("Error", "Nama pertama hanya bisa berisi huruf saja atau 1 kata saja")   
                
            if len(entry_nama2.get()) == 0:    
                messagebox.showinfo("Error", "Dimohon untuk mengisi nama terakhir")  
            elif  entry_nama2.get().isalpha() == False:
                messagebox.showinfo("Error", "Nama terakhir hanya bisa berisi huruf saja atau 1 kata saja")   

            if re.search("[@]", entry_Email.get()): 
                if re.search("[.]", entry_Email.get()): 
                    valid = True    
                else:
                    messagebox.showinfo("Error", "Dimohon untuk mengisi Email yang VALID") 
            else:
                messagebox.showinfo("Error", "Dimohon untuk mengisi Email yang VALID") 
                
            if len(penerbangan.get()) == 0:   
                messagebox.showinfo("Error", "Dimohon untuk memilih penerbangan")    

            if len(penumpang.get()) == 0:    
                messagebox.showinfo("Error", "Dimohon untuk memilih berapa banyak penumpang")   

            if len(penumpang.get()) != 0 and len(penerbangan.get()) != 0:
                if (nomor_penerbangan[penerbangan.get()])+ int(penumpang.get()) > 60: 
                    messagebox.showinfo("Error", "Tiket sebanyak ini tidak tersedia. \n"+ str( 60 - nomor_penerbangan[penerbangan.get()]) +" seat(s) is/are available for the flight: "+ str(penerbangan.get())) 


            if len(entry_nama1.get()) != 0 and entry_nama1.get().isalpha() == True and entry_nama2.get().isalpha() == True and len(entry_nama2.get()) != 0 and valid != False and len(penerbangan.get()) != 0 and len(penumpang.get()) != 0 and (nomor_penerbangan[penerbangan.get()])+ int(penumpang.get()) <= 60:
                buttonToPageTwo.invoke() 

                
        tk.Frame.__init__(self, parent)
        self.controller = controller        

        global entry_nama1
        global entry_nama2
        global entry_Email
        global penerbangan
        global penumpang
        global txtdisplay1
        global nomor_penerbangan

        
        
        frameHeading = tk.Frame(self)   
        frameHeading.grid(row=0, columnspan=3)  
        heading = tk.Label(frameHeading, text="Flight Booking System", fg="white", bg="#a11212", height="2", width="22")
        heading.grid(row=0,columnspan=2)    
        
        
        label_nama1 = tk.Label(self, text="Nama Awal: ",font=("",15)) 
        label_nama1.grid(row=1, column=0, pady=6)  
        entry_nama1 = tk.Entry(self, font=("",15)) 
        entry_nama1.grid(row=1, column=1, pady=6)
        entry_nama1.focus_force()  


        label_nama2 = tk.Label(self, text="Nama Akhir: ",font=("",15))  
        label_nama2.grid(row=2, column=0, pady=6)
        entry_nama2 = tk.Entry(self, font=("",15)) 
        entry_nama2.grid(row=2, column=1, pady=6)

        label_Email = tk.Label(self, text="Email Address: ",font=("",15))   
        label_Email.grid(row=3, column=0, pady=6)
        entry_Email = tk.Entry(self, font=("",15))  
        entry_Email.grid(row=3, column=1, pady=6)
            
        label_penerbangan = tk.Label(self, text="Pilih Maskapai Penerbangan: ",font=("",15))  
        label_penerbangan.grid(row=4, column=0, pady=6)    
        nomor_penerbangan = {'Garuda NZ345':0, 'Lion Air NZ436':0, 'Citilink NZ543':0, 'Air Asia NZ427':0} 
        penerbangan = tk.StringVar(self)  
        penerbangan.set('') 
        popupMenu_penerbangan = tk.OptionMenu(self, penerbangan, *nomor_penerbangan)   
        popupMenu_penerbangan.configure(font=("",15), width=17)  
        popupMenu_penerbangan.grid(row=4, column=1, pady=6)

        label_penumpang = tk.Label(self, text="Jumlah Penumpang: ",font=("",15))    
        label_penumpang.grid(row=5, column=0, pady=6)
        nomor_penumpang = {1,2,3,4,5,6,7,8,9,10}   
        penumpang = tk.StringVar(self)   
        penumpang.set('') 
        popupMenu_penumpang = tk.OptionMenu(self, penumpang, *nomor_penumpang) 
        popupMenu_penumpang.configure(font=("",15), width=17)  
        popupMenu_penumpang.grid(row=5, column=1, pady=6)
        
        Button_Status= tk.Button(self, text="Status Penerbangan",width="16",height="1", font=("",15), command=status1) 
        Button_Status.grid(row=6, column=0, pady=10,  padx=4)
        Button_Clear= tk.Button(self, text="Clear",width="7",height="1", font=("",15), command=clear1)   
        Button_Clear.grid(row=6, column=1, pady=10, sticky='E')
        
        txtdisplay1= tk.Text(self, width=57, height=15)   
        txtdisplay1.grid(row=7, column=0, columnspan=3)
        txtdisplay1.configure(state='disabled') 

        Button_next= tk.Button(self, text="Next",width="7",height="1", font=("",15), command = Validation)  
        Button_next.grid(row=8, column=1, pady=10, sticky='E')

        Page_One = tk.Label(self, text="Page 1", font=("",10)).grid(row=9, column=1, sticky='E')    
        buttonToPageTwo = tk.Button(self, text="", command=lambda: controller.show_frame("PageTwo"))    
     
        

        
class PageTwo(tk.Frame):


    def __init__(self, parent, controller): 
        def Calc(): 

            txtdisplay2.configure(state='normal')   
           
            if int(dewasa.get()) == 0:
                messagebox.showinfo("Error", "Dimohon untuk memilih setidaknya satu orang dewasa.") 
            else:
                if int(penumpang.get()) == ( int(dewasa.get()) + int(anakkecil.get()) + int(balita.get())):  
                    
                    txtdisplay2.insert(tk.END,"\n----------------------------------------------")
                    txtdisplay2.insert(tk.END, "\nJumlah Penumpang:" + str(penumpang.get()))  
                    txtdisplay2.insert(tk.END,"\nJumlah Orang Dewasa:" + str(dewasa.get()))   
                    txtdisplay2.insert(tk.END,"\nJumlah Anak-Anak:" + str(anakkecil.get()))  
                    txtdisplay2.insert(tk.END,"\nJumlah Balita:" + str(balita.get()))  
                    
                    cost = (int(dewasa.get())*1417000-155870) + (int(anakkecil.get())*675000-74250) 
                    txtdisplay2.insert(tk.END,"\n----------------------------------------------")
                    txtdisplay2.insert(tk.END,"\nHarga: Rp" +str(round(cost,2)))  
                    txtdisplay2.insert(tk.END,"\n----------------------------------------------")
                    txtdisplay2.insert(tk.END,"\nHarga untuk Dewasa: Rp 1.417.000,00 *Termasuk Pajak")    
                    txtdisplay2.insert(tk.END,"\nHarga untuk Anak-Anak: Rp 675.000,00 *Termasuk Pajak")   
                    txtdisplay2.insert(tk.END,"\nHarga untuk Balita: Free")                    
                elif int(penumpang.get()) > ( int(dewasa.get()) + int(anakkecil.get()) + int(balita.get())):     
                     messagebox.showinfo("Error", "Anda telah memilih lebih sedikit penumpang daripada yang dipilih. \n") 
                else:
                    messagebox.showinfo("Error", "Anda telah memilih lebih banyak penumpang daripada yang dipilih. \n")  
                
            txtdisplay2.configure(state='disabled') 

            
        def Confirm():  

            if int(dewasa.get()) == 0:    
                messagebox.showinfo("Error", "Dimohon untuk memilih setidaknya 1 orang dewasa")
            else:
                if int(penumpang.get()) == ( int(dewasa.get()) + int(anakkecil.get()) + int(balita.get())):  
                    loadPageThree = 1
                    buttonToPageThree.invoke()
                    
                elif int(penumpang.get()) > ( int(dewasa.get()) + int(anakkecil.get()) + int(balita.get())): 
                     messagebox.showinfo("Error", "Anda telah memilih lebih sedikit penumpang daripada yang Anda pilih di halaman satu. \n") 
                else:
                    messagebox.showinfo("Error", "Anda telah memilih lebih banyak penumpang daripada yang Anda pilih di halaman satu. \n")  
        def clear2():    
            txtdisplay2.configure(state='normal')   
            txtdisplay2.delete('1.0', tk.END)
            txtdisplay2.configure(state='disabled') 
            
        tk.Frame.__init__(self, parent)
        self.controller = controller

        global dewasa
        global anakkecil
        global balita
        global txtdisplay2

        frameHeading = tk.Frame(self)   
        frameHeading.grid(row=0, columnspan=3)  
        heading = tk.Label(frameHeading, text="Flight Booking System", fg="white", bg="#a11212", height="2", width="22")      
        heading.config(font=("",30))    
        heading.grid(row=0,columnspan=2)    


        label_dewasa = tk.Label(self, text="Jumlah Orang Dewasa: ",font=("",15))    
        label_dewasa.grid(row=5, column=0, pady=6)
        nomor_dewasa = {0,1,2,3,4,5,6,7,8,9,10} 
        dewasa = tk.StringVar(self)   
        dewasa.set(0) 
        popupMenu_dewasa = tk.OptionMenu(self, dewasa, *nomor_dewasa)  
        popupMenu_dewasa.configure(font=("",15), width=17)   
        popupMenu_dewasa.grid(row=5, column=1, pady=6)
        limitdewasa = tk.Label(self, text="*Orang dewasa harus berusia di atas 17 tahun")
        limitdewasa.grid(row=6, column=1, sticky='W')
        popupMenu_dewasa.focus_force()

        label_anakkecil = tk.Label(self, text="Jumlah Anak-Anak: ",font=("",15))  
        label_anakkecil.grid(row=7, column=0, pady=6)
        nomor_anakkecil = {0,1,2,3,4,5,6,7,8,9,10}  
        anakkecil = tk.StringVar(self)    
        anakkecil.set(0)  
        popupMenu_anakkecil = tk.OptionMenu(self,anakkecil, *nomor_anakkecil)  
        popupMenu_anakkecil.configure(font=("",15), width=17)    
        popupMenu_anakkecil.grid(row=7, column=1, pady=6)
        limitanakkecil = tk.Label(self, text="*Anak-anak berusia antara 2 dan 17 tahun inklusif")
        limitanakkecil.grid(row=8, column=1, sticky='W')

        label_balita = tk.Label(self, text="Jumlah Balita: ",font=("",15)) 
        label_balita.grid(row=9, column=0, pady=6)
        nomor_balita = {0,1,2,3,4,5,6,7,8,9,10}   
        balita = tk.StringVar(self)  
        balita.set(0)    
        popupMenu_Infant = tk.OptionMenu(self, balita, *nomor_balita)   
        popupMenu_Infant.configure(font=("",15), width=17)  
        popupMenu_Infant.grid(row=9, column=1, pady=6)
        limitbalita = tk.Label(self, text="*Balita harus berusia dibawah 2 tahun")
        limitbalita.grid(row=10, column=1, sticky='W')

        Button_Clear= tk.Button(self, text="Clear",width="7",height="1", font=("",15), command=clear2)
        Button_Clear.grid(row=11, column=0, pady=6, padx=50, sticky='W')
        
        Button_Calculate = tk.Button(self, text="Calculate",width="8",height="1", font=("",15),
                                     command=Calc).grid(row=11, column=1, pady=6, padx=15, sticky='E')   

        txtdisplay2=tk.Text(self,width=57,height=15)    
        txtdisplay2.grid(row=12, column=0, columnspan=3)
        txtdisplay2.configure(state='disabled')     

        Button_back = tk.Button(self, text="Back", width="7",height="1", font=("",15), command=lambda: controller.show_frame("StartPage"))
        Button_back.grid(row=13, column=0, pady=6, padx=50, sticky='W')  
        Button_Confirm = tk.Button(self, text="Confirm",width="8",height="1", font=("",15), command=Confirm)
        Button_Confirm.grid(row=13, column=1, pady=6, padx=15, sticky='E') 

        buttonToPageThree = tk.Button(self, text="", command=lambda: controller.show_frame("PageThree"))    

        Page_Two = tk.Label(self, text="Page 2", font=("",10)).grid(row=14, column=1, sticky='E')   

class PageThree(tk.Frame):

    def __init__(self, parent, controller):

        def PrintTicket():  
            
            txtdisplay3.configure(state='normal')
            txtdisplay3.insert(tk.END,"\n----------------------------------------------")
            txtdisplay3.insert(tk.END,"\nNama: " + entry_nama1.get() + " " + entry_nama2.get()) 
            txtdisplay3.insert(tk.END,"\nEmail: " + entry_Email.get())                          
            txtdisplay3.insert(tk.END,"\nJumlah penumpang: " + penumpang.get()) 
            txtdisplay3.insert(tk.END,"\nJumlah Orang Dewasa: " + dewasa.get())             
            txtdisplay3.insert(tk.END,"\nJumlah Anak-Anak: " + anakkecil.get())       
            txtdisplay3.insert(tk.END,"\nJumlah Balita: " + balita.get())           
            txtdisplay3.insert(tk.END,"\n----------------------------------------------")
            
            hargatanpapajak = int(dewasa.get())*1417000 + int(anakkecil.get())*675000   
            pajak = int(dewasa.get())*1417000*0.11 + int(anakkecil.get())*675000*0.11   
            TotalHarga = hargatanpapajak + pajak                    

            txtdisplay3.insert(tk.END,"\nMaskapai Penerbangan: " + penerbangan.get())
            txtdisplay3.insert(tk.END,"\nHarga: Rp" + str(hargatanpapajak))    
            txtdisplay3.insert(tk.END,"\nPajak: Rp" + str(pajak))                
            txtdisplay3.insert(tk.END,"\nTotal Harga: Rp" + str(TotalHarga))   
            txtdisplay3.insert(tk.END,"\n----------------------------------------------")
            txtdisplay3.configure(state='disabled') 
            
        tk.Frame.__init__(self, parent) 
        self.controller = controller

        frameHeading = tk.Frame(self)   
        frameHeading.grid(row=0, columnspan=3)  
        heading = tk.Label(frameHeading, text="Flight Booking System", fg="white", bg="#a11212", height="2", width="22")    
        heading.config(font=("",30))    
        heading.grid(row=0,columnspan=2)    
        

        txtdisplay3=tk.Text(self,width=57,height=30)    
        txtdisplay3.grid(row=5, column=0, columnspan=3)
        txtdisplay3.configure(state='disabled') 

        ButtonPrint = tk.Button(self, text="Click to Print the Ticket" ,width="20",height="2", font=("",15),
                                command=PrintTicket).grid(row=6, column=2, pady=6, padx=15, sticky='W')  

   
        
if __name__ == "__main__":
    app = SampleApp()
    app.geometry("512x750")
    app.title("Flight Booking System")  
    app.mainloop()