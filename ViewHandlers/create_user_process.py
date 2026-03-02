from CommonLibrary import *
result = Blueprint("create_user_process", __name__)
@result.route("/admin/create-user/process", methods=["GET", "POST"])
def view():
    users = ConfigManager("./data/users.cfg").get_key().split("\n")
    for i in range(len(users)):
        users[i] = users[i].split(",")
    if "username" in session:
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            with open("./data/users.cfg", "a+") as f:
                f.write(str(username) + "," + str(password) + ",3\n")
                f.close()
            users.append([str(username), str(password), str(3)])
            return redirect("/admin/dashboard")
        return redirect("/admin/dashboard")
    return redirect("/")
