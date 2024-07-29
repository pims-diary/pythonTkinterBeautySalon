from Resources.Common.Root import root
from Pages.Login.Login import Login
from Data.DataLink.SqlDatabaseToData import print_users, validate_user

print_users()

a = validate_user("staff1", "pass1")
print(a)

b = validate_user("staff2", "pass1")
print(b)


# Create the main window
app = Login(root)

# Run the main event loop
root.mainloop()
