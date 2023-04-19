from flask import Flask

app = Flask("Battlesnake")

@app.get('/')
def on_info():
    print("INFO")
    return {
        "apiversion": "1",
        "author": "",  # TODO: Your Battlesnake Username
        "color": "#888888",  # TODO: Choose color
        "head": "default",  # TODO: Choose head
        "tail": "default",  # TODO: Choose tail
    }

@app.post("/start")
def on_start():
    print("GAME START")
    return "ok"

@app.post("/move") # this is the logic
def on_move():
    return {"move": "up"}

@app.post("/end")
def on_end():
    print("GAME END")
    return "ok"