from jd_parser import parse_jd
from flask import Flask, request, jsonify
from flask_cors import CORS
import json

from matcher import calculate_match
from scorer import simulate_interest

app = Flask(__name__)
CORS(app)

# Load candidates
with open("candidates.json") as f:
    candidates = json.load(f)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    jd_text = data.get("jd")

    jd_data = parse_jd(jd_text)

    results = []

    for candidate in candidates:
        match_score, explanation = calculate_match(candidate, jd_data)

        interest_label, interest_score = simulate_interest()

        final_score = (match_score * 0.6) + (interest_score * 0.4)

        results.append({
            "name": candidate["name"],
            "match_score": match_score,
            "interest_score": interest_score,
            "interest_label": interest_label,
            "final_score": round(final_score, 2),
            "explanation": explanation
        })

    results = sorted(results, key=lambda x: x["final_score"], reverse=True)

    return jsonify({
        "jd_data": jd_data,
        "results": results
    })

if __name__ == "__main__":
    app.run(debug=True)