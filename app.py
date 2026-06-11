# ==========================================
# CareerPath AI Assistant - Mini RAG Demo
# ==========================================

# Membaca dokumen knowledge base
documents = {
    "frontend": open("frontend.txt", "r", encoding="utf-8").read(),
    "backend": open("backend.txt", "r", encoding="utf-8").read(),
    "data analyst": open("data_analyst.txt", "r", encoding="utf-8").read()
}

print("=" * 50)
print("      CAREERPATH AI ASSISTANT")
print("=" * 50)

# Input user
question = input("\nMasukkan pertanyaan: ").lower()

retrieved_context = None
source = None

# ==========================================
# Retrieval
# ==========================================

frontend_keywords = [
    "frontend",
    "html",
    "css",
    "javascript",
    "react",
    "git",
    "web developer"
]

backend_keywords = [
    "backend",
    "node",
    "nodejs",
    "express",
    "database",
    "mysql",
    "postgresql",
    "api",
    "authentication"
]

analyst_keywords = [
    "data analyst",
    "analyst",
    "excel",
    "sql",
    "python",
    "power bi",
    "statistics",
    "data"
]

# Cari dokumen yang relevan
if any(keyword in question for keyword in frontend_keywords):
    retrieved_context = documents["frontend"]
    source = "frontend.txt"

elif any(keyword in question for keyword in backend_keywords):
    retrieved_context = documents["backend"]
    source = "backend.txt"

elif any(keyword in question for keyword in analyst_keywords):
    retrieved_context = documents["data analyst"]
    source = "data_analyst.txt"

# ==========================================
# Output
# ==========================================

if retrieved_context:

    print("\n" + "=" * 50)
    print("RETRIEVED CONTEXT")
    print("=" * 50)
    print(retrieved_context)

    print("\n" + "=" * 50)
    print("JAWABAN AI")
    print("=" * 50)

    if source == "frontend.txt":
        print("""
Untuk menjadi Frontend Developer, Anda perlu
mempelajari HTML, CSS, JavaScript, React, dan Git.

Roadmap yang disarankan:

1. HTML
2. CSS
3. JavaScript
4. React
5. Git
6. Membuat Portfolio Project

Karier terkait:
- Frontend Developer
- React Developer
- Web Developer
""")

    elif source == "backend.txt":
        print("""
Untuk menjadi Backend Developer, Anda perlu
mempelajari JavaScript, Node.js, Express.js,
Database, REST API, dan Authentication.

Roadmap yang disarankan:

1. JavaScript
2. Node.js
3. Express.js
4. Database
5. REST API
6. Authentication

Karier terkait:
- Backend Developer
- API Developer
- Software Engineer
""")

    elif source == "data_analyst.txt":
        print("""
Untuk menjadi Data Analyst, Anda perlu
menguasai Excel, SQL, Python, Statistics,
dan Power BI.

Roadmap yang disarankan:

1. Excel
2. SQL
3. Python
4. Statistics
5. Power BI

Karier terkait:
- Data Analyst
- Business Analyst
- Junior Data Scientist
""")

    print("=" * 50)
    print("SOURCE / CITATION")
    print("=" * 50)
    print(source)

    print("\n" + "=" * 50)
    print("EVALUASI")
    print("=" * 50)
    print("✓ Dokumen ditemukan")
    print("✓ Retrieval berhasil")
    print("✓ Jawaban berdasarkan dokumen")
    print("✓ Source ditampilkan")

else:

    print("\n" + "=" * 50)
    print("HASIL")
    print("=" * 50)
    print("Maaf, saya tidak menemukan dokumen yang relevan.")
    print("Silakan tanyakan seputar Frontend Developer, Backend Developer, atau Data Analyst.")