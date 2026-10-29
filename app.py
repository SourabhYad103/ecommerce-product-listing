from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/product/<int:product_id>")
def product_details(product_id):
    conn = get_db_connection()

    product = conn.execute(
        "SELECT id FROM products WHERE id = ?",
        (product_id,)
    ).fetchone()

    conn.close()

    if product is None:
        return "Product not found", 404

    return render_template("product.html")



@app.route("/api/products", methods=["GET"])
def get_products():
    conn = get_db_connection()
    products = conn.execute("SELECT * FROM products").fetchall()
    conn.close()

    return jsonify([dict(product) for product in products]), 200


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    conn = get_db_connection()

    product = conn.execute(
        "SELECT * FROM products WHERE id = ?",
        (product_id,)
    ).fetchone()

    conn.close()

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(dict(product)), 200


if __name__ == "__main__":
    app.run(debug=True)
