import streamlit as st
st.set_page_config(page_title="AI Startup Idea Generator", layout="wide")
st.title("🚀 AI Startup Idea Generator")
st.subheader("Enter your startup preferences")
industry = st.text_input("Industry (e.g., Healthcare, Education)")
technology = st.text_input("Technology (e.g., AI, Blockchain)")
skills = st.text_input("Skills (optional, e.g., Python, ML)")
audience = st.text_input("Target Audience (e.g., Students, Farmers)")
if st.button("Generate Startup Idea"):
    ideas = []
    if not skills.strip():
        base_names = ["Edu", "Learn", "SkillUp", "MindBoost", "Smart"]
        for i, name in enumerate(base_names[:3], start=1):
            ideas.append({
                "Startup Name": f"{name}{industry.replace(' ', '')}",
                "Problem": f"{audience} face challenges in {industry.lower()} learning and engagement.",
                "Solution": f"{technology} platform to improve {industry.lower()} outcomes for {audience}.",
                "Key Features": f"AI-driven insights, adaptive content, progress tracking {'' if i != 1 else ', quizzes'}",
                "Technology": f"{technology}, Python",
                "Business Model": "Subscription or Freemium",
                "Instructions": (
                    f"1. Research {industry} challenges for {audience}.\n"
                    "2. Build a prototype platform using AI.\n"
                    "3. Test with small group of target users.\n"
                    "4. Collect feedback and iterate.\n"
                    "5. Launch publicly and promote through social channels."
                )
            })
    else:
        ideas.append({
            "Startup Name": f"{industry}{technology}Hub",
            "Problem": f"{audience} struggle with personalized {industry.lower()} solutions.",
            "Solution": f"AI-powered platform leveraging {skills} for {audience} in {industry}.",
            "Key Features": f"Adaptive learning, real-time feedback, analytics",
            "Technology": f"{technology}, {skills}",
            "Business Model": "Subscription",
            "Instructions": (
                f"1. Validate the problem with {audience}.\n"
                "2. Build a prototype using your skills.\n"
                "3. Test and iterate based on feedback.\n"
                "4. Launch beta.\n"
                "5. Scale with marketing and partnerships."
            )
        })
    for i, idea in enumerate(ideas, start=1):
        st.subheader(f"Idea {i}: {idea['Startup Name']}")
        st.markdown(f"**Problem:** {idea['Problem']}")
        st.markdown(f"**Solution:** {idea['Solution']}")
        st.markdown(f"**Key Features:** {idea['Key Features']}")
        st.markdown(f"**Technology Stack:** {idea['Technology']}")
        st.markdown(f"**Business Model:** {idea['Business Model']}")
        st.markdown(f"**How to Start:**\n{idea['Instructions']}")
    st.subheader("💡 Suggested Startup Names")
    suggested_names = [
        f"{industry}{technology}Hub",
        f"Smart{audience}",
        f"{industry}AI",
        f"{audience}Genie",
        f"{technology}Innovators"
    ]
    st.write(", ".join(suggested_names))
