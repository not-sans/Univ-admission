# 🎓 College Admissions Assistant (ScaleDown AI)

The **College Admissions Assistant** is a tool designed to solve the "information overload" problem in higher education. It takes dense university requirement documents and compresses them into high-signal summaries for students.

Using **ScaleDown AI**, the assistant strips away marketing "fluff" and extracts only the non-negotiable data points required for a successful application.

---

## 🏗️ The "Buckets of Truth" Framework
The assistant categorizes information into three pillars:

### 1. The Hard Gates (Eligibility & Metrics)
* **Objective:** Immediate "Yes/No" determination for the student.
* **Details:** Minimum GPA, SAT/ACT scores, and required prerequisite courses (Physics, Calculus, etc.).

### 2. The Narrative (The "Human" Element)
* **Objective:** Decoding the university's expectations.
* **Details:** Analysis of essay prompt themes (Leadership, Creativity) and Letter of Recommendation (LOR) requirements.

### 3. The Logistics (The Timeline)
* **Objective:** Preventing deadline panic.
* **Details:** Early Action vs. Regular Decision dates and application fees.

---

## 🛠️ Project Structure

```text
Univ/
├── main.py                 # Core logic & ScaleDown Pipeline
├── .env                    # Secure API Key storage
├── raw_university_data/    # Input: Original university .txt files
└── buckets_of_truth/       # Output: Compressed summaries
