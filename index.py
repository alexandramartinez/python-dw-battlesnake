from flask import Flask

app = Flask("Battlesnake")

@app.get('/')
def on_info():
    print("INFO")
    return {
        "apiversion": "1",
        "author": "alexandramartinez",  
        "color": "#6c25be",
        "head": "caffeine",
        "tail": "nr-booster",
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