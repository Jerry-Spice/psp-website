from CommonLibrary import *
result = Blueprint("edit_user_specific_process", __name__)
@result.route("/admin/edit-user/<username>/process", methods=["GET", "POST"])
def view(username):
    users = ConfigManager("./data/users.cfg").get_key().split("\n")
    for i in range(len(users)):
        users[i] = users[i].split(",")
    if "username" in session:
        if request.method == "POST":
            for user in users:
                if user[0] == username and user[2] != 0:
                    user[0] = request.form["username"]
                    user[1] = request.form["password"]
                    if int(session["mode"]) < 2:
                        user[2] = int(request.form["mode"])
            with open("./data/users.cfg", "w") as f:
                for user in users:
                    if user[0] != "":
                        f.write(str(user[0]))
                        f.write(",")
                        f.write(str(user[1]))
                        f.write(",")
                        f.write(str(user[2]))
                        f.write("\n")
                f.close()
        return redirect("/admin/dashboard")
    return redirect("/")