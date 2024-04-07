from app import app, db
from models import Game, User, Review

with app.app_context():
    db.drop_all()
    db.create_all()

    game1 = Game(
        title="Elden Ring",
        description="An action role-playing game set in the Lands Between, a new fantasy world created by Hidetaka Miyazaki and George R. R. Martin.",
        image_url="https://example.com/elden-ring.jpg"
    )

    game2 = Game(
        title="Horizon Forbidden West",
        description="An action role-playing game set in a post-apocalyptic world where humans live in primitive tribes and coexist with robotic creatures.",
        image_url="https://hbw.com/horizon-forbidden-west.jpg"
    )
    game3 = Game(
        title="FIFA23",
        description="A popular football video game featuring realistic gameplay, professional leagues, and immersive graphics.",
        image_url="https://easports.com/fifa23.jpg"
    )
    game4 = Game(
        title="Call of Duty 4: Modern Warfare ",
        description="An iconic first-person shooter set in modern times, known for its intense single-player campaign and competitive multiplayer modes.",
        image_url="https://cod.com/cod4mw.jpg"
    )
    game5 = Game(
        title="Wolfenstein",
        description="A classic first-person shooter series known for its alternate history settings, where players battle against Nazi forces and supernatural threats to save the world.",
        image_url="https://wolfenstein.com/wolfenstein.jpg"
    )

    user1 = User(username="BrianKipkirui")
    user2 = User(username="KBNgeno")
    user3 = User(username="MadMax")
    user4 = User(username="Deadpool")

    review1 = Review(
        score=5,
        comment="Elden Ring is an absolute masterpiece! The open world is stunning and the combat is incredibly satisfying.",
        game=game1,
        user=user1
    )

    review2 = Review(
        score=4,
        comment="Horizon Forbidden West is a great sequel, with improved gameplay and visuals. Highly recommended!",
        game=game2,
        user=user2
    )

    db.session.add_all([game1, game2, user1, user2, review1, review2])
    db.session.commit()

    print("Database seeded successfully!")