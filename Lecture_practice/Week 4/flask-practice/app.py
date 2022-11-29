from flask import Flask, jsonify, request

app = Flask(__name__)

menus = [{'id' : 1, 'name' : 'Espresso', 'price' : 3800},
         {'id' : 2, 'name' : 'Americano', 'price' : 4100},
         {'id' : 3, 'name' : 'Cafelatte', 'price' : 4600}
         ]
@app.route('/')
def hello_flask():
    return "hello world"

# Get / menus -> 자료를 가지고 온다.
@app.route('/menus')
def get_menus():
    return jsonify({'menus' : menus}) #json은 list를 가져올 수 없음 -> dic


# Post / menus -> 자료를 자원에 추가한다.
@app.route('/menus', methods=['POST'])
def create_menu(): # requst에는 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json() # {'name' : ..., 'price' : ...}
    new_menu = {
        'id' : 4,
        'name' : requst_data['name'],
        'price' : requst_data['price']
    }
    
    menus.append(new_menu)
    return jsonify(new_menu)

if __name__ == '__main__':
    app.run()