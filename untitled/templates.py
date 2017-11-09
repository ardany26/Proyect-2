from flask import Flask
from flask import request, g, redirect, url_for, render_template, flash

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


@app.route('/', methods=['GET','POST'])
def index():
    global usuarios, contraseñas
    error = None
    if(request.method == 'POST'):
        if (request.form['entrar'] == "Entrar"):
            if(request.form['nombre'] != "" and request.form['pswd'] != ""):
                usuario = (request.form['nombre'],request.form['pswd'])
                i = 0
                while(i < len(usuarios)):
                    if(usuario[0] == usuarios[i] and usuario[1] == contraseñas[i]):
                        return redirect(url_for('chat'))
                    i = i + 1
                else: 
                    error = "Usuario o contraseña incorrectos, intente de nuevo"
            else:
                error = "No ha introducido datos"

    return render_template('index.html', error=error)

@app.route('/Registro')
def registro():
    global usuarios, contraseñas
    return render_template('registro.html')

@app.route('/Chat')
def chat():
    global usuarios, contraseñas
    return render_template('Chat.html')
        

if __name__ == '__main__':
    app.run(debug = True, port=9000)
 

