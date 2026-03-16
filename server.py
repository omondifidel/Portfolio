from flask import Flask, render_template , request,redirect

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static",
)  # This 'app' variable is what Flask is looking for!


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/works")
def works():
    return render_template("works.html")


@app.route("/work")
def work():
    return render_template("work.html")


@app.route("/work2")
def work2():
    return render_template("work2.html")


@app.route("/work3")
def work3():
    return render_template("work3.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_file(data)
        # Render a template or redirect to a route rather than a static file path
        return redirect("/thankyou")
    else:
        return "Something went wrong. Try again!"

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n{email},{subject},{message}")


if __name__ == "__main__":
    app.run(debug=True)