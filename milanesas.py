from flask import Flask, render_template
 
app = Flask("danico")

@app.route("/")
def hello_word():
    return render_template("index.html")

if  __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)