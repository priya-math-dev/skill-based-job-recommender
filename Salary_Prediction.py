import matplotlib.pyplot as plt

# ------------------------
# Job roles with skills, salary, companies
# ------------------------
jobs = {
    "Data Analyst": {
        "skills": ["Python", "SQL", "Excel", "Statistics"],
        "salary": "4 - 7 LPA",
        "companies": ["TCS", "Infosys", "Accenture"]
    },
    "Python Developer": {
        "skills": ["Python", "OOP", "Django", "API"],
        "salary": "5 - 9 LPA",
        "companies": ["Zoho", "Freshworks", "Cognizant"]
    },
    "Data Scientist": {
        "skills": ["Python", "Machine Learning", "Statistics", "Pandas"],
        "salary": "8 - 15 LPA",
        "companies": ["Amazon", "Google", "Microsoft"]
    }
}

# ------------------------
# Skill Score System
# ------------------------
skill_score = {
    "Python": 3,
    "SQL": 2,
    "Excel": 1,
    "Statistics": 2,
    "Machine Learning": 4,
    "Pandas": 2,
    "OOP": 2,
    "Django": 3,
    "API": 2
}

# ------------------------
# Course Suggestions
# ------------------------
courses = {
    "Python": "Python Programming - Coursera",
    "SQL": "SQL for Data Analysis - Udemy",
    "Excel": "Advanced Excel - LinkedIn Learning",
    "Machine Learning": "Machine Learning - Andrew Ng",
    "Statistics": "Statistics for Data Science - Coursera",
    "Django": "Django Web Development - Udemy",
    "API": "REST API Development - Coursera"
}

# ------------------------
# User Input
# ------------------------
user_skills = input("Enter your skills (comma separated): ").split(",")
user_skills = [skill.strip() for skill in user_skills]

experience = int(input("Enter your experience (years): "))

print("\nYour Skills:", user_skills)
print("Experience:", experience, "years")

# ------------------------
# Skill Score Calculation
# ------------------------
total_score = 0
for skill in user_skills:
    if skill in skill_score:
        total_score += skill_score[skill]

print("\n⭐ Your Skill Score:", total_score)

# ------------------------
# Job Match Analysis + Company Recommendation
# ------------------------
best_match = None
highest_match = 0
roles_list = []
match_list = []

for role, details in jobs.items():
    required_skills = details["skills"]
    match_count = len([s for s in required_skills if s in user_skills])
    match_percent = (match_count / len(required_skills)) * 100

    # For Graph
    roles_list.append(role)
    match_list.append(match_percent)

    print("\nJob Role:", role)
    print("Required Skills:", required_skills)
    print("Skill Match:", round(match_percent,2), "%")

    # Missing skills & course suggestions
    missing = [skill for skill in required_skills if skill not in user_skills]
    if missing:
        print("Missing Skills:", missing)
        print("📚 Recommended Courses:")
        for skill in missing:
            if skill in courses:
                print(skill, "->", courses[skill])
    else:
        print("All skills matched ✅")

    # Estimated Salary
    print("Estimated Salary:", details["salary"])

    # Salary Level
    if match_percent == 100:
        level = "High Salary Opportunity"
    elif match_percent >= 70:
        level = "Good Salary Opportunity"
    elif match_percent >= 40:
        level = "Average Salary Opportunity"
    else:
        level = "Low Salary Opportunity"
    print("Salary Level Prediction:", level)

    # Experience Level
    if experience >= 5:
        exp_level = "Senior Level Candidate"
    elif experience >= 2:
        exp_level = "Mid Level Candidate"
    else:
        exp_level = "Fresher Level Candidate"
    print("Experience Level:", exp_level)

    # Company Recommendation Logic
    if match_percent >= 70:
        recommended_companies = details["companies"]
        print("🏢 Recommended Companies to Apply:", recommended_companies)
    elif match_percent >= 40:
        recommended_companies = details["companies"][:2]  # top 2
        print("🏢 Suggested Companies to Improve Skills:", recommended_companies)
    else:
        recommended_companies = []
        print("🏢 Focus on skill improvement before applying.")

    # Track Best Role
    if match_percent > highest_match:
        highest_match = match_percent
        best_match = role

# ------------------------
# Final Best Job Suggestion
# ------------------------
print("\n🏆 Best Job Suggestion for You")
if best_match:
    print("Best Role:", best_match)
    print("Skill Match:", round(highest_match,2), "%")
    print("📌 Apply to Companies:", jobs[best_match]["companies"])
else:
    print("Improve your skills to match job roles.")

# ------------------------
# Graph Visualization
# ------------------------
plt.bar(roles_list, match_list, color='skyblue')
plt.xlabel("Job Roles")
plt.ylabel("Skill Match Percentage")
plt.title("Job Role vs Skill Match Percentage")
plt.ylim(0, 100)
plt.show()