from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/armstrong/<int:n>")
def armstrong(n):
    sum=0
    order=len(str(n))
    copy_n=n
    while(n>0):
        digit=n%10
        sum+=digit **order
        n=n//10 

        if (sum== copy_n):
            print(f"{copy_n} is an armstrong number")
            result = {
                "Number":copy_n,
                "Armstrong":True,
                "Server IP":"122.234.213.53",
                "Other Number":[1,2,3,4,5]
            }
        else:
            print(f"{copy_n} is not an armstrong number")
            result = {
                "Number":copy_n,
                "Armstrong":False,
                "Server IP":"156.122.213.67",
                "Other Number":[6,7,8,9,10]
            }

            return jsonify(result)

if __name__ == "__main__":
      app.run(debug=True)