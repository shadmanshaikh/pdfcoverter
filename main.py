from cProfile import label
from importlib.metadata import entry_points
import string
import tkinter as tk
import aspose.slides as slides
import aspose.pydrawing as drawing
from PIL import ImageTk , Image
from tkinter import PhotoImage, filedialog


main = tk.Tk()
main.title("PPT to PdfConverter")
p1 = PhotoImage(file = 'icon.png')
main.iconphoto(False,p1)

main.geometry("900x300")  
poster = ImageTk.PhotoImage(Image.open(r"poster_03.png"))
poster_label = tk.Label(main,image=poster)
poster_label.pack()

def opefile():
        global file
        global file_text
        file = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("PPT",
                                                        "*.pptx*"),
                                                       ("all files",
                                                        "*.*")))
        file_text = tk.Label(main, bg="red" , bd=3 )
        file_text.configure(text="File Opened: "+file)
        
        file_text.pack()
        print(file)


def readfile():
    global open
    string = open.get()
    with slides.Presentation(file) as presentation:
        presentation.save("converted.pdf ",slides.export.SaveFormat.PDF)
open_label = tk.Label(main, text="Type path manually: " ,bg="red" , bd=3 ).place(x=140,y=170)
open = tk.Entry(main ,  width=50 , bd=6)
open_btn = tk.Button(main , text="open",command=opefile , bg="red" , bd=4 ).place(x=480 , y=230)

or_label = tk.Label(main, text="OR").place(x=450,y=210)
save_btn = tk.Button(main , text="convert" , command=readfile , bg="powderblue" , bd=4 ).place(x=380 , y=230)
# save_btn.pack()

open.pack(padx=10, pady=10)
# open_label.pack()
main.mainloop()
tk.Tk.update(main)
tk.Tk.update_idletasks(main)