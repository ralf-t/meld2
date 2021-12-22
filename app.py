
from app import create_app

app = create_app()
# socketio = app.socketio


if __name__ == "__main__":
    app.run(debug=True)
    # socketio.run(app=app, debug=True)
