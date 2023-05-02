from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import ttk # ttk(the tree view) is used to create the tables


window = Tk()
# -------------------- window title --------------------
window.title("Restaturant Management System")

# -------------------- display geomentry --------------------
window.geometry("1400x800") 

# --------------- Data ---------------------
breakfast_menu = [
    ['idli',30],
    ['dosa',40],
    ['poha',40],
    ['poori',40],
    ['upma',30],
    ['paneer_paratha',50]]
lunch_menu = [
    ['rice',40],
    ['roti',20],
    ['chicken',120],
    ['paneer',80],
    ['mutton',100],
    ['biryani',120]]
snacks_menu = [
    ['samosa',15],
    ['panipuri',20],
    ['chaat',20],
    ['momos',50],
    ['thukpa',30],
    ['sandal',20]
]
sb = [] # used to store the values of the spinbox values


# ------------------ Table ------------------------
# treeview
table = ttk.Treeview(window, columns=('items','price','qty','total_price'), show="headings") # show="heading" shows the headings inleft side

# setting col width
table.column("items", width = 100)
table.column("qty", width = 80)
table.column("price", width =80 )
table.column("total_price", width = 80)

table.heading('items', text='Items')
table.heading('qty',text="Qty")
table.heading('price', text='Price' )
table.heading('total_price',text='Total' )

table.place(x=900,y=100)


# -------------------- label to display Name --------------------
name = Label(window, text="Restaurant Management System By Jaswanth", font=("arial","26"), fg="Green")
name.place(x=450,y=10)


# -------------------- Radiobutton --------------------
#variables
v=IntVar()

#function for radio button
item1_breakfast = Image.open("imgs/idli.png")
item1_breakfast = item1_breakfast.resize((150,150))
idli = ImageTk.PhotoImage(item1_breakfast)
item1 = Button(window, image=idli)
item1.place(x=100,y=150)

item2_breakfast = Image.open("imgs/dosa.png")
item2_breakfast = item2_breakfast.resize((150,150))
dosa = ImageTk.PhotoImage(item2_breakfast)
item2 = Button(window, image=dosa)
item2.place(x=300,y=150)

item3_breakfast = Image.open("imgs/poha.png")
item3_breakfast = item3_breakfast.resize((150,150))
poha = ImageTk.PhotoImage(item3_breakfast)
item3 = Button(window, image=poha)
item3.place(x=500,y=150)

item4_breakfast = Image.open("imgs/poori.png")
item4_breakfast = item4_breakfast.resize((150,150))
poori = ImageTk.PhotoImage(item4_breakfast)
item4 = Button(window, image=poori)
item4.place(x=100,y=430)

item5_breakfast = Image.open("imgs/upma.png")
item5_breakfast = item5_breakfast.resize((150,150))
upma = ImageTk.PhotoImage(item5_breakfast)
item5 = Button(window, image=upma)
item5.place(x=300,y=430)

item6_breakfast = Image.open("imgs/paneer_paratha.png")
item6_breakfast = item6_breakfast.resize((150,150))
paneer_paratha = ImageTk.PhotoImage(item6_breakfast)
item6 = Button(window, image=paneer_paratha)
item6.place(x=500,y=430)

# # lunch images 
iteam1_lunch = Image.open("imgs/rice.png")
iteam1_lunch = iteam1_lunch.resize((150,150))
rice = ImageTk.PhotoImage(iteam1_lunch)

iteam2_lunch = Image.open("imgs/roti.jpeg")
iteam2_lunch = iteam2_lunch.resize((150,150))
roti = ImageTk.PhotoImage(iteam2_lunch)

iteam3_lunch = Image.open("imgs/chicken.jpeg")
iteam3_lunch = iteam3_lunch.resize((150,150))
chicken = ImageTk.PhotoImage(iteam3_lunch)

iteam4_lunch = Image.open("imgs/Paneer.jpeg")
iteam4_lunch = iteam4_lunch.resize((150,150))
Panner = ImageTk.PhotoImage(iteam4_lunch)

iteam5_lunch = Image.open("imgs/mutton.jpeg")
iteam5_lunch = iteam5_lunch.resize((150,150))
mutton = ImageTk.PhotoImage(iteam5_lunch)

iteam6_lunch = Image.open("imgs/Biryani.jpeg")
iteam6_lunch = iteam6_lunch.resize((150,150))
Biryani = ImageTk.PhotoImage(iteam6_lunch)

# snacks images
iteam1_snacks = Image.open("imgs/samosa.png")
iteam1_snacks = iteam1_snacks.resize((150,150))
samosa = ImageTk.PhotoImage(iteam1_snacks)

