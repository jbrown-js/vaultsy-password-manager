import customtkinter as ctk
import json

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("900x600")
app.resizable(False, False)
app.title("Vaultsy")

passwords = []
selected_login = None
current_category = "All"

def savePasswords():
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)


def loadPasswords():
    global passwords

    try:
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    except:
        passwords = []

def setCategory(category):
    global current_category
    current_category = category
    refreshPasswords()

def showAll():
    setCategory("All")

def showPersonal():
    setCategory("Personal")

def showWork():
    setCategory("Work")

def showFinance():
    setCategory("Finance")

def showUtilities():
    setCategory("Utilities")

def showOther():
    setCategory("Other")

def selectLogin(login):
    global selected_login
    selected_login = login
    refreshPasswords()

def removeFunction():
    global selected_login

    if selected_login != None:
        passwords.remove(selected_login)
        selected_login = None
        savePasswords()
        refreshPasswords()

def refreshPasswords():
    for widget in main.winfo_children():
        widget.destroy()

    for login in passwords:

        if current_category != "All":
            if login["category"] != current_category:
                continue

        if login == selected_login:
            colour = "#4A4A4A"
        else:
            colour = "#2f2f2f"

        card = ctk.CTkFrame(main, fg_color=colour, corner_radius=8)
        card.pack(fill="x", padx=15, pady=8)

        card.bind("<Button-1>", lambda event, login=login: selectLogin(login))

        siteLabel = ctk.CTkLabel(card, text=login["site"], font=("Arial", 16, "bold"))
        siteLabel.pack(anchor="w", padx=12, pady=(8, 0))

        userLabel = ctk.CTkLabel(card, text=login["user"], font=("Arial", 13))
        userLabel.pack(anchor="w", padx=12, pady=(0, 8))

        siteLabel.bind("<Button-1>", lambda event, login=login: selectLogin(login))
        userLabel.bind("<Button-1>", lambda event, login=login: selectLogin(login))

def copyPassword():

    if selected_login != None:
        app.clipboard_clear()
        app.clipboard_append(selected_login["password"])

def addFunction():
    popup = ctk.CTkToplevel(app)
    popup.title("Add Login")
    popup.geometry("420x500")
    popup.resizable(False, False)
    popup.configure(fg_color="#353535")

    ctk.CTkLabel(popup, text="Add New Login", font=("Arial", 22, "bold")).pack(pady=(20, 25))

    ctk.CTkLabel(popup, text="Website").pack(anchor="w", padx=30)
    websiteEntry = ctk.CTkEntry(popup, width=340)
    websiteEntry.pack(padx=30, pady=(5, 15), fill="x")

    ctk.CTkLabel(popup, text="Username").pack(anchor="w", padx=30)
    usernameEntry = ctk.CTkEntry(popup, width=340)
    usernameEntry.pack(padx=30, pady=(5, 15), fill="x")

    ctk.CTkLabel(popup, text="Password").pack(anchor="w", padx=30)
    passwordEntry = ctk.CTkEntry(popup, show="*", width=340)
    passwordEntry.pack(padx=30, pady=(5, 15), fill="x")

    ctk.CTkLabel(popup, text="Category").pack(anchor="w", padx=30)
    categoryBox = ctk.CTkOptionMenu(popup, values=["Personal", "Work", "Finance", "Utilities", "Other"])
    categoryBox.pack(padx=30, pady=(5, 25), fill="x")

    def saveLogin():
        passwords.append({
            "site": websiteEntry.get(),
            "user": usernameEntry.get(),
            "password": passwordEntry.get(),
            "category": categoryBox.get()
        })

        savePasswords()
        refreshPasswords()
        popup.destroy()

    ctk.CTkButton(
        popup,
        text="Save Login",
        fg_color="#38A52F",
        hover_color="#2E7E27",
        command=saveLogin
    ).pack(pady=(0, 20))

