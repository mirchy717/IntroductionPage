from flask import Flask, render_template

app = Flask(__name__) # create new Flask object

# CONTROLLER oz HANDLER -  usmerja promet na naši strani - od tukaj naprej se zadeva začne prikazovati uporabniku
@app.route("/") # poševnica = izhodišče strani, ki pelje na index.html - root
def index():
    return render_template("index.html")

@app.route("/interests") 
def interests():
    return render_template("interests.html")

@app.route("/gallery") 
def gallery():
    return render_template("gallery.html")

@app.route("/contact") 
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(use_reloader=True)


