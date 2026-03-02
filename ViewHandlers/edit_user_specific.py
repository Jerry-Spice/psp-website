from CommonLibrary import *
result = Blueprint("edit_user_specific", __name__)
@result.route("/admin/edit-user/<username>")
def view(username):
    users = ConfigManager("./data/users.cfg").get_key().split("\n")
    for i in range(len(users)):
        users[i] = users[i].split(",")
    if "username" in session:
        for user in users:
            if user[0] == username:
                return render_template("edit_user_specific.html", user=user)
    return redirect("/")
