from app.init import app


@app.route("/")
def home():
    return "Hello, CI/CD with Canary Deployment!"