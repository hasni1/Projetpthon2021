import mysql.connector
def connect_BD():
    mydb = mysql.connector.connect(
        host="localhost",
        user="hamza",
        password="zapatista2007",
        database="gestionpatisserie"
        )
    return mydb


class produit:
    db=connect_BD()
    mycursor=db.cursor()
    def __init__(self,i=0,typee='',quantite=''):
        self.id=i
        self.typee=typee
        self.quantite=quantite

    def ajouterproduit(self):
        sql="INSERT INTO produit (id,typee,quantite) VALUES (%s,%s,%s)"
        val=(self.id,self.typee,self.quantite)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"AJOUT FAIS AVEC SUCCES")
    
    def afficherproduit(self):
        self.mycursor.execute("SELECT * FROM produit ")
        resultat=self.mycursor.fetchall()
        return resultat
            
    def supprimerproduit(self,other):
        sql="DELETE FROM produit WHERE id=%s"
        val=(other,)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"suppression FAIS AVEC SUCCES")

    def rechercher(self,other):
        sql = "SELECT * FROM produit where id like %s or typee like %s "
        other='%'+other+'%'
        val=(other,other)
        self.mycursor.execute(sql,val)  
        rows=self.mycursor.fetchall()
        return rows
        

    def modifierproduit(self,other):
        
        sql="UPDATE produit SET quantite=%s, typee =%s WHERE id= %s"
        val=(self.quantite,self.typee,other)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"UPDATE FAIS AVEC SUCCES")
#programme principale
#a=produit()
#a.ajouterproduit()
#a.afficherproduit()





from tkinter import *
import tkinter.ttk as ttk

class gestionproduit():
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x600')
        self.root.title("Gestion patisserie")
        self.id=StringVar()
        self.typee=StringVar()
        self.quantite=StringVar()
        self.cher=StringVar
  
        
  
        
    #Formulaire ajout Id produit dans __init():
        #============== produit TEXTFIELD AND LABEL
        x = Label(self.root,text = "Id",anchor='w')
        x.grid(row = 0,column = 0,padx = 40,pady = 40)
        y= Entry(self.root,textvariable = self.id)
        y.grid(row = 0,column = 1,ipady = 7,ipadx = 20,padx = 20)

        
        #=======================typee produit LABEL AND TEXTFIELD
        x= Label(self.root,text="type",anchor='w')
        x.grid(row = 2,column = 0,pady = 40)
        y = Entry(self.root,textvariable = self.typee)
        y.grid(row = 2,column = 1,ipady = 7,ipadx = 20,padx = 20)
         #=======================quantite produit LABEL AND TEXTFIELD
        x= Label(self.root,text="quantite",anchor='w')
        x.grid(row = 2,column = 2,pady = 40)
        y = Entry(self.root,textvariable = self.quantite)
        y.grid(row = 2,column = 3,ipady = 7,ipadx = 20,padx = 20)
        #=======================chercher produit LABEL AND TEXTFIELD
        x= Label(self.root,text="chercher",anchor='w')
        x.grid(row = 5,column = 0,pady = 40)
        y = Entry(self.root,textvariable = self.cher)
        y.grid(row = 5,column = 1,ipady = 7,ipadx = 20,padx = 20)



        
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        x= Button(self.root,text = "Supprimer",command = self.remove,anchor='c')
        x.grid(row = 6,column = 1,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton affichage à ajouter après boutton "Ajouter" dans __init()__
        x= Button(self.root,text = "Afficher",command = self.view,anchor='c')
        x.grid(row = 6,column = 2,ipady = 4,ipadx = 13,pady = 40)
 
        
        #=====================Boutton ajout
        x = Button(self.root,text = "Ajouter",command = self.add,anchor='c')
        x.grid(row = 6,column = 0,ipady = 4,ipadx = 13,pady = 40)

        #=====================Boutton modifier
        x = Button(self.root,text = "Modifier",command = self.modifier,anchor='c')
        x.grid(row = 6,column = 3,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton chercher à ajouter après boutton "chercher" dans __init()__
        x= Button(self.root,text = "chercher",command = self.chercher,anchor='c')
        x.grid(row = 6,column = 6,ipady = 4,ipadx = 13,pady = 40)


        
        #Fonction d'ajout d'un produit (sera appelée dérière le boutton "Ajouter")
    def add(self):
        E = produit(self.id.get(),self.typee.get(),self.quantite.get())
        print("produit: ",E.id)
        E.ajouterproduit()

        #Fonction de suppression d'un produit sera appelée dans le boutton "Supprimer"  
    def remove(self):
        E = produit()
        E.supprimerproduit(self.id.get())
        #Fonction de modification d'un produit sera appelée dans le boutton "modifier"  
    def modifier(self):
        E = produit(self.quantite.get(),self.typee.get())
        E.modifierproduit(self.id.get())
    

    def view(self):
        #self.root.title("product managment(Details)")
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('800x400')
        self.root.title("Affichage des produits")
        show_frame = Frame(self.root)
        show_frame.place(width = 1000,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage des listes des produits ")
        labl_show.pack()
        
        #========================Main Frame
        x= Frame(self.root,bd = 10,relief = SUNKEN)
        x.place(width = 800,height = 300,x = 8,y = 58)
        tree = ttk.Treeview(x,height = 200)
        vsb = ttk.Scrollbar(x,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3")
        tree.column('#0',width=20)
        tree.column('1',width=20)
        tree.column('2',width=20)
        tree.column('3',width=20)
        
        tree.heading("#0",text = "num",anchor='c')
        tree.heading("1",text = "id",anchor='w')
        tree.heading("2",text = "quantite",anchor='c')
        tree.heading("3",text = "typee",anchor='w')
        
        E=produit()
        rows=E.afficherproduit()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}'))
            j+=1
    def chercher(self):
    
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('800x400')
        self.root.title("recherche")
        show_frame = Frame(self.root)
        show_frame.place(width = 1000,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "recherche")
        labl_show.pack()   


        #========================Main Frame
        x= Frame(self.root,bd = 10,relief = SUNKEN)
        x.place(width = 800,height = 300,x = 8,y = 58)
        tree = ttk.Treeview(x,height = 200)
        vsb = ttk.Scrollbar(x,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3")
        tree.column('#0',width=20)
        tree.column('1',width=20)
        tree.column('2',width=60)
        tree.column('3',width=60)

        tree.heading("#0",text = "num",anchor='c')
        tree.heading("1",text = "id",anchor='w')
        tree.heading("2",text = "quantite",anchor='w')
        tree.heading("3",text="type",anchor='w')
        E=produit()
        rows=E.rechercher(self.cher.get())
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}'))
            j+=1
        
        
root = Tk()
l = gestionproduit(root)
root.mainloop()

