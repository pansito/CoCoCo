from flask import Flask, render_template 
app = Flask(__name__)
@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/dias')
def bar():
    
    return render_template('dias.html')
@app.route('/ecco')
def ecco():
    
    return render_template('ecco.html')
if __name__ == "__main__":
    app.run(debug=True)
