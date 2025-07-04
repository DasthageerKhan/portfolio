import streamlit as st
from PIL import Image
import base64

# === Background image setup ===
def set_bg_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_bg_image("edited.png")

# === Page Config ===
st.set_page_config(page_title="Portfolio", layout="wide")

# === Title and Header ===
st.markdown("""
<style>
@keyframes typing {
  0% { width: 0 }
  50% { width: 30% }
  100% { width: 0 }
}

@keyframes blink {
  50% { border-color: transparent }
}

.typing-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  height: 80px;
  padding-left: 30px;
}

.typing-text {
  font-size: 3rem;
  font-weight: bold;
  color: white;
  white-space: nowrap;
  overflow: hidden;
  border-right: 3px solid white;
  animation: typing 6s steps(30, end) infinite, blink 0.75s step-end infinite;
}
</style>

<div class="typing-container">
  <div class="typing-text">Dasthageer Khan</div>
</div>
""", unsafe_allow_html=True)
# Add this before or near where you call the animated subtitle
st.markdown("""
<style>
@keyframes fadeSlide {
  0% {
    opacity: 0;
    transform: translateY(-20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
""", unsafe_allow_html=True)

# Then this animated subtitle will now work
st.markdown("""
<div style='text-align: left; color: lightgray; font-size: 1.2rem; animation: fadeSlide 3s ease forwards; opacity: 0; padding-left: 30px;'>
    Python Developer | UI/UX Designer | Automation Enthusiast
</div>
""", unsafe_allow_html=True)
st.markdown("---")

# === Contact Section ===
st.markdown("📞 *Phone:* 8309980142  ✉ *Email:* dasthgeerkhan07@gmail.com  📍 *Location:* Madanapalli, India")

# === About Me ===
st.subheader("About Me")
st.info(
    "I am a detail-oriented and efficient developer with a strong passion for Python GUI development and automation programming. "
    "I specialize in integrating front-end and back-end components, developing responsive interfaces, and designing user-centric systems. "
    "With real-world experience in automation tools, database integration, and cross-functional UI/UX design, I’m eager to streamline workflows and enhance digital experiences."
)

# === Skills ===
st.subheader("Skills")
st.markdown("""
- *Programming:* Python GUI, Automation, Database Integration  
- *Web Development:* HTML, CSS, JavaScript (Basic), Responsive Design  
- *UI/UX Design:* Figma, Wireframing, Prototyping, Front-end Best Practices  
- *Tools & Tech:* TtkBootstrap, CustomTkinter, PyQt6, Excel Data Automation  
- *Soft Skills:* Problem Solving, Creativity, Presentation, Team Collaboration  
""")

# === Education ===
st.subheader("Education")
st.markdown("""
- 🎓 *Bachelor’s in Computer Applications (BCA)* – Gnanambica Degree College – 2025 — 75%  
- 🏫 *PUC (12th Std)* – Krishna Reddy Junior College – 2022 — 62%  
- 🏫 *SSC (10th Std)* – Gnanodaya EM High School – 2020 — CGPA: 10  
""")

# === Internship ===
st.subheader("Internship Experience")
st.markdown("""
*Rossell Techsys Pvt. Ltd* (Jan 25 – June 6)  
- Developed multi-user interface using Python, HTML, CSS & JS with dynamic DB integration.  
- Built GUI automation tool for logistics data management with Excel import/export support.  
- Packaged Python apps into .EXE files for internal distribution.  
- Worked with ERP system modules and backend optimization.
""")

# === Projects ===
st.subheader("Projects")
st.markdown("""
- *Portfolio Website:* Responsive HTML/CSS website with front-end best practices.  
- *UI-based Data Manager:* Python tool for Excel processing and database integration.  
- *Login & Signup System:* Prototyped using Figma, optimized for desktop/mobile.  
""")

# === Certifications ===
st.subheader("Certifications")
st.markdown("""
- 🎓 UI/UX Kickstart Workshop – Growth School  
- 🎓 Codeathon Participation Certificate  
- 🎓 MySQL Workshop – WsCube Tech  
- 🎓 Data Analytics Job Simulation - Deloitte
""")

# === Extras ===
st.subheader("Extracurricular Activities")
st.markdown("""
- 🧠 Presented on OECD Cyber Law  
- 🎤 Anchored and organized cultural/technical events  
- 📸 Vlog content creator on YouTube  
""")

# === Footer ===
st.markdown("---")
st.markdown("*Languages:* English, Hindi, Urdu, Telugu  |  *Interests:* Video Creation, Anime, Exploring Places", unsafe_allow_html=True)
st.markdown("© 2025 Dasthageer Khan")
