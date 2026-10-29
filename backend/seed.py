from app import create_app, db
from app.models import Video

app = create_app()

MOCK_VIDEOS = [
    {
        "title": "Big Buck Bunny",
        "description": "Un lapin géant et débonnaire se réveille pour découvrir trois rongeurs qui le harcèlent. Comédie animée légendaire de la Blender Foundation.",
        "thumbnail_url": "https://images.unsplash.com/photo-1518709268805-4e9042af2176?w=800&q=80",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
        "duration": "10 min",
        "category": "Trending",
    },
    {
        "title": "Elephant Dream",
        "description": "Deux personnages explorent un univers mécanique étrange et onirique rempli de rouages et de machines.",
        "thumbnail_url": "https://images.unsplash.com/photo-1535025183041-0991a977e25b?w=800&q=80",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4",
        "duration": "11 min",
        "category": "Trending",
    },
    {
        "title": "Sintel",
        "description": "Une jeune femme part à la recherche d'un dragon qu'elle a perdu, dans un voyage épique à travers des terres fantastiques.",
        "thumbnail_url": "https://images.unsplash.com/photo-1542204165-65bf26472b9b?w=800&q=80",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4",
        "duration": "15 min",
        "category": "Popular",
    },
    {
        "title": "Tears of Steel",
        "description": "Dans un futur dystopique, une équipe de guerriers et scientifiques tente de sauver le monde grâce aux voyages dans le temps.",
        "thumbnail_url": "https://images.unsplash.com/photo-1506318137071-a8e063b4bec0?w=800&q=80",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4",
        "duration": "12 min",
        "category": "Popular",
    },
    {
        "title": "For Bigger Blazes",
        "description": "Une démonstration spectaculaire des capacités de Chromecast à travers des images haute qualité.",
        "thumbnail_url": "https://images.unsplash.com/photo-1574375927938-d5a98e8ffe85?w=800&q=80",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
        "duration": "2 min",
        "category": "Recently Added",
    },
    {
        "title": "For Bigger Escapes",
        "description": "Évadez-vous avec ce court métrage haut en couleur qui met en valeur le streaming haute définition.",
        "thumbnail_url": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=800&q=80",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerEscapes.mp4",
        "duration": "3 min",
        "category": "Recently Added",
    },
    {
        "title": "For Bigger Fun",
        "description": "Un voyage joyeux et coloré conçu pour démontrer la qualité du streaming vidéo moderne.",
        "thumbnail_url": "https://images.unsplash.com/photo-1542204165-65bf26472b9b?w=800&q=80",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4",
        "duration": "3 min",
        "category": "Recently Added",
    },
    {
        "title": "For Bigger Joyrides",
        "description": "Embarquez pour une balade visuellement saisissante à travers des paysages variés.",
        "thumbnail_url": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&q=80",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4",
        "duration": "3 min",
        "category": "Recommended",
    },
    {
        "title": "For Bigger Meltdowns",
        "description": "Une explosion d'émotions et de couleurs dans ce court métrage dynamique.",
        "thumbnail_url": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&q=80",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4",
        "duration": "3 min",
        "category": "Recommended",
    },
    {
        "title": "Subaru Outback On Street And Dirt",
        "description": "Aventure tout-terrain à travers des paysages naturels époustouflants.",
        "thumbnail_url": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=800&q=80",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/SubaruOutbackOnStreetAndDirt.mp4",
        "duration": "1 min",
        "category": "Recommended",
    },
    {
        "title": "Volkswagen GTI Review",
        "description": "Un essai détaillé d'une voiture iconique, filmé avec une qualité cinématographique.",
        "thumbnail_url": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=800&q=80",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/VolkswagenGTIReview.mp4",
        "duration": "1 min",
        "category": "Trending",
    },
    {
        "title": "We Are Going On Bullrun",
        "description": "Suivez l'aventure d'un rallye automobile international à travers plusieurs pays.",
        "thumbnail_url": "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=800&q=80",
        "video_url": "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4",
        "duration": "1 min",
        "category": "Popular",
    },
]

def seed_database():
    with app.app_context():
        db.create_all()
        
        if Video.query.first():
            print("Database already seeded.")
            return

        for video_data in MOCK_VIDEOS:
            video = Video(**video_data)
            db.session.add(video)
        
        db.session.commit()
        print("Database successfully seeded!")

if __name__ == '__main__':
    seed_database()
