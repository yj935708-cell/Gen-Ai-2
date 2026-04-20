"""
knowledge_base.py
==================
Predefined FAQ knowledge base for TechVision Institute.
This gives instant responses without needing the API,
and also serves as context fed to the Gemini LLM.
"""

# ──────────────────────────────────────────────
# College Knowledge Base (fed to LLM as context)
# ──────────────────────────────────────────────
COLLEGE_INFO = """
COLLEGE: TechVision Institute of Engineering, Bangalore, Karnataka
ESTABLISHED: 2005
AFFILIATION: Visvesvaraya Technological University (VTU)
NAAC GRADE: A+
NBA ACCREDITED: Yes (CSE, ECE, ME)
TOTAL STUDENTS: ~4,500
CAMPUS SIZE: 25 acres

COURSES OFFERED (B.Tech - 4 years):
- Computer Science & Engineering (CSE) — 120 seats
- Artificial Intelligence & Machine Learning (AIML) — 60 seats
- Electronics & Communication Engineering (ECE) — 120 seats
- Mechanical Engineering (ME) — 60 seats
- Civil Engineering (CE) — 60 seats
- Information Science & Engineering (ISE) — 60 seats

POSTGRADUATE (M.Tech - 2 years):
- Computer Science — 18 seats
- VLSI Design — 18 seats
- Machine Design — 18 seats

FEE STRUCTURE (Per Year):
- CSE / AIML / ISE: ₹1,20,000
- ECE: ₹1,10,000
- ME / CE: ₹1,00,000
- M.Tech: ₹80,000
- Hostel Fee: ₹70,000/year (AC), ₹50,000/year (Non-AC)
- Mess Charges: ₹36,000/year (approx.)

SCHOLARSHIPS:
- Government of Karnataka scholarship (SC/ST/OBC)
- Merit scholarship: Top 5 rank holders get 50% fee waiver
- Management scholarship: Up to ₹30,000/year for meritorious students
- EWS scholarship available

ADMISSION PROCESS:
- Eligibility: 10+2 / PUC with Physics, Chemistry, Maths (PCM)
- Minimum marks: 45% aggregate (40% for SC/ST)
- Entrance exam: KCET (Karnataka CET) or COMEDK
- Management quota: Direct admission via college counselling
- NRI/OCI quota: Available (separate fee structure)
- Documents needed: 10th, 12th marksheets, transfer certificate,
  character certificate, KCET/COMEDK scorecard, passport photos, Aadhaar

IMPORTANT DATES (2024-25):
- KCET Registration: February - March 2025
- KCET Exam: April 2025
- College Counselling: June - July 2025
- Semester start: August 2025
- Last date for admission: September 15, 2025

HOSTEL FACILITIES:
- Separate hostels for boys and girls
- 24/7 security with CCTV
- Wi-Fi enabled campus
- Mess with vegetarian and non-vegetarian options
- Laundry facility
- Indoor games room, gym
- Medical room with nurse on duty
- 300 students capacity (Boys), 200 students capacity (Girls)

CAMPUS FACILITIES:
- Central Library: 50,000+ books, e-journals, NPTEL access
- Computer Labs: 600+ systems, latest software
- Advanced Research Labs: AI/ML Lab, IoT Lab, Robotics Lab
- Auditorium: 1,200 seat capacity
- Sports: Cricket ground, basketball court, football field, badminton, table tennis
- Cafeteria and food courts
- ATM (SBI, HDFC)
- Transport: College buses from 15+ routes in Bangalore

PLACEMENTS:
- Placement rate: 92% (2023-24)
- Highest package: ₹32 LPA (Microsoft)
- Average package: ₹8.5 LPA
- Top recruiters: Google, Microsoft, Amazon, Infosys, TCS, Wipro,
  Accenture, IBM, Cognizant, Bosch, Siemens, L&T
- Companies visited: 150+ per year
- Internship tie-ups: 80+ companies

FACULTY:
- Total faculty: 180+
- PhD holders: 65%
- Average experience: 12 years
- Student-faculty ratio: 20:1

RESEARCH & INNOVATION:
- Patents filed: 28 (2020-2024)
- Research papers published: 400+ in Scopus/SCI journals
- DST-funded projects: 5 ongoing
- Innovation Cell and Startup Incubator on campus

CONTACT:
- Address: TechVision Campus, Yelahanka, Bangalore - 560064
- Phone: +91-98765-43210
- Email: admissions@techvision.edu.in
- Website: www.techvision.edu.in
- Admissions office hours: Mon-Sat, 9:00 AM - 5:00 PM
"""

