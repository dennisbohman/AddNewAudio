from flask import Flask, request, jsonify
import json

app =  Flask(__name__)

workfile = 'data.json'

# To read data from the workfile
def read_data():
        try: 
                with open(workfile, 'r') as file:
                        return json.load(file)
        except FileNotFoundError:
                return[]
        except json.JSONDecodeError:
                return[]

# Write data to workfile        
def write_data(data):
        with open(workfile, 'w') as file:
                json.dump(data, file, indent=4)


# Defines a route to website or root endpoint  
@app.route('/add', methods=['POST']) #
def add_audio_item():
        audio_items = read_data()

        new_audio_item = {
                "title": request.json.get('title', ''),
                "artist": request.json.get('artist', ''),
                "genre": request.json.get('genre', ''),
                "location": request.json.get('location', ''),
                "language": request.json.get('language', '')
        }

        audio_items.append(new_audio_item)
        write_data(audio_items)

        return jsonify({"message": "Updated (200)"}), 200 # 200 is a status code to show that the request is OK

if __name__ == '__main__':
        app.run(debug=True)
