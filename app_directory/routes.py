from app_directory import app


# @ is a decorator. route basically means address/path. "/" is the equivalent of the start page.
@app.route("/")
def index():
    return "Hello World!"

