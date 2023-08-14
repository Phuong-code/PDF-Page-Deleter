import tkinter as tk
from tkinter import filedialog
from PyPDF4 import PdfFileReader, PdfFileWriter

selected_file = ""

def select_pdf_file():
    global selected_file
    selected_file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if selected_file:
        delete_button.config(state=tk.NORMAL)  # Enable the delete button

def delete_pages():
    pdf = PdfFileReader(selected_file)
    output = PdfFileWriter()
    page_numbers = [int(p.strip()) for p in page_entry.get().split(',')]

    for i in range(pdf.getNumPages()):
        if i+1 not in page_numbers:
            output.addPage(pdf.getPage(i))

    destination_path = selected_file.replace(".pdf", "_new.pdf")
    with open(destination_path, 'wb') as f:
        output.write(f)
    result_label.config(text=f"File saved as: {destination_path}")

# Create the main window
root = tk.Tk()
root.title("PDF Page Deleter")

# Create UI elements
file_button = tk.Button(root, text="Select PDF File", command=select_pdf_file)
file_button.pack()

page_label = tk.Label(root, text="Enter page numbers to delete (comma-separated):")
page_label.pack()

page_entry = tk.Entry(root)
page_entry.pack()

delete_button = tk.Button(root, text="Delete Pages", command=delete_pages, state=tk.DISABLED)  # Initially disabled
delete_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()