def editFunction():

    if selected_login == None:
        return

    popup = ctk.CTkToplevel(app)
    popup.title("Edit Login")
    popup.geometry("420x500")
    popup.resizable(False, False)
    popup.configure(fg_color="#353535")

    ctk.CTkLabel(popup, text="Edit Login", font=("Arial", 22, "bold")).pack(pady=(20, 25))

    ctk.CTkLabel(popup, text="Website").pack(anchor="w", padx=30)
    websiteEntry = ctk.CTkEntry(popup, width=340)
    websiteEntry.pack(padx=30, pady=(5, 15), fill="x")
    websiteEntry.insert(0, selected_login["site"])

    ctk.CTkLabel(popup, text="Username").pack(anchor="w", padx=30)
    usernameEntry = ctk.CTkEntry(popup, width=340)
    usernameEntry.pack(padx=30, pady=(5, 15), fill="x")
    usernameEntry.insert(0, selected_login["user"])

    ctk.CTkLabel(popup, text="Password").pack(anchor="w", padx=30)
    passwordEntry = ctk.CTkEntry(popup, show="*", width=340)
    passwordEntry.pack(padx=30, pady=(5, 15), fill="x")
    passwordEntry.insert(0, selected_login["password"])

    ctk.CTkLabel(popup, text="Category").pack(anchor="w", padx=30)
    categoryBox = ctk.CTkOptionMenu(
        popup,
        values=["Personal", "Work", "Finance", "Utilities", "Other"]
    )
    categoryBox.pack(padx=30, pady=(5, 25), fill="x")
    categoryBox.set(selected_login["category"])

    def saveChanges():
        selected_login["site"] = websiteEntry.get()
        selected_login["user"] = usernameEntry.get()
        selected_login["password"] = passwordEntry.get()
        selected_login["category"] = categoryBox.get()

        savePasswords()
        refreshPasswords()
        popup.destroy()

    ctk.CTkButton(
        popup,
        text="Save Changes",
        fg_color="#38A52F",
        hover_color="#2E7E27",
        command=saveChanges
    ).pack(pady=(0, 20))



# TOP BAR
topbar = ctk.CTkFrame(app, height=50, fg_color="#292929", corner_radius=0)
topbar.pack(side="top", fill="x")
topbar.pack_propagate(False)

logoLabel = ctk.CTkLabel(topbar, text="VAULTSY", font=("arial", 24, "bold"))
logoLabel.pack(side="left", padx=40)

addButton = ctk.CTkButton(topbar, text="Add Login", fg_color="#38A52F", hover_color="#2E7E27", command=addFunction)
addButton.pack(side="left", padx=(20,20))

removeButton = ctk.CTkButton(topbar, text="Remove Login", fg_color="#B83535", hover_color="#912C2C", command=removeFunction)
removeButton.pack(side="left", padx=20)

editButton = ctk.CTkButton(topbar, text="Edit Login", command=editFunction)
editButton.pack(side="left", padx=20)

copyButton = ctk.CTkButton(topbar, text="Copy Password", command=copyPassword)
copyButton.pack(side="left", padx=20)

content = ctk.CTkFrame(app)
content.pack(side="top", fill="both", expand=True)

# SIDEBAR
sidebar = ctk.CTkFrame(content, width=200, fg_color="#242424", corner_radius=0)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

ctk.CTkButton(sidebar, text="All", command=showAll).pack(pady=(30, 10))
ctk.CTkButton(sidebar, text="Personal", command=showPersonal).pack(pady=10)
ctk.CTkButton(sidebar, text="Work", command=showWork).pack(pady=10)
ctk.CTkButton(sidebar, text="Finance", command=showFinance).pack(pady=10)
ctk.CTkButton(sidebar, text="Utilities", command=showUtilities).pack(pady=10)
ctk.CTkButton(sidebar, text="Other", command=showOther).pack(pady=10)


# MAIN AREA
main = ctk.CTkScrollableFrame(content, fg_color="#353535", corner_radius=0)
main.pack(side="left", fill="both", expand=True)

loadPasswords()
refreshPasswords()

app.mainloop()
