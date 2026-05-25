from flask import Flask, render_template, request
from utils.heun_solver import heun_method
from utils.plotter import generate_plot

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/examples")
def examples():
    return render_template("examples.html")


@app.route("/calculator", methods=["GET", "POST"])
def calculator():

    results = None
    error = None
    graph = None

    if request.method == "POST":

        try:

            equation = request.form["equation"]

            x0 = float(request.form["x0"])
            y0 = float(request.form["y0"])
            h = float(request.form["h"])
            steps = int(request.form["steps"])

            results, x_values, y_values = heun_method(

                equation,
                x0,
                y0,
                h,
                steps

            )

            graph = generate_plot(x_values, y_values)
    
        except Exception as e:

            error = str(e)

    return render_template(

    "calculator.html",

    results=results,

    error=error,

    graph=graph

)


if __name__ == "__main__":
    app.run(debug=True)