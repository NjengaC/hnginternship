# HNG12 Public API

## Description

This project is a public API developed using Flask that provides basic information including the registered email address, current datetime in ISO 8601 format (UTC), and the GitHub URL of the project's codebase.

## Technology Stack

- **Programming Language**: Python
- **Framework**: Flask
- **Deployment**: Heroku
- **CORS Handling**: Flask-CORS

## Setup Instructions

### Prerequisites

- Python 3.7 or later
- Git
- Heroku CLI (if deploying to Heroku)

### Running Locally

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/NjengaC/hnginternship.git
   cd hnginternship
```

2. **Set Up Virtual Environment**:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

4. **Run the Application**:

```bash
python app.py
```
5. **Access the API: Open http://127.0.0.1:5000/ in your browser or use curl**:

```bash
curl http://127.0.0.1:5000/
```
6. **Deployment**
The API is deployed on Heroku and can be accessed at:

```arduino
https://theactive.herokuapp.com/
```
## API Documentation
### Endpoint
- URL: https://your-app-name.herokuapp.com/
- Method: GET
### Request
- Headers: None required.
- Parameters: None.
### Response
- Content-Type: application/json
- Body:
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/hng12_public_api"
}
```

### Example Usage
```bash
curl https://your-app-name.herokuapp.com/
```
### Response:

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/hng12_public_api"
}
```
## Backlinks
Hire Python Developers

## License
This project is licensed under the MIT License
