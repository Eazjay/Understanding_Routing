from flask import Flask  

app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')
def say_dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_hi(name):
    print(name)
    return f"Hi, {name}!"

@app.route('/repeat/<word>/<int:num>')
def say_repeat(word, num):
    print(f"{word*num}\nThis word is repeated {num} times!!!")
    return word*num

if __name__=="__main__":
    app.run(debug=True)