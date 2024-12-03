# ABInBev E-commerce API

This is an E-commerce API built with FastAPI based in Clean Architecture. It provides various endpoints for managing clients, authentication, products, carts, and orders.

## Implementation Details

For more information about the implementation, please refer to the [report.md](report.md) file.

## Highlights

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.10+.
- **Clean Architecture**: Organized into routes, entities, repositories, use cases, and utilities.
- **Exception Handling**: Custom exception handlers for HTTP exceptions, validation errors, and general exceptions.
- **Testing**: Includes unit tests using pytest.

## Project Structure

The project is organized into the following directories:
* src: Contains the source code for the API.
    * `entities`: Contains the Entities used for communication, those objects does not represent exactly what is stored in the database.
    * `repositories`: Contains the data access layer for interacting with the database.
    * `models`: Contains the SQLModel classes that represent the database tables.
    * `routes`: Contains the FastAPI routers for the API endpoints.
    * `use_cases`: Contains the business logic for the API.
    * `utils`: Contains utility functions and classes used accross the project.

This `README.md` file provides an overview of the project, installation steps, how to run the application, and how to make requests to its routes.


## Getting Started

### Prerequisites

- Python 3.10+

### Installation

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Install test dependencies** (optional):
    ```sh
    pip install -r requirements-test.txt
    ```

### Running the Application

#### With Docker
1. Build the Docker image:

    ```sh
    docker build -t e-commerce-api .
    ```
2. Run the Docker container:
    ```sh
    docker run -d -p 8000:8000 e-commerce-api
    ```

#### Without Docker

1. **Start the FastAPI server**:
    ```sh
    uvicorn main:app --port 8000 --reload
    ```

The application will be accessible at `http://127.0.0.1:8000`.

### Making Requests

You can use tools like `curl`, `httpie`, or Postman to make requests to the API.

For Postman, you can import the collection from the `postman` directory.

to get more information about the routes, you can access the Swagger documentation at `http://127.0.0.1:8000/docs`.

#### Health Check

- **Endpoint**: `/health`
- **Method**: `GET`
- **Description**: Check the health status of the API.

    ```sh
    curl -X GET http://127.0.0.1:8000/health
    ```

#### Client Routes

- **Endpoint**: `/v1/clients`
- **Method**: `POST`.
- **Description**: Creates a new Client User.

    ```sh
    curl --location 'http://127.0.0.1:8000/v1/clients/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "username":"<username>",
        "password":"P4$$W0rd",
        "email":"<email>@mail.com"
    }'
    ```
  
#### Admin Routes

- **Endpoint**: `/v1/admin`
- **Method**: `POST`.
- **Description**: Creates a new Admin User.

    ```sh
    curl --location 'http://127.0.0.1:8000/v1/clients/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "username":"<username>",
        "password":"P4$$W0rd",
        "email":"<email>@mail.com"
    }'

#### Authentication Routes

- **Endpoint**: `/v1/auth`
- **Method**: `POST`
- **Description**: Authenticates the provided User.

    ```sh
    curl --location 'http://127.0.0.1:8000/v1/auth/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'username=<username>' \
    --data-urlencode 'password=<password>'
    ```

#### Product Routes

- **Endpoint**: `/v1/products`
- **Method**: `POST`.
- **Description**: Add a new product.

    ```sh
    curl --location 'http://127.0.0.1:8000/v1/products/' \
    --header 'Content-Type: application/json' \
    --data '{
        "product": {
            "name": <product_name>,
            "description": <product_description>,
            "price": <price>,
            "stock": <stock>
        },
        "token": {
            "access_token": <access_token>,
            "token_type": "bearer"
        }
    }'
    ```
  
- **Endpoint**: `/v1/products/<id>`
- **Method**: `PUT` and `DELETE`.
- **Description**: Updates or deletes the product with the provided ID.

    ```sh
    curl --location 'http://127.0.0.1:8000/v1/products/<product_id>' \
    --header 'Content-Type: application/json' \
    --data '{
        "product": {
            "name": <product_name>,
            "description": <product_description>,
            "price": <price>,
            "stock": <stock>
        },
        "token": {
            "access_token": <access_token>,
            "token_type": "bearer"
        }
    }'
    ```

#### Cart Routes

- **Endpoint**: `/v1/carts/item`
- **Method**: `PUT`, `DELETE`, etc.
- **Description**: Add or Removes items to the users cart.

    ```sh
    curl --location --request PUT 'http://127.0.0.1:8000/v1/orders/cart/item' \
    --header 'Content-Type: application/json' \
    --data '{
        "cart_item": {
            "product_id": <product_id>,
            "quantity": <quantity>,
            "user_id": <user_id>
        },
        "token": {
            "access_token": <access_token>,
            "token_type": "bearer"
        }
    }'
    ```
  
- **Endpoint**: `/v1/carts/items`
- **Method**: `PUT`, `DELETE`.
- **Description**: List or removes all items from the users cart.

    ```sh
    curl --location --request PUT 'http://127.0.0.1:8000/v1/orders/cart/item' \
    --header 'Content-Type: application/json' \
    --data '{
        "access_token": <access_token>,
        "token_type": "bearer"
    }'
    ```

#### Order Routes

- **Endpoint**: `/v1/orders`
- **Method**: `POST`, `GET`.
- **Description**: Make a new order or list all orders from the user.

    ```sh
    curl --location 'http://127.0.0.1:8000/v1/orders/' \
    --header 'Content-Type: application/json' \
    --data '{
        "access_token": <access_token>,
        "token_type": "bearer"
    }'
    ```
  
- **Endpoint**: `/v1/orders/<id>`
- **Method**: `GET`.
- **Description**: List the order with the provided ID.

    ```sh
    curl --location 'http://127.0.0.1:8000/v1/orders/' \
    --header 'Content-Type: application/json' \
    --data '{
        "access_token": <access_token>,
        "token_type": "bearer"
    }'
    ```
  


## Running Tests

To run the unit tests, use the following command:

```sh
pytest -V