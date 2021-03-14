import mysql.connector
def connect_BD():
    mydb = mysql.connector.connect(
        host="localhost",
        user="hamza",
        password="zapatista2007",
        database="gestionpatisserie"
        )
    return mydb

"""#Programme principal:
db=connect_BD()
mycursor = db.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS commande(id INT PRIMARY KEY, nom VARCHAR(255), prenom VARCHAR(255) , telephone INT,mail VARCHAR(255),adresse VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)"""

class commande:
    db=connect_BD()
    mycursor=db.cursor()
    def __init__(self,i=0,nom='',prenom='',telephone=0,mail='',adresse=''):
        self.id=i
        self.nom=nom
        self.prenom=prenom
        self.telephone=telephone
        self.mail=mail
        self.adresse=adresse
        
    def ajoutercommande(self):
        sql="INSERT INTO commande (id,nom,prenom,telephone,mail,adresse) VALUES (%s,%s,%s,%s,%s,%s) "


        val=(self.id,self.nom,self.prenom,self.telephone,self.mail,self.adresse)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"AJOUT FAIS AVEC SUCCES")
    
    def affichercommande(self):
        self.mycursor.execute("SELECT * FROM commande ")
        resultat=self.mycursor.fetchall()
        return resultat
            
    def supprimercommande(self,other):
        sql="DELETE FROM commande WHERE id=%s"
        val=(other,)
        self.mycursor.execute(sql,val)
        self.db.commit()
        print(self.mycursor.rowcount,"suppression FAIS AVEC SUCCES")

    def rechercher(self,other):
        sql = "SELECT * FROM commande where nom like %s or prenom like %s "
        other='%'+other+'%'
        val=(other,other)
        self.mycursor.execute(sql,val)  
        rows = self.mycursor.fetchall()  
        return rows

    def modifiercommande(self,other):

        sql="UPDATE commande SET nom =%s, prenom =%s,telephone=%s,mail=%s,adresse=%s WHERE id= %s"
        val=(self.nom,self.prenom,self.telephone,self.mail,self.adresse,other)
        self.mycursor.execute(sql,val)  
        self.db.commit()
        print(self.mycursor.rowcount,"UPDATE FAIS AVEC SUCCES")
#programme principale
#a=commande()
#a.ajoutercommande()
#a.affichercommande()




from tkinter import *
import tkinter.ttk as ttk

