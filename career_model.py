def recommend_path(education, coding, math, communication, interest):

    recommendations = {

        "Artificial Intelligence": {
            "degree": "B.Tech",
            "branches": ["AI & ML", "CSE", "Data Science"],
            "alternatives": ["B.Sc AI", "BCA"],
            "careers": ["Python", "Machine Learning", "Deep Learning"]
        },

        "Machine Learning": {
            "degree": "B.Tech",
            "branches": ["AI & ML", "CSE"],
            "alternatives": ["Data Science"],
            "careers": ["Machine Learning", "Deep Learning", "MLOps"]
        },

        "Data Science": {
            "degree": "B.Tech / B.Sc",
            "branches": ["Data Science", "Statistics", "Computer Science"],
            "alternatives": ["Mathematics"],
            "careers": ["Data Analytics", "Power BI", "SQL"]
        },

        "Software Development": {
            "degree": "B.Tech",
            "branches": ["CSE", "IT"],
            "alternatives": ["BCA"],
            "careers": ["Python", "Java", "DSA"]
        },

        "Web Development": {
            "degree": "B.Tech / BCA",
            "branches": ["CSE", "IT"],
            "alternatives": ["B.Sc Computer Science"],
            "careers": ["HTML", "CSS", "JavaScript", "React"]
        },

        "Cyber Security": {
            "degree": "B.Tech",
            "branches": ["Cyber Security", "CSE"],
            "alternatives": ["BCA"],
            "careers": ["Ethical Hacking", "Network Security"]
        },

        "Cloud Computing": {
            "degree": "B.Tech",
            "branches": ["CSE", "IT"],
            "alternatives": ["BCA"],
            "careers": ["AWS", "Azure", "Google Cloud"]
        },

        "Defence Services": {
            "degree": "B.Tech / B.Sc / BA",
            "branches": ["Mechanical", "Civil", "B.Sc Mathematics"],
            "alternatives": ["NDA", "CDS"],
            "careers": ["Indian Army", "Indian Navy", "Indian Air Force"]
        },

        "Indian Army": {
            "degree": "B.Tech / B.Sc / BA",
            "branches": ["Mechanical", "Civil", "B.Sc Mathematics"],
            "alternatives": ["NDA", "CDS"],
            "careers": ["TES Entry", "NDA", "CDS"]
        },

        "Indian Navy": {
            "degree": "B.Tech",
            "branches": ["Mechanical", "Electrical", "ECE"],
            "alternatives": ["B.Sc Nautical Science"],
            "careers": ["Naval Academy", "Technical Entry"]
        },

        "Indian Air Force": {
            "degree": "B.Tech / B.Sc",
            "branches": ["Aeronautical", "ECE", "Mechanical"],
            "alternatives": ["B.Sc Mathematics"],
            "careers": ["AFCAT", "Flying Branch"]
        },

        "Government Jobs": {
            "degree": "Any Graduation",
            "branches": ["BA", "B.Com", "B.Sc", "B.Tech"],
            "alternatives": ["UPSC", "SSC"],
            "careers": ["UPSC", "SSC", "Bank PO", "Railways"]
        }
    }

    return recommendations.get(
        interest,
        {
            "degree": "Career Counseling Recommended",
            "branches": ["Explore Multiple Fields"],
            "alternatives": [],
            "careers": []
        }
    )