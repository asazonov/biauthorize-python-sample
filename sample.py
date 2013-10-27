from flask import Flask, render_template, request
app = Flask(__name__)

import biauthorize as ba

users = [{"email": "test", "password": "test", "biauth": "1"}]


def checkFunction(email, password, biauth_user):
    for user in users:
        if (
                user["email"] == email and
                user["password"] == password and
                user["biauth"] == biauth_user
        ):
            return True

    return False


@app.route('/')
def index_route():
    return render_template("index.html")


@app.route('/secret', methods=["POST"])
def secret_route():
    email = request.form["email"]
    password = request.form["password"]
    biauth_user = request.form["biauth_user"]
    biauth_verified = request.form["biauth_verified"]
    biauth_token = request.form["biauth_token"]
    if (
            biauth_verified == "true" and
            ba.biauthorizeVerifyToken(biauth_user, biauth_token) and
            checkFunction(email, password, biauth_user)
    ):
        return render_template("secret.html")
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
