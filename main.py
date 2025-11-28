from flask import Flask, request, render_template_string
import google.genai as genai
import os

app = Flask(__name__)

# Load Gemini API key from environment variable
API_KEY = os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=API_KEY)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>YSR Influencer Tool</title>
</head>
<body>
    <h1>YSR Influencer Tool</h1>
    <form method="post">
        <input type="text" name="handle" placeholder="Enter an Instagram handle…">
        <button type="submit">Analyse</button>
    </form>
    {% if result %}
        <pre>{{ result }}</pre>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result_text = None

    if request.method == "POST":
        handle = request.form.get("handle", "").strip()

        try:
            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=f"Say hi to {handle}"
            )

            result_text = response.text

        except Exception as e:
            result_text = f"Error communicating with Gemini: {e}"

    return render_template_string(HTML_TEMPLATE, result=result_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
