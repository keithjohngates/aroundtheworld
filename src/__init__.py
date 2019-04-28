from flask import Flask, render_template
import folium

app = Flask(__name__)


@app.route("/")
def main():
    return render_template('home.html')


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/projects")
def projects():
    return render_template('projects.html')


@app.route("/map")
def map_page():
    # start_coords = (46.9540700, 142.7360300)
    # folium_map = folium.Map(location=start_coords, zoom_start=14)
    # folium_map.save('templates/mademap.html')
    return render_template('map.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)