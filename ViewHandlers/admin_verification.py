from CommonLibrary import *
result = Blueprint("admin_verification", __name__)
@result.route("/admin/verification", methods=["GET","POST"])
def view():
    users = ConfigManager("./data/users.cfg").get_key().split("\n")
    for i in range(len(users)):
        users[i] = users[i].split(",")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        for user in users:
            if user[0] == username and user[1] == password and int(user[2]) < 2:
                session["username"] = username
                session["mode"] = user[2]
                session["error"] = False
                return redirect("/admin/dashboard", code=302)
    session["error"] = True
    return redirect("/admin", code=302)