# Example usage
import json
import sys
import os

sys.path.append(os.getcwd())



from daemon import WeApRous


def create_sampleapp():
    return WeApRous()

app = WeApRous()
@app.route("/", methods=["GET"])
def home(_):
    return {"message": "Welcome to the RESTful TCP WebApp"}

@app.route("/user", methods=["GET"])
def get_user(_):
    return {"id": 1, "name": "Alice", "email": "alice@example.com"}

@app.route("/echo", methods=["POST"])
def echo(body):
    try:
        data = json.loads(body)
        return {"received": data}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON"}

if __name__ == "__main__":
    print("Server starting on port 9000")
    app.prepare_address("0.0.0.0", 9000)
    app.run()