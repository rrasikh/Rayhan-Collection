from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Example data for your collection
    products = [
        {"name": "Premium Uzbek Coat", "description": "Traditional embroidery with a modern cut."},
        {"name": "Silk Chiffon Hijab", "description": "Lightweight, breathable, and elegant."},
        {"name": "Handcrafted Ikat Outerwear", "description": "Authentic patterns from the heart of Uzbekistan."}
    ]
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)