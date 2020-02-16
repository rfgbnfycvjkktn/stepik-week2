from flask import Flask, render_template
import data_tour


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', data =data_tour)

# @app.route("/test/")
# def test():
#     return render_template('test.html', data =data_tour)

@app.route("/tour/<id>/")
def tour(id):
    return render_template('tour.html', id = int(id), data =data_tour)

@app.route("/departure/<departure>/")
def departure(departure):
    data_tour_2 = []
    for k, v in data_tour.tours.items():
        if v["departure"] == departure:
            v["id"] = k
            data_tour_2.append(v)

    return render_template('departure.html', dep = departure, data =data_tour, tours_clear = data_tour_2)

app.run()
