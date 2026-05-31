from app.db import engine
from sqlmodel import Session, select
from app.models import Project, Profile, Skill


def create_sample_projects():
    with Session(engine) as session:
        statement = select(Project)
        existing = session.exec(statement).first()
        if existing:
            return
        p1 = Project(
            title="X-Ray Image Classification",
            description="A machine learning project deployed on Render for X-ray image analysis.",
            url="https://xray-9t34.onrender.com/",
        )
        p2 = Project(
            title="Topic Classifier",
            description="A machine learning project deployed on Render for classifying text by topic.",
            url="https://topic-classifier-yf1p.onrender.com/",
        )
        session.add(p1)
        session.add(p2)
        session.commit()


def create_sample_profile_and_skills():
    with Session(engine) as session:
        # profile
        profile = session.exec(select(Profile)).first()
        if not profile:
            profile = Profile(
                full_name="Mussa Rutta",
                headline="Data Scientist, Software Developer & Network Marketing Specialist",
                bio="I am a data scientist working on data analysis and software development. On the side, I am a networker at BF Suma dealing with nutritional supplements, and I am a business and economy enthusiast.",
                picture_path="profile.jpg",
                website=None,
                linkedin=None,
                twitter="@mussa_bbo",
            )
            session.add(profile)
        else:
            profile.full_name = "Mussa Rutta"
            profile.headline = "Data Scientist, Software Developer & Network Marketing Specialist"
            profile.bio = "I am a data scientist working on data analysis and software development. On the side, I am a networker at BF Suma dealing with nutritional supplements, and I am a business and economy enthusiast."
            profile.picture_path = "profile.jpg"
            profile.website = None
            profile.linkedin = None
            profile.twitter = "@mussa_bbo"

        # skills
        skill_exists = session.exec(select(Skill)).first()
        if not skill_exists:
            skills = [
                Skill(name="Python", category="data-science", level="advanced"),
                Skill(name="Software Development", category="data-science", level="advanced"),
                Skill(name="Pandas", category="data-science", level="advanced"),
                Skill(name="Network Marketing", category="network-marketing", level="advanced"),
                Skill(name="Business & Economy", category="network-marketing", level="intermediate"),
                Skill(name="Nutritional Supplements", category="network-marketing", level="intermediate"),
            ]
            session.add_all(skills)

        session.commit()

