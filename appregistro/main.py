from flask import Flask
from flask import render_template, request
from configlol import Config
import formslol
from modelslol import Pizzeria, db

app = Flask(__name__)
app.config.from_object(Config)



@app.route("/")
def inicio():
    return "Estas dentro del inicio"


#Ingresamos datos a la base de datos pizzeria
@app.route("/registro", methods =["GET", "POST"])
def registro():
    registro = formslol.CreateForm(request.form)
    print(registro.username.data)

    if request.method == "POST":
        user = Pizzeria(username = registro.username.data)
        
        #agregamos el dato y le hacemos commit
        db.session.add(user)
        db.session.commit()

    return render_template("registro.html", formulariolol = registro)

if __name__ == "__main__":

    db.init_app(app) 
    with app.app_context(): #con esto sincronizamos nuestra app y la db
        db.create_all()
    app.run() #al ejecutar este script se ejecuta la app.run