iteam2_snacks = Image.open("imgs/panipuri.png")
iteam2_snacks = iteam2_snacks.resize((150,150))
panipuri = ImageTk.PhotoImage(iteam2_snacks)

iteam3_snacks = Image.open("imgs/chaat.jpeg")
iteam3_snacks = iteam3_snacks.resize((150,150))
chaat = ImageTk.PhotoImage(iteam3_snacks)

iteam4_snacks = Image.open("imgs/momos.jpeg")
iteam4_snacks = iteam4_snacks.resize((150,150))
momos = ImageTk.PhotoImage(iteam4_snacks)

iteam5_snacks = Image.open("imgs/thukpa.png")
iteam5_snacks = iteam5_snacks.resize((150,150))
thukpa = ImageTk.PhotoImage(iteam5_snacks)

iteam6_snacks = Image.open("imgs/sandal.jpeg")
iteam6_snacks = iteam6_snacks.resize((150,150))
sandal = ImageTk.PhotoImage(iteam6_snacks)

# label or food items names
item1_name = Label(window, text='Idli - Rs.30', font=("",16))
item1_name.place(x=110,y=310)
item2_name = Label(window, text='Dosa - Rs.40', font=("",16))
item2_name.place(x=310,y=310)
item3_name = Label(window, text='Poha - Rs.40', font=("",16))
item3_name.place(x=510,y=310)
item4_name = Label(window, text='Poori - Rs.40', font=("",16))
item4_name.place(x=110,y=590)
item5_name = Label(window, text='Upma - Rs.30', font=("",16))
item5_name.place(x=310,y=590)
item6_name = Label(window, text='Paneer Paratha - Rs.50', font=("",16))
item6_name.place(x=510,y=590)

def show_items(val):
    if (val == 1):
        # buttons to display items of breakfast
        item1["image"] = idli
        item2["image"] = dosa
        item3["image"] = poha
        item4["image"] = poori
        item5["image"] = upma
        item6["image"] = paneer_paratha
        item1_name['text'] ='Idli - Rs.30'
        item2_name['text'] ='Dosa - Rs.40'
        item3_name['text'] ='Poha - Rs.40'
        item4_name['text'] ='Poori - Rs.40'
        item5_name['text'] ='Upma - Rs.30'
        item6_name['text'] ='Paneer Paratha - Rs.50'

    elif (val == 2):
        # buttons to display items of breakfast
        item1["image"] = rice
        item2["image"] = roti
        item3["image"] = chicken
        item4["image"] = Panner
        item5["image"] = mutton
        item6["image"] = Biryani
        item1_name['text'] ='Rice - Rs.40'
        item2_name['text'] ='Roti - Rs.20'
        item3_name['text'] ='Chicken - Rs.120'
        item4_name['text'] ='Panner - Rs.80'
        item5_name['text'] ='Mutton - Rs.100'
        item6_name['text'] ='Biryani - Rs.120'

    elif (val == 3):
        # buttons to display items of breakfast
        item1["image"] = samosa
        item2["image"] = panipuri
        item3["image"] = chaat
        item4["image"] = momos
        item5["image"] = thukpa
        item6["image"] = sandal
        item1_name['text'] ='Samosa - Rs.15'
        item2_name['text'] ='Panipuri - Rs.20'
        item3_name['text'] ='Chaat - Rs.20'
        item4_name['text'] ='Momos - Rs.50'
        item5_name['text'] ='Thukpa - Rs.30'
        item6_name['text'] ='Sandal - Rs.20'
    sb_reset()

# for breakfast
breakfast = Radiobutton(window, text='Breakfast', value=0, variable=v, font=('Times',20,'normal'), command=lambda: show_items(1))
breakfast.place(x=120,y=70)

# for lunch
lunch = Radiobutton(window, text='Lunch/Dinner', value=1, variable=v,font=('Times',20,'normal'), command=lambda: show_items(2))
lunch.place(x=310,y=70)

# for dinner
dinner = Radiobutton(window, text='Snacks', value=2, variable=v,font=('Times',20,'normal'), command=lambda: show_items(3))
dinner.place(x=520,y=70)


# -------------- Spinbox to get the items -----------------
sb1 = Spinbox(window,from_=0,to_=10,font=('Times',20,'normal'),width=2)
sb1.place(x=150,y=350)
sb.append(sb1)

sb2 = Spinbox(window,from_=0,to_=10,font=('Times',20,'normal'),width=2)
sb2.place(x=350,y=350)
sb.append(sb2)

