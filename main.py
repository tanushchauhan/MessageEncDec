from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
      if request.method == "POST":
        userInput = request.form["user_name"]
        # maybe add a system to log the conversions in future

        # making a key for basic quick conversion
        key = "2aa5aa3aa1aa6aa8aa7aa4"

        def main():
            #formating the key for use
            temp_key = key.split("aa")
            key = []
            for i in temp_key:
                key.append(int(i))
            
            #converting text to binary - may be a more effientient way avaliable 
            userInput = ' '.join(format(ord(c), '08b') for c in userInput)
            userInputList = userInput.split(" ")

if __name__ == "__main__":
    app.run()

