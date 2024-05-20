'''GUI para registro de estudiantes en '''
from tkinter import Tk, Canvas,Label,Frame,Entry, Button, W,E,Listbox,END,messagebox
import psycopg2

root=Tk()
root.title("Entregable")
def guardar_estudiante(name,age,degree):
    conn= psycopg2.connect(
        dbname="postgres" ,
        user="postgres" , 
        password="admin", 
        host="localhost", 
        port="5432"
    )
    cursor = conn.cursor()
    query = ''' INSERT INTO students(name,age,degree) VALUES (%s, %s, %s)'''
    cursor.execute(query,(name,age,degree))
    print("Estudiante guardado")
    conn.commit()
    conn.close()
    mostrar_estudiantes()

def mostrar_estudiantes():
    conn= psycopg2.connect(
        dbname="postgres" ,
        user="postgres" , 
        password="admin", 
        host="localhost", 
        port="5432"
    )
    cursor = conn.cursor()
    query = ''' SELECT * FROM students'''
    cursor.execute(query)
    row= cursor.fetchall()
    listbox= Listbox(frame, width=20, height=10)
    listbox.grid(row=10,columnspan=4,sticky=W+E)
    for x in row:
        listbox.insert(END,x)
    conn.commit()
    conn.close()

def buscar(id):
    conn= psycopg2.connect(
        dbname="postgres" ,
        user="postgres" , 
        password="admin", 
        host="localhost", 
        port="5432"
    )
    
    cursor = conn.cursor()
    query = ''' SELECT * FROM students WHERE id=%s'''
    cursor.execute(query,id)
    row = cursor.fetchone()
    if row:
        mostrar_busqueda(row)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Busqueda fallida","El ID es incorrecto")
        conn.commit()
        conn.close()

def mostrar_busqueda(row):
    listbox=Listbox(frame,width=20,height=1)
    listbox.grid(row=9,columnspan=4, sticky=W+E)
    listbox.insert(END,row)

canvas = Canvas(root, height=300, width=400)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
label= Label(frame, text ="Agregar estudiante")
label.grid(row=0, column=1)
#Input nombre
label=Label(frame, text="Nombre")
label.grid(row=1, column=0)
entry_name=Entry(frame)
entry_name.grid(row=1,column=1)
#Input edad
label=Label(frame, text="Edad")
label.grid(row=2, column=0)
entry_age=Entry(frame)
entry_age.grid(row=2,column=1)
#Input programa academico
label=Label(frame, text="Carrera")
label.grid(row=3, column=0)
entry_degree=Entry(frame)
entry_degree.grid(row=3,column=1)

button=Button(frame, text="Agregar",command=lambda:guardar_estudiante(entry_name.get(),entry_age.get(),entry_degree.get()))
button.grid(row=4, column=1,sticky=W+E)

#Buscar estudiante
label = Label(frame, text="Buscar estudiante")
label.grid(row=5, column=0)

label=Label(frame, text="Buscar por id")
label.grid(row=6, column=0)
id_search=Entry(frame)
id_search.grid(row=6, column=1)

button=Button(frame, text="Buscar", command=lambda:buscar(id_search.get()))
button.grid(row=6,column=2)
mostrar_estudiantes()
root.mainloop()