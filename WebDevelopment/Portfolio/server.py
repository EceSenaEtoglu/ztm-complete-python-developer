import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/<string:page_path>")
def get_generic_route(page_path):
    return render_template(page_path)

def write_to_csv(data:dict):
    with open("database.csv", mode ="a") as file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_writer = csv.writer(file,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()  #returns data from frontend in dict
            write_to_csv(data)
            return redirect("thankyou.html")

        except:
            return "did not save to database"
    else:
        return "something went wrong, try again"

