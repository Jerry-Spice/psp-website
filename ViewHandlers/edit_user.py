from CommonLibrary import *
result = Blueprint("edit_user", __name__)
@result.route("/admin/edit-user")
def view():
    users = ConfigManager("./data/users.cfg").get_key().split("\n")
    for i in range(len(users)):
        users[i] = users[i].split(",")

    
    if "username" in session:
        current_user = session["username"]
        current_permission = 0
        for user in users:
            if user[0] == current_user:
                current_permission = int(user[2])
                break
        i = 0
        while i < len(users):
            if users[i][0] == "":
                users.remove(users[i])
                i -= 1
            elif users[i][2] == "0":
                users.remove(users[i])
                i -= 1
            elif int(users[i][2]) <= current_permission:
                users.remove(users[i])
                i -= 1
            i+= 1
        return render_template("edit_user.html", users=users)
    return redirect("/")
