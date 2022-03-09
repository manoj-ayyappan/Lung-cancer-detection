from flask import Flask, render_template
app = Flask(__name__, template_folder="templates")

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ =="__main__":  
    app.run(debug = True)  
    
@app.route('/upload/')
def upload():
    return render_template('upload.html')
    
@app.route('/login/')
def login():
    return render_template('login.html')
    
@app.route('/delete/')
def delete():
    return render_template('delete.html')