# ──────────────────────────────────────────────
# FAQ Dictionary (keyword → answer)
# ──────────────────────────────────────────────
FAQ = {
    # Courses
    "courses": """**Courses offered at TechVision Institute:**

**B.Tech (4 years):**
- Computer Science & Engineering (CSE)
- AI & Machine Learning (AIML)
- Electronics & Communication (ECE)
- Mechanical Engineering (ME)
- Civil Engineering (CE)
- Information Science & Engineering (ISE)

**M.Tech (2 years):**
- Computer Science, VLSI Design, Machine Design

Affiliated to VTU, Bangalore. NBA & NAAC A+ accredited.""",

    "fee": """**Fee Structure (Per Year):**

| Program | Annual Fee |
|---------|-----------|
| CSE / AIML / ISE | ₹1,20,000 |
| ECE | ₹1,10,000 |
| ME / CE | ₹1,00,000 |
| M.Tech | ₹80,000 |
| Hostel (AC) | ₹70,000 |
| Hostel (Non-AC) | ₹50,000 |
| Mess charges | ₹36,000 (approx.) |

💡 Scholarships and EMI options are available!""",

    "admission": """**Admission Process:**

1. ✅ Complete 10+2 / PUC with PCM (min. 45% marks)
2. ✅ Appear for **KCET** or **COMEDK** entrance exam
3. ✅ Participate in counselling based on rank
4. ✅ Management quota: Direct admission available
5. ✅ Submit required documents and pay fees

**Documents needed:** 10th & 12th marksheets, TC, CC, CET scorecard, Aadhaar, photos.

📞 Call us: +91-98765-43210""",

    "hostel": """**Hostel Facilities:**

🏠 Separate hostels for boys (300 seats) and girls (200 seats)

**Amenities:**
- 24/7 security + CCTV surveillance
- High-speed Wi-Fi
- Veg & Non-veg mess
- Gym, indoor games, laundry
- Medical room with nurse
- Warden on duty round the clock

**Fees:**
- AC Hostel: ₹70,000/year
- Non-AC Hostel: ₹50,000/year
- Mess: ~₹36,000/year""",

    "placement": """**Placement Statistics (2023-24):**

- 🎯 Placement Rate: **92%**
- 💰 Highest Package: **₹32 LPA** (Microsoft)
- 📊 Average Package: **₹8.5 LPA**
- 🏢 Companies visited: **150+**

**Top Recruiters:**
Google, Microsoft, Amazon, Infosys, TCS, Wipro, Accenture, IBM, Bosch, Siemens

**Internship tie-ups:** 80+ companies""",

    "scholarship": """**Scholarships Available:**

- 🎓 **Government Scholarship** – SC/ST/OBC students (Karnataka Govt.)
- ⭐ **Merit Scholarship** – Top 5 rank holders get 50% fee waiver
- 💡 **Management Scholarship** – Up to ₹30,000/year
- 🏛️ **EWS Scholarship** – For economically weaker sections

Apply during admission. Contact the Financial Aid Office for details.""",

    "contact": """**Contact TechVision Institute:**

📍 TechVision Campus, Yelahanka, Bangalore - 560064
📞 Phone: +91-98765-43210
📧 Email: admissions@techvision.edu.in
🌐 Website: www.techvision.edu.in
🕘 Office Hours: Mon–Sat, 9:00 AM – 5:00 PM""",

    "date": """**Important Dates (2024-25):**

| Event | Date |
|-------|------|
| KCET Registration | Feb – Mar 2025 |
| KCET Exam | April 2025 |
| Counselling | June – July 2025 |
| Semester starts | August 2025 |
| Last date for admission | Sept 15, 2025 |""",
}

# Keywords mapped to FAQ keys
KEYWORD_MAP = {
    "course": "courses",
    "program": "courses",
    "branch": "courses",
    "stream": "courses",
    "btech": "courses",
    "mtech": "courses",
    "engineering": "courses",
    "fee": "fee",
    "fees": "fee",
    "cost": "fee",
    "tuition": "fee",
    "charges": "fee",
    "money": "fee",
    "admission": "admission",
    "apply": "admission",
    "eligibility": "admission",
    "entrance": "admission",
    "kcet": "admission",
    "comedk": "admission",
    "document": "admission",
    "hostel": "hostel",
    "accommodation": "hostel",
    "room": "hostel",
    "stay": "hostel",
    "mess": "hostel",
    "placement": "placement",
    "job": "placement",
    "salary": "placement",
    "package": "placement",
    "recruit": "placement",
    "company": "placement",
    "scholarship": "scholarship",
    "financial": "scholarship",
    "discount": "scholarship",
    "free": "scholarship",
    "contact": "contact",
    "phone": "contact",
    "email": "contact",
    "address": "contact",
    "location": "contact",
    "date": "date",
    "deadline": "date",
    "when": "date",
    "last date": "date",
    "schedule": "date",
}


def get_faq_answer(query: str) -> str | None:
    """
    Check if the user query matches any FAQ keyword.
    Returns the predefined answer string, or None if no match.
    """
    query_lower = query.lower()
    for keyword, faq_key in KEYWORD_MAP.items():
        if keyword in query_lower:
            return FAQ.get(faq_key)
    return None
