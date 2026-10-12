AI Resume ATS System

Project Description

AI Resume ATS System is a Python-based web application that helps users analyze their resumes against job requirements.

The application extracts text from a PDF resume, compares resume skills with the required job skills, and displays matched skills, missing skills, and an ATS-style score.

This project was built to learn Python, PDF text extraction, web application development, and Docker.

 Features

- Upload a resume in PDF format.
- Extract text from the resume.
- Compare resume skills with job requirements.
- Display matched skills.
- Identify missing skills.
- Calculate an ATS-style matching score.
- Run the application using Streamlit.
- Package the application using Docker.

 Technologies Used

- Python — Programming language
- Streamlit — Web application interface
- pypdf — Extracting text from PDF files
- Docker — Packaging and running the application in a container
- Git and GitHub — Version control and code hosting

 How to Run the Project

 Install Dependencies

```bash
pip install -r requirements.txt
```

 Run the Application

```bash
python -m streamlit run app.py
```

 Open in Browser

After running the application, open the URL shown in the terminal. Usually: http://localhost:8501

 Run with Docker

 Build the Docker Image

```bash
docker build -t resume-ats .
```

 Run the Docker Container

```bash
docker run --name resume-ats-app -p 8501:8501 resume-ats
```

 Open the Application

Open http://localhost:8501 in your browser.

 Project Structure

```text
AI_Resume_ATS/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

Learning Outcomes

- Learned PDF text extraction using Python.
- Practiced resume skill matching and score calculation.
- Built a web interface using Streamlit.
- Learned Git and GitHub basics.
- Built and ran a Docker container.

 Future Improvements

- Improve resume skill matching.
- Support more resume formats.
- Improve the user interface.
- Deploy the application online.

 Author

Shiv Agnihotri
