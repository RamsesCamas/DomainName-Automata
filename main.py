from flask import Flask, request, redirect, url_for
from flask import render_template
from flask_bootstrap import Bootstrap
from auto_process import start_automata, get_domain

app = Flask(__name__,template_folder='templates')
bootstrap = Bootstrap(app)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        domain_name = request.form['domain_name'].replace(' ','')
        is_valid = start_automata(domain_name)
        result_url ='.result_domain'
        if is_valid:
            is_aviable = get_domain(domain_name)
            if is_aviable:
                return redirect(url_for(result_url,response='El nombre de dominio está disponible'))
            else:
                return redirect(url_for(result_url,response='El nombre de dominio no está disponible'))
        else:
            return redirect(url_for(result_url,response='El nombre NO es válido'))
        
    return render_template('index.html')

@app.route('/result')
def result_domain():
    result = request.args['response']
    return render_template('response.html',response=result)

if __name__ == '__main__':
    app.run(debug=True,port=9000)