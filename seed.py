from app import create_app, db  # Import from the app package
from app.models import Hero, Power, HeroPower

# Initialize the app context
app = create_app()

with app.app_context():
    # Create heroes
    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
    hero3 = Hero(name="Gwen Stacy", super_name="Spider-Gwen")

    # Create powers
    power1 = Power(name="Super Strength", description="Gives the wielder super-human strength.")
    power2 = Power(name="Flight", description="Gives the ability to fly at supersonic speeds.")
    power3 = Power(name="Elasticity", description="Can stretch the human body to extreme lengths.")

    # Create hero powers
    hero_power1 = HeroPower(strength="Strong", hero=hero1, power=power1)
    hero_power2 = HeroPower(strength="Average", hero=hero2, power=power2)
    hero_power3 = HeroPower(strength="Weak", hero=hero3, power=power3)

    # Add all objects to session and commit
    db.session.add_all([hero1, hero2, hero3, power1, power2, power3, hero_power1, hero_power2, hero_power3])
    db.session.commit()

    print("Database seeded!")
