from flask import Blueprint, jsonify, request
from .models import Video, User
from .extensions import db

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/videos', methods=['GET'])
def get_videos():
    videos = Video.query.all()
    return jsonify([video.to_dict() for video in videos])

@api.route('/videos/<int:video_id>', methods=['GET'])
def get_video(video_id):
    video = Video.query.get_or_404(video_id)
    return jsonify(video.to_dict())

@api.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    user = User(name=name, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201

@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return jsonify(user.to_dict()), 200

    return jsonify({"error": "Invalid email or password"}), 401
