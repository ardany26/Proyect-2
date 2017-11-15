from flask import Flask
from flask import request, redirect, url_for, render_template, flash

app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

u = open("usuarios.txt", "r")
users = u.readlines()
u.close()
usuarios = []
i = 0
while(i < len(users)):
    usuario = users[i]
    i = i + 1
    usuarios = usuarios + usuario.split(" ")
print(usuarios)

c = open("contraseñas.txt", "r")
psw = c.readlines()
u.close()
contraseñas = []
x = 0
while(x < len(psw)):
    contraseña = psw[x]
    x = x + 1
    contraseñas = contraseñas + contraseña.split(" ")
print(contraseñas)

Mensajes = []
contador = 0


@app.route('/', methods=['GET','POST'])
def index():

    global usuario, usuarios, contraseñas, contador
    
    error = None
    if(request.method == 'POST'):
        if (request.form['entrar'] == "Entrar"):
            if(request.form['nombre'] != "" and request.form['pswd'] != ""):
                usuario = (request.form['nombre'],request.form['pswd'])
                i = 0
                while(i < len(usuarios)):
                    contador = i
                    if(usuario[0] == usuarios[i] and usuario[1] == contraseñas[i]):
                        return redirect(url_for('who'))
                    i = i + 1
                else: 
                    error = "Usuario y/o contraseña incorrectos"
            else:
                error = "No ha introducido datos"

    return render_template('index.html', error=error)

@app.route('/Registro', methods=['GET','POST'])
def registro():

    global usuario, pswd, usuarios, contraseñas

    if(request.method == "POST"):
        usuario = request.form['nombre']
        pswd = request.form['pswd']
        f = open("usuarios.txt", "r")
        texto = f.readlines()
        f.close()
        usuarios = (texto[0]).split()
        g = open("contraseñas.txt", "r")
        texto = g.readlines()
        g.close()
        contraseñas = (texto[0]).split()
        if not(usuario in usuarios):
            f = open("usuarios.txt", "a")
            f.write(" " + usuario + " ")
            f.close()
            if not(pswd in contraseñas):
                g = open("contraseñas.txt", "a")
                g.write(" " + pswd + " ")
                g.close()
                return redirect(url_for('chat'))

    return render_template('registro.html')

@app.route('/Who', methods=['GET','POST'])
def who():
    
    global usuarios, Mensajes, chat

    error = None
    if(request.method == "POST"):
        if(request.form['abrir'] == "Abrir conversación"):
            if(request.form['who'] != ""):
                chat = request.form['who']
                i = 0
                while(i < len(usuarios)):
                    if(chat == usuarios[i]):
                        Mensajes.append([])
                        return redirect(url_for('chat'))
                    i = i + 1
                else:
                    error = "Ingrese Nombre de usuario"

    return render_template('Who.html', error=error)

@app.route('/Chat', methods=['GET','POST'])
def chat():
    
    global usuarios, contraseñas, Mensajes, contador, chat

    if(request.method == 'POST'): 
        if(request.form['mensaje'] != ""):
            mensaje = (chat, request.form['mensaje'])
            i = 0
            while(i < len(usuarios)):
                if(usuarios[i] == mensaje[1]):
                    Mensajes.append(request.form['mensaje'])
                i = i + 1

    entries = {'datos1' : request.form["nombre"], 'datos2' : Mensajes[contador], 'datos3' : chat}
    
    return render_template('Chat.html', entries=entries)
        

if __name__ == '__main__':
    app.run(debug=True, port=9000)
 

