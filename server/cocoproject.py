from cocoProject import app
from flask_ngrok import run_with_ngrok

if __name__ == "__main__":
    run_with_ngrok(app)
    app.run(host='0.0.0.0')