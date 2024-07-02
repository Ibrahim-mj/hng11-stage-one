# Flask Weather API

This project sets up a basic web server using Flask that exposes an API endpoint to greet visitors and provide the current temperature of their location based on their IP address.

## Features

- Get the client's IP address.
- Determine the client's location (city) using their IP address.
- Fetch the current temperature for the client's location.
- Return a JSON response with the client's IP, location, and greeting message.

## Endpoint

### [GET] `/api/hello`

**Query Parameters:**

- `visitor_name` (optional): The name of the visitor. Defaults to "Guest" if not provided.

**Response:**

```json
{
  "client_ip": "127.0.0.1",
  "location": "New York",
  "greeting": "Hello, Guest! The temperature is 11 degrees Celsius in New York."
}
```

## Requirements

To run this project, you need to have the following installed:

- Python 3.x
- Flask
- Requests

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Ibrahim-mj/hng11-stage-one.git
```

2. Change into the project directory:

```bash
cd hng11-stage-one
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```
4. Add your seceret key and openweather api key to the .env file

## Usage

1. Start the Flask server:

```bash
flask runn
```

2. Open your browser and navigate to `http://localhost:5000/api/hello` to access the API endpoint.

3. You can also pass a `visitor_name` query parameter to customize the greeting message:

```bash
http://localhost:5000/api/hello?visitor_name=Mark
```