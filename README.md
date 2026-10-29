# E-Commerce Product Listing Website

## 1. Project Description

This project is a basic e-commerce website developed using Python Flask, SQLite, HTML, CSS, and JavaScript.

Users can browse products, view product details, and search for products.

## 2. Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- JavaScript
- Git

## 3. Project Structure

```text
ecommerce/
├── app.py
├── init_db.py
├── database.db
├── README.md
├── templates/
│   ├── index.html
│   └── product.html
└── static/
    ├── style.css
    └── images/
```

## 4. Prerequisites

- Python 3
- Python virtual environment support
- pip

## 5. Installation and Setup

Open a terminal and navigate to the project directory.

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install Flask:

```bash
pip install Flask
```

Initialize the database:

```bash
python init_db.py
```

**Note:** The current `init_db.py` inserts five sample products each time it runs. If the database is already initialized, avoid running this command again until duplicate insertion has been prevented.

## 6. Run the Application

Activate the virtual environment:

```bash
source venv/bin/activate
```

Start the Flask server:

```bash
python app.py
```

Open a browser and visit:

http://127.0.0.1:5000/

## 7. API Endpoints

### Get All Products

`GET /api/products`

Returns all products as JSON.

### Get a Single Product

`GET /api/products/<product_id>`

Returns the product with the specified ID.

If the product does not exist, the API returns a 404 response.

## 8. Database

The application uses SQLite to store product information.

The `products` table contains:

- `id`: Unique product identifier
- `name`: Product name
- `description`: Product description
- `price`: Product price
- `image`: Product image filename

## 9. Application Architecture

The frontend uses HTML, CSS, and JavaScript to display products and provide search functionality.

The Flask backend handles page requests and API endpoints. It retrieves product information from the SQLite database and returns the data to the frontend as JSON.

The frontend communicates with the backend rather than accessing the database directly.

## 10. Features

- Product listing
- Product details page
- Product search
- SQLite database integration
- REST-style GET API endpoints
- Handling of nonexistent products
