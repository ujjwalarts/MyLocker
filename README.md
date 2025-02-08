# MyLocker

MyLocker is a Django-based web application designed to securely upload, share, view, and verify documents. It utilizes AWS S3 for cloud storage to manage uploaded files and supports user authentication for secure access.

![image](https://github.com/user-attachments/assets/fffe780f-27c4-4e86-9418-6b70446ec262)
![image](https://github.com/user-attachments/assets/475fa69c-0794-434d-9b92-6fc3157761d1)
![image](https://github.com/user-attachments/assets/591e6d43-96f3-442e-909f-8af221d99c7d)
![image](https://github.com/user-attachments/assets/0aae5d84-9971-4533-b3c5-8ca044525693)





## Features

- **User Authentication**:
  - Signup, Login, and Logout functionality.
  - Secure access for authorized users only.
- **Document Management**:
  - Upload documents securely to **AWS S3**.
  - View and verify uploaded documents.
  - Generate QR codes for shared documents.
- **Dark Mode**:
  - Includes a sleek, modern dark theme for improved usability.

## Technology Stack

- **Backend**:
  - Django
  - Django REST Framework
  - AWS S3 (via `django-storages`)
- **Frontend**:
  - HTML, CSS, Bootstrap
- **Others**:
  - QR Code generation using `qrcode.js`.

## Installation and Setup

### Prerequisites
- Python 3.10+
- pip (Python package manager)
- AWS account with an S3 bucket set up
- Virtual Environment (Recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/ujjwalarts/MyLocker.git
   cd MyLocker
   
2. Create and Activate a Virtual Environment:

    ```bash
    
    python -m venv env
    env\Scripts\activate  # On Windows
    # OR
    source env/bin/activate  # On Linux/Mac

3. Configure AWS S3: Update the settings.py file with your AWS credentials and bucket details:
      
      ```bash
      AWS_ACCESS_KEY_ID = 'your-access-key-id'
      AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
      AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
      AWS_S3_REGION_NAME = 'your-region'

4. Run Database Migrations:
      ```bash
      python manage.py makemigrations
      python manage.py migrate

6. Start the Development Server:
      ```bash
      python manage.py runserver

7. Access the Application: Open your browser and navigate to:
http://127.0.0.1:8000/
