from flask import Flask, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run-script")
def run_script():
    # Run Selenium script
    record = get_trending_topics()
    if record:
        return jsonify(record)
    else:
        return jsonify({"error": "Failed to fetch trending topics"})

def get_trending_topics():
    # Placeholder function to simulate fetching trending topics
    return {"topics": ["topic1", "topic2", "topic3"]}

if __name__ == "__main__":
    app.run(debug=True)
