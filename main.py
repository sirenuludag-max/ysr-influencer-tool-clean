from flask import Flask, request, render_template_string
from google import genai
import os

app = Flask(__name__)

# Gemini client using your Cloud Run env variable
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>YSR Influencer Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f6f7f9;
            padding: 40px;
            display: flex;
            justify-content: center;
        }
        .container {
            width: 600px;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        h1 {
            margin-top: 0;
            font-size: 26px;
            text-align: center;
        }
        input[type=text] {
            width: 100%;
            padding: 14px;
            font-size: 16px;
            border-radius: 8px;
            border: 1px solid #ccc;
            margin-bottom: 20px;
        }
        button {
            width: 100%;
            padding: 14px;
            font-size: 16px;
            border-radius: 8px;
            background: #3164ff;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background: #224ed1;
        }
        .result-box {
            white-space: pre-wrap;
            background: #fafafa;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            border: 1px solid #ddd;
            font-size: 15px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>YSR Influencer Tool</h1>
        <form method="post">
            <input type="text" name="handle" placeholder="Enter an Instagram handle…">
            <button type="submit">Analyse</button>
        </form>

        {% if result %}
            <div class="result-box">{{ result }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result_text = None

    if request.method == "POST":
        handle = request.form.get("handle", "").strip()

        if not handle:
            result_text = "Please enter a handle."
        else:
            try:
                # SIMPLE GEMINI TEST ONLY — no tribes yet
                response = client.models.generate_content(
                    model="gemini-1.5-flash",
                    contents=f"Say hello to the user who searched for: {handle}"
                )
                result_text = response.text

            except Exception as e:
                result_text = f"Error talking to Gemini API: {str(e)}"

    return render_template_string(HTML_TEMPLATE, result=result_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
