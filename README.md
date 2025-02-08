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
   git clone <repository_url>
   cd MyLocker
