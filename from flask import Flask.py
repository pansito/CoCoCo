from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def home():
    
    return render_template('index.html',name='Congreso Colombiano de Combinatoria')

@app.route('/dias')
def bar():
    
    return render_template('dias.html',name='Dias Combinatoria')
@app.route('/ecco')
def ecco():
    return render_template('ecco.html', name='ECCO')
if __name__ == "__main__":
    app.run(debug=True, port=8001)
