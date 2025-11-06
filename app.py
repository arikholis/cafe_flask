
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Sample data for the cafe
MENU = [
    {"name": "Espresso", "price": 18000, "category": "Coffee", "desc": "Single shot, bold and rich."},
    {"name": "Americano", "price": 20000, "category": "Coffee", "desc": "Espresso with hot water."},
    {"name": "Cappuccino", "price": 25000, "category": "Coffee", "desc": "Espresso with steamed milk & foam."},
    {"name": "Latte", "price": 26000, "category": "Coffee", "desc": "Smooth espresso with milk."},
    {"name": "Matcha Latte", "price": 28000, "category": "Non-Coffee", "desc": "Premium matcha, creamy and mellow."},
    {"name": "Lemon Tea", "price": 18000, "category": "Tea", "desc": "Fresh lemon, fragrant tea."},
    {"name": "Croissant", "price": 22000, "category": "Pastry", "desc": "Buttery, flaky layers."},
    {"name": "Chocolate Cake", "price": 30000, "category": "Dessert", "desc": "Rich cocoa slice."}
]

@app.template_filter('rupiah')
def rupiah(n):
    return f"Rp{n:,.0f}".replace(",", ".")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    # Group menu items by category
    categories = {}
    for item in MENU:
        categories.setdefault(item["category"], []).append(item)
    return render_template('menu.html', categories=categories)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


from flask import Flask, render_template, url_for

app = Flask(__name__)

# Sample data for the cafe
MENU = [
    {"name": "Espresso", "price": 18000, "category": "Coffee", "desc": "Single shot, bold and rich."},
    {"name": "Americano", "price": 20000, "category": "Coffee", "desc": "Espresso with hot water."},
    {"name": "Cappuccino", "price": 25000, "category": "Coffee", "desc": "Espresso with steamed milk & foam."},
    {"name": "Latte", "price": 26000, "category": "Coffee", "desc": "Smooth espresso with milk."},
    {"name": "Matcha Latte", "price": 28000, "category": "Non-Coffee", "desc": "Premium matcha, creamy and mellow."},
    {"name": "Lemon Tea", "price": 18000, "category": "Tea", "desc": "Fresh lemon, fragrant tea."},
    {"name": "Croissant", "price": 22000, "category": "Pastry", "desc": "Buttery, flaky layers."},
    {"name": "Chocolate Cake", "price": 30000, "category": "Dessert", "desc": "Rich cocoa slice."}
]

@app.template_filter('rupiah')
def rupiah(n):
    return f"Rp{n:,.0f}".replace(",", ".")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu():
    # Group menu items by category
    categories = {}
    for item in MENU:
        categories.setdefault(item["category"], []).append(item)
    return render_template('menu.html', categories=categories)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
    
if __name__ == "__main__":
    from os import environ
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 8000)))


