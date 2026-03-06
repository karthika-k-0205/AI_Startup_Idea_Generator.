import pandas as pd
import random
import os

# -------------------------------
# Function to generate startup ideas (mock mode)
# -------------------------------
def generate_startup_idea(industry, technology, skills, audience):
    """
    Generate a startup idea based on user inputs.
    If skills are empty, return 2 alternative ideas.
    """
    
    # Predefined sample ideas for demonstration
    sample_ideas = [
        {
            "Startup Name": f"{industry}AI",
            "Problem Statement": f"{audience} struggle with problems in {industry}.",
            "Solution": f"AI-powered platform for {audience}.",
            "Key Features": "Adaptive learning, real-time feedback, analytics",
            "Technology Stack": f"{technology}, Python, Java",
            "Business Model": "Subscription",
            "Pitch Summary": f"AI solution to help {audience} solve {industry}-related problems."
        },
        {
            "Startup Name": f"Smart{industry}",
            "Problem Statement": f"{audience} face challenges in {industry}.",
            "Solution": f"Intelligent platform for {audience} using AI.",
            "Key Features": "Automation, Analytics, Insights",
            "Technology Stack": f"{technology}, Python, JavaScript",
            "Business Model": "Freemium",
            "Pitch Summary": f"A startup that uses AI to improve {industry} for {audience}."
        }
    ]
    
    # If user has provided skills, just return the first idea
    if skills.strip():
        return [sample_ideas[0]]
    else:
        # Return multiple ideas if no skills provided
        return sample_ideas

# -------------------------------
# Function to save idea(s) to CSV
# -------------------------------
def save_ideas_to_csv(ideas, filename="assets/data/startup_ideas.csv"):
    """
    Save list of startup ideas to CSV.
    Creates the folder if it does not exist.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    df = pd.DataFrame(ideas)
    
    # If file exists, append; else, create new
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', index=False, header=False)
    else:
        df.to_csv(filename, index=False)

# -------------------------------
# Optional: function to generate startup name suggestions
# -------------------------------
def generate_startup_names(base_name, n=5):
    """
    Generate multiple name suggestions for the startup.
    """
    suffixes = ["Hub", "Lab", "Genie", "Bot", "AI"]
    names = [f"{base_name}{random.choice(suffixes)}" for _ in range(n)]
    return names


  HOW  IT IS USED IN MAIN app.py
from utils import generate_startup_idea, save_ideas_to_csv, generate_startup_names

# Generate ideas
ideas = generate_startup_idea(industry, technology, skills, audience)

# Show ideas in Streamlit
for idea in ideas:
    st.write(idea)

# Save ideas
save_ideas_to_csv(ideas)

# Generate extra name suggestions
names = generate_startup_names(ideas[0]['Startup Name'])
st.write("Suggested Names:", names)
