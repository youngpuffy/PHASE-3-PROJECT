from lib.db.connection import init_db
from lib.scripts.run_scripts import create_user, make_payment, start_wifi_session, get_active_session_for_user

def main():
    init_db()

    user = create_user("vile", "securepass")
    make_payment(user.id, 10.0)
    session = start_wifi_session(user.id, 60)

    user = create_user("levi", "tazRAN")
    make_payment(user.id, 20.0)
    session = start_wifi_session(user.id, 120)

    user = create_user("muturi", "qwertmck")
    make_payment(user.id, 5.0)
    session = start_wifi_session(user.id, 30)

    user = create_user("turi", "123456we")
    make_payment(user.id, 30.0)
    session = start_wifi_session(user.id, 180)

    user = create_user("phoebe", "ebeoph!q")
    make_payment(user.id, 40.0)
    session = start_wifi_session(user.id, 260)

    session =get_active_session_for_user(user.id)
    print(f"Active sessions for user {user.username}:{[s.id for s in session]}")

if __name__ =="__main__":
    main()