import menu

main_menu = menu.Menu()
user = main_menu.login()

try:
    if user[3] == "Manager":
        logged_user = Fabrica.angajat.Manager(user)
        logged_user.start_menu()
    elif user[3] == "Operator":
         logged_user = Fabrica.angajat.Operator(user)
         logged_user .start_menu()
    elif user[3] == "Gestionar":
         logged_user = Fabrica.angajat.Gestionar(user)
         assert isinstance(logged_user, user)
         logged_user.start_menu()
expect:
    pass