sb3 = Spinbox(window,from_=0,to_=10,font=('Times',20,'normal'),width=2)
sb3.place(x=550,y=350)
sb.append(sb3)

sb4 = Spinbox(window,from_=0,to_=10,font=('Times',20,'normal'),width=2)
sb4.place(x=150,y=630)
sb.append(sb4)

sb5 = Spinbox(window,from_=0,to_=10,font=('Times',20,'normal'),width=2)
sb5.place(x=350,y=630)
sb.append(sb5)

sb6 = Spinbox(window,from_=0,to_=10,font=('Times',20,'normal'),width=2)
sb6.place(x=550,y=630)
sb.append(sb6)

# funtion to reset the spinbox values
def sb_reset():
    for i in range(7):
        sb[i].config(textvariable = IntVar(value=0))


# ------------------ Add Bill --------------------
total = 0
final_total = 0
# funtion to add the bills
def add_bill():
    global v, total, table
    if v.get() == 0:
        for i in range(6):
            if int(sb[i].get()) != 0:
                table.insert(parent='',index=END, values=(breakfast_menu[i][0], breakfast_menu[i][1], sb[i].get(), (int(sb[i].get())*breakfast_menu[i][1])))
                total += (int(sb[i].get())*breakfast_menu[i][1])

    if v.get() == 1:
        for i in range(6):
            if int(sb[i].get()) != 0:
                table.insert(parent='',index=END, values=(lunch_menu[i][0], lunch_menu[i][1], sb[i].get(), (int(sb[i].get())*lunch_menu[i][1])))
                total += (int(sb[i].get())*lunch_menu[i][1])

    if v.get() == 2:
        for i in range(6):
            if int(sb[i].get()) != 0:
                table.insert(parent='',index=END, values=(snacks_menu[i][0], snacks_menu[i][1], sb[i].get(), (int(sb[i].get())*snacks_menu[i][1])))
                total += (int(sb[i].get())*snacks_menu[i][1])
        
    sb_reset()


addbill = Button(window, text="Add Bill", font=("",20), command=add_bill)
addbill.place(x=100,y=700)


# -------------------- Get Bill --------------------
# funtion to cal total amount
cost = Label(window, text="", font=("Times",24))
tax = Label(window, text="", font=("Times",24))
total_cost = Label(window, text="", font=("Times",24))
cost_display = Label(window, text="", font=("Times",24))
tax_display = Label(window, text="", font=("Times",24))
total_cost_display = Label(window, text="", font=("Times",24))
def final_bill():
    global table, final_total, total
    # ------------- labels to show the total cost -----------------
    # label to show the Cost
    cost['text'] = "Cost : "
    cost.place(x=900,y=400)
    cost_display['text'] = total
    cost_display.place(x=1000,y=400)

    # label to show the tax %
    tax["text"] = "Tax % : "
    tax.place(x=900,y=450)
    tax_display['text'] = '10%'
    tax_display.place(x=1000,y=450)

    # label to show the total cost
    total_cost['text']="Total Cost : "
    total_cost.place(x=900,y=500)
    final_total = total+(total/10)
    total_cost_display['text'] = final_total
    total_cost_display.place(x=1050,y=500)


getbill = Button(window, text="Get Bill", font=("",20), command=final_bill)
getbill.place(x=300,y=700)


# -------------------- Reset --------------------
# function of reset
def resetbill():
    global total, final_total

    messagebox.showinfo("Total Cost",f"Total Cost : {final_total}\nSee you again\n Have a nice Day :)")
    total = 0
    final_total = 0
    for item in table.get_children():
        table.delete(item)

    cost['text'] = ''
    tax['text'] = ''
    total_cost['text'] = ''
    cost_display['text'] = ''
    tax_display['text'] = ''
    total_cost_display['text'] = ''

reset_bill = Button(window, text="Reset Bill", font=("",20), command=resetbill)
reset_bill.place(x=500, y=700)


# -------------------- Exit --------------------
# funtion to close the window
def close_window():
    window.after(100,window.destroy)


exit_window = Button(window, text="Close", font=("",20), command=close_window)
exit_window.place(x=1000,y=700)


# -------------------- Remove ------------------
# function to remove item
def delete_items():
    global total
    for i in table.selection():
        total -= table.item(i)['values'][3]
        table.delete(i)
    cost_display['text'] = total
    final_total = total+(total/10)
    total_cost_display['text'] = final_total

    

table.bind('<Delete>',delete_items) 

remove_item = Button(window, text="Remove Item" , font=("",20), command=delete_items)
remove_item.place(x=980,y=340)


window.mainloop() 