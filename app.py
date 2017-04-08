from flask import Flask

app = Flask(__name__, static_url_path="")


# @app.route('/')
# def hello_world():
#     return "Welcome~ This is a website designed by Yu~"
@app.route('/')
def hello_world():
    return app.send_static_file("Apple.html")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
