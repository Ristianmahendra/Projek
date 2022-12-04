from process import preparation, generate_response
from flask import Flask, render_template, request

# download nltk
preparation()

#Start Chatbot
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_input = str(request.args.get('msg'))
    result = generate_response(user_input)
    return result

if __name__ == "__main__":
    app.run(debug=True)

# if __name__ == "__main__":
#     print("Let's chat! (type 'quit' to exit)")
#     while True:
#        # sentence = "do you use credit cards?"
#         result = input("You: ")
#         if result == "quit":
#             break

#         resp = get_bot_response(result)
#         print(resp)