import streamlit as st
from pypdf import PdfReader

st.title("AI Resume ATS System")
uploaded_file = st.file_uploader("Upload your Resume PDF", type=["pdf"])
if uploaded_file is not None:
    st.success("Resume uploaded sucessfully!")
    pdf = PdfReader(uploaded_file)

# -----------------------------
# 1. Read Resume PDF
# -----------------------------


    resume_text = ""

    for page in pdf.pages:
        text = page.extract_text()
        resume_text = resume_text + text


# -----------------------------
# 2. Clean Resume Text
# -----------------------------

        resume_text = resume_text.lower()
        resume_text = resume_text.strip()
        resume_text = resume_text.replace("-", " ")

    print("Resume text cleaned successfully.")


    # -----------------------------
    # 3. Job Description
    # -----------------------------

    job_description = """
    We are looking for a Python developer with skills in
    Python, SQL, Machine Learning, Git, Docker and Pandas.
    """


    # -----------------------------
    # 4. Available Skills
    # -----------------------------

    available_skills = [
        "Python",
        "SQL",
        "Machine Learning",
        "Git",
        "Docker",
        "Pandas",
        "NumPy"
    ]


    # -----------------------------
    # 5. Find Required Skills
    # -----------------------------

    required_skills = []

    for skill in available_skills:
        if skill.lower() in job_description.lower():
            required_skills.append(skill)

    print("Required Skills:", required_skills)


    # -----------------------------
    # 6. Skill Aliases
    # -----------------------------

    skill_aliases = {
        "machine learning": "ml",
        "artificial intelligence": "ai",
        "natural language processing": "nlp"
    }


    # -----------------------------
    # 7. Match Resume with Job
    # -----------------------------

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        skill_lower = skill.lower()

        alias = skill_aliases.get(skill_lower)

        if skill_lower in resume_text or (alias and alias in resume_text):
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)


    # -----------------------------
    # 8. Print Matched / Missing
    # -----------------------------

    print("Matched Skills:", matched_skills)
    print("Missing Skills:", missing_skills)


    # -----------------------------
    # 9. Calculate ATS Score
    # -----------------------------

    match_percentage = (len(matched_skills) / len(required_skills)) * 100

    print("ATS Match Score:", round(match_percentage, 2), "%")
    st.subheader("ATS Score")
    st.metric("ATS Match Score", f"{round(match_percentage,2)}%")
    print("\n===== ATS REPORT ====")
    print("ATS Score:", round(match_percentage,2), "%")
    print("Matched Skills: ", matched_skills)
    st.subheader("Matched Skills")
    # st.write("Matched Skills:", matched_skills)
    st.subheader("Matched SKills")

    for skill in matched_skills:
         st.write(".", skill)
    print("Missing Skills:", missing_skills)
    st.subheader("Missing Skills")
    # st.write("Missing Skills:", missing_skills)
    st.subheader("Missing SKills")

    for skill in missing_skills:
            st.write(".", skill)
    # print("Suggestion: Improve these missing skills.")
    print("Suggestion: Improve:", missing_skills)
    # st.subheader("Suggestion")
    # st.write("Improve these skills:", missing_skills)
    st.subheader("Suggestions")

    if len(missing_skills) > 0:
         st.write("You should improve these skills:")

         for skill in missing_skills:
              st.write(".", skill)
    else :
         st.write("Great ! No important skills are missing.")
    print("Total Matched Skills:", len(matched_skills))
    print("Total Missing Skills:", len(missing_skills))
    st.write("Total Matched Skills:", len(matched_skills))
    st.write("Total Missing Skills:", len(missing_skills))

    print("Total Matched Skills:", len(matched_skills))
    print("Total Missing Skills:", len(missing_skills))