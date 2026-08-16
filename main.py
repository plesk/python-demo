import platform
from importlib.metadata import version
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return (
        f"Hello, World!<br>"
        f"Python {platform.python_version()}<br>"
        f"Flask {version('flask')}"
    )

if __name__ == "__main__":
    app.run()
