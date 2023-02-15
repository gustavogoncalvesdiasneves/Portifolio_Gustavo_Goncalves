from flask import Flask, render_template

app = Flask(__name__)

# route = domion.com/route_aqui
# função = oque vai exibir na tela

@app.route("/")
def homepage():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
