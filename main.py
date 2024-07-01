import tkinter as tk
from tkinter import filedialog
import PyPDF2
import pandas as pd
from elect import main
import getmac , os
from time import sleep

mac=getmac.get_mac_address()
# # mac="00:e9:3a:3a:d6:f7"
print(mac)

def convert_pdf_to_xlsx():

    result_label.config(text="")
    select_button.configure(state=tk.DISABLED)
    
    loading_label.pack(pady=10)

    # Open file dialog to select PDF file
    # pdf_file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    # print(pdf_file_path)
    folder = filedialog.askdirectory()
    files=os.listdir(folder)
    for filename in files:
        print(folder+"/"+filename)
        pdf_file_path=folder+"/"+filename
    
        # directory_path, filename = pdf_file_path.rsplit('/', 1)
        filename=filename.replace("pdf","xls")
        main(pdf_file_path,filename)

        loading_label.pack_forget()
        select_button.configure(state=tk.NORMAL)
        # Show success message
        result_label.config(text="Conversion successful!")

# Create the main window
window = tk.Tk()

window.geometry("400x400")

window.title("PDF to XLSX")

# print(str(mac) ,"==", "00:e9:3a:3a:d6:f7" )
sleep(2)
mac_list=["00:e9:3a:3a:d6:f7","00:e9:3a:3c:a3:b9","2c:db:07:98:ac:e2","80:19:34:9b:65:09"]
# if mac == "00:e9:3a:3a:d6:f7":   #avin
# if mac == "00:e9:3a:3c:a3:b9":     #mash
if mac in mac_list:     #chit
# if str(mac)=="80:19:34:9b:65:09":

    # Create a button to select PDF file
    # select_button = tk.Button(window, text="Select PDF", command=convert_pdf_to_xlsx)
    # Create a button to select PDF file
    select_button = tk.Button(window, text="Select Folder", command=convert_pdf_to_xlsx, bg="grey", fg="white", padx=10, pady=5, relief=tk.RAISED, font=("Arial", 12))
    select_button.pack(pady=20)

    # select_button.pack(pady=20)

    loading_label = tk.Label(window, text="Converting...", font=("Arial", 12))


    # Create a label to show the conversion result
    result_label = tk.Label(window, text="")
    result_label.pack()

    # Start the Tkinter event loop
    window.mainloop()

else:
    print("Not matched")
    loading_label = tk.Label(window, text="Unique ID Unmatched", font=("Arial", 12))