class gestioncommande():
    def __init__(self,root):
        self.root = root
        self.root.geometry('800x600')
        self.root.title("Gestion patisserie")
        
        self.id=StringVar()
        self.nom=StringVar()
        self.prenom=StringVar()
        self.telephone=StringVar()
        self.mail=StringVar()
        self.adresse=StringVar()
        self.aux=StringVar()
  
        
  
        
    #Formulaire ajout Departement dans __init():
        #==============Num commande TEXTFIELD AND LABEL
        x = Label(self.root,text = "Id Unique",anchor='w')
        x.grid(row = 1,column = 0,padx = 40,pady = 40)
        y= Entry(self.root,textvariable = self.id)
        y.grid(row = 1,column = 1,ipady = 7,ipadx = 20,padx = 20)

        
        #=======================nom commandeLABEL AND TEXTFIELD
        x= Label(self.root,text="Nom",anchor='w')
        x.grid(row = 2,column = 0,pady = 40)
        y = Entry(self.root,textvariable = self.nom)
        y.grid(row = 2,column = 1,ipady = 7,ipadx = 20,padx = 20)
         #=======================prenom commande LABEL AND TEXTFIELD
        x= Label(self.root,text="Prenom",anchor='w')
        x.grid(row = 2,column = 2,pady = 40)
        y = Entry(self.root,textvariable = self.prenom)
        y.grid(row = 2,column = 3,ipady = 7,ipadx = 20,padx = 20)
         #=======================chef departement LABEL AND TEXTFIELD
        x= Label(self.root,text="telephone",anchor='w')
        x.grid(row = 3,column = 0,pady = 40)
        y = Entry(self.root,textvariable = self.telephone)
        y.grid(row = 3,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================chef departement LABEL AND TEXTFIELD
        x= Label(self.root,text="mail",anchor='w')
        x.grid(row = 3,column = 2,pady = 40)
        y = Entry(self.root,textvariable = self.mail)
        y.grid(row = 3,column = 3,ipady = 7,ipadx = 20,padx = 20)
        #=======================chef departement LABEL AND TEXTFIELD
        x= Label(self.root,text="adresse",anchor='w')
        x.grid(row = 4,column = 0,pady = 40)
        y = Entry(self.root,textvariable = self.adresse)
        y.grid(row = 4,column = 1,ipady = 7,ipadx = 20,padx = 20)
        #=======================chef departement LABEL AND TEXTFIELD
        x= Label(self.root,text="recherche",anchor='w')
        x.grid(row = 5,column = 0,pady = 40)
        y = Entry(self.root,textvariable = self.aux)
        y.grid(row = 5,column = 1,ipady = 7,ipadx = 20,padx = 20)




        
        #=====================Boutton Supprimer à ajouter après boutton "Afficher" dans __init()__
        x= Button(self.root,text = "Supprimer",command = self.remove,anchor='c')
        x.grid(row = 6,column = 1,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton affichage à ajouter après boutton "Ajouter" dans __init()__
        x= Button(self.root,text = "Afficher",command = self.view,anchor='c')
        x.grid(row = 6,column = 2,ipady = 4,ipadx = 13,pady = 40)
        #=====================Boutton chercher à ajouter après boutton "chercher" dans __init()__
        x= Button(self.root,text = "chercher",command = self.chercher,anchor='c')
        x.grid(row = 6,column = 6,ipady = 4,ipadx = 13,pady = 40)
        
        #=====================Boutton ajout
        x = Button(self.root,text = "Ajouter",command = self.add,anchor='c')
        x.grid(row = 6,column = 0,ipady = 4,ipadx = 13,pady = 40)

        #=====================Boutton modifier
        x = Button(self.root,text = "Modifier",command = self.modifier,anchor='c')
        x.grid(row = 6,column = 3,ipady = 4,ipadx = 13,pady = 40)
        
        

        
        #Fonction d'ajout d'un étudiant (sera appelée dérière le boutton "Ajouter"
    def add(self):
        E = commande(self.id.get(),self.nom.get(),self.prenom.get(),self.mail.get(),self.telephone.get(),self.adresse.get())
        print("commande: ",E.id)
        E.ajoutercommande()

        #Fonction dse suppression d'un étudiant sera appelée dans le boutton "Supprimer"  
    def remove(self):
        E = commande()
        E.supprimercommande(self.id.get())
    def modifier(self):
        E = commande(self.nom.get(),self.prenom.get(),self.mail.get(),self.telephone.get(),self.adresse.get())
        E.modifiercommande(self.id.get())
    def view(self):
        #self.root.title("Student Management(Details)")
        #==========================Show Frame
        self.root=Tk()
        self.root.geometry('800x400')
        self.root.title("Affichage des commandes")
        show_frame = Frame(self.root)
        show_frame.place(width = 1000,x = 0,y = 0 ,height = 300)
        labl_show = Label(show_frame,text = "Affichage des listes des commandes ")
        labl_show.pack()
          #========================Main Frame
        x= Frame(self.root,bd = 10,relief = SUNKEN)
        x.place(width = 800,height = 300,x = 8,y = 58)



        
        tree = ttk.Treeview(x,height = 200)
        vsb = ttk.Scrollbar(x,command = tree.yview,orient = "vertical")
        tree.configure(yscroll = vsb.set)
        vsb.pack(side = RIGHT,fill = Y)
        tree.pack(side = TOP,fill = X)
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=20)
        tree.column('1',width=20)
        tree.column('2',width=60)
        tree.column('3',width=60)
        tree.column('4',width=60)
        tree.column('5',width=50)
        tree.column('6',width=50)
        
        
       
        tree.heading("#0",text = "num",anchor='c')
        tree.heading("1",text = "id",anchor='w')
        tree.heading("2",text = "nom",anchor='w')
        tree.heading("3",text="prenom",anchor='w')
        tree.heading("4",text = "mail",anchor='c')
        tree.heading("5",text = "telephone",anchor='c')
        tree.heading("6",text = "adresse",anchor='c')
        E=commande()
        rows=E.affichercommande()
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
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
        tree['columns'] = ("1","2","3","4","5","6")
        tree.column('#0',width=20)
        tree.column('1',width=20)
        tree.column('2',width=60)
        tree.column('3',width=60)
        tree.column('4',width=60)
        tree.column('5',width=60)
        tree.column('6',width=60)
        
        
       
        tree.heading("#0",text = "num",anchor='c')
        tree.heading("1",text = "id",anchor='w')
        tree.heading("2",text = "nom",anchor='w')
        tree.heading("3",text="prenom",anchor='w')
        tree.heading("4",text = "telephone",anchor='c')
        tree.heading("5",text = "mail",anchor='c')
        tree.heading("6",text = "adresse",anchor='c')
        E=commande()
        rows=E.rechercher(self.aux.get())
        j=1
        for i in rows:
            tree.insert("","end",text=str(j), values = (f'{i[0]}',f'{i[1]}',f'{i[2]}',f'{i[3]}',f'{i[4]}',f'{i[5]}'))
            j+=1

        
        
root = Tk()
l = gestioncommande(root)
root.mainloop()
