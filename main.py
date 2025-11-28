from flask import Flask, request, render_template_string
from google import genai
import os

app = Flask(__name__)

# Gemini client using your API key from environment
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
