from flask import Flask, render_template, request
from database import get_db

app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def check_login():

    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "1234":
        return render_template("home.html")

    else:
        return "Invalid Login"



@app.route("/estimate", methods=["GET", "POST"])
def estimate():

    if request.method == "POST":

        product = request.form["product"]
        quantity = int(request.form["quantity"])
        price = int(request.form["price"])
        expected = int(request.form["expected"])


        total = quantity * price


        if total < expected:
            status = "Reasonable Price"

        elif total <= expected + 10000:
            status = "Slightly High Price"

        else:
            status = "Too High Price"



        db = get_db()

        db.execute(
            "INSERT INTO estimate(product, price, date_time) VALUES(?,?,datetime('now'))",
            (product, total)
        )

        db.commit()



        return render_template(
            "result.html",
            product=product,
            total=total,
            status=status
        )


    return render_template("estimate.html")




@app.route("/history")
def history():

    db = get_db()

    data = db.execute(
        "SELECT * FROM estimate"
    ).fetchall()


    return render_template(
        "history.html",
        data=data
    )



if __name__ == "__main__":
    app.run(debug=True)