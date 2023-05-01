from tkinter import *
import pandas as pd
from tkinter import ttk, filedialog
#import openpyxl

data = pd.read_excel("./BabasExcel.xlsx")
data_dict = data.to_dict()
data_list = list(data)
print(data_list)





def create_new_Type():
    new_list = []
    for a, b, c in some_function_that_yields_data():
        new_list.append([a, b, c])
    df = pd.DataFrame(new_list, columns=['A', 'B', 'C'])

    with pd.ExcelWriter('BabasExcel.xlsx',mode='a') as writer: 
        data.to_excel(writer)


create_new_Type()

root = Tk()
root.title('Babas Budget App')
root.geometry("700x500")


# create the frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# create my treeview
my_tree = ttk.Treeview(my_frame)

# file open function

def file_open():
    filename = filedialog.askopenfilename(
        initialdir = "/home/guelden/Schreibtisch/",
        title = "Open A File",
        filetypes = (("xlsx files","*.xlsx"),("All Files","*.*"))
        )
    
    if filename:
        try: 
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)
        except ValueError:
            my_label.config(text="File Could Not Be Opend..Try Again")
        except FileNotFoundError:
            my_label.config(text="File Could Not Be Found")
   

    # clear old tree view
    clear_tree()

    # set up new tree view
    my_tree["column"] = list(df.columns)
    my_tree["show"] = "headings"
    # loop through column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    # put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert('', 'end', values=row)

    # pack the tree view
    my_tree.pack()

def clear_tree():
    my_tree.delete(*my_tree.get_children())    


def add_type():
    pass

def add_input():
    pass


# add a menu

my_menu = Menu(root)
root.config(menu=my_menu)

# add a dropdown
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Spreadsheets", menu=file_menu)
file_menu.add_command(label="Open", command=file_open)

my_label = Label(root, text="")
my_label.pack(pady=20)

e = Entry(root)
e.pack()

root.mainloop()