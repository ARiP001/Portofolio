# app.py
import streamlit as st

def st_version_geq(major, minor):
    try:
        parts = st.__version__.split(".")
        return (int(parts[0]), int(parts[1])) >= (major, minor)
    except Exception:
        return False

def get_page():
    if st_version_geq(1, 30):
        # new API: st.query_params (dict-like). use get_all for safety with repeated keys
        vals = st.query_params.get_all("page") if hasattr(st.query_params, "get_all") else st.query_params.get("page")
        if isinstance(vals, list) and vals:
            return vals[0]
        if isinstance(vals, str):
            return vals
        return "login"
    else:
        # old API: experimental_get_query_params() returns lists for values
        qp = st.experimental_get_query_params()
        return qp.get("page", ["login"])[0]

def set_page(p):
    if st_version_geq(1, 30):
        # new API: from_dict updates the URL
        st.query_params.from_dict({"page": p})
    else:
        # old API
        st.experimental_set_query_params(page=p)

page = get_page()

if page == "login":
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.success(f"Welcome {username}!")
        set_page("user")
    if st.button("Go to register"):
        set_page("register")

elif page == "register":
    st.title("Register")
    new_user = st.text_input("New username")
    new_pass = st.text_input("New password", type="password")
    if st.button("Register"):
        st.success(f"User {new_user} registered!")
        set_page("login")

elif page == "user":
    st.title("User Dashboard")
    st.write("This is a protected page.")
    if st.button("Logout"):
        set_page("login")
