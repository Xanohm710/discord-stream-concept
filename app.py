from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Discord Stream Concept", page_icon="🤫", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/pyapp.css")

# -- LOAD ASSETS
lottie_coding = "https://assets4.lottiefiles.com/packages/lf20_2glqweqs.json"
img_duo_form = Image.open("images/duos.jpg")
img_trio_form = Image.open("images/trios.jpg")
img_chaos_form = Image.open("images/chaos.jpg")

# --Header Section-- 
with st.container():
  st.subheader("Hi, we are a small group of friends trying to create an application to make streaming to friends in discord more enjoyable")
  st.title("Discord Stream Concept")
  st.write("Though our experience is very diverse, we are very passionate about this project in hopes it will bring as much joy to others as it does to ourselves")
  st.write("[Join us 🤖<--](https://discord.gg/r37ubzAM)")
  
  # --Goal of our project--
  with st.container():
      st.write("---")
      left_column, right_column = st.columns(2)
      with left_column:
          st.header("Our Goal:")
          st.write("##")
          st.write(
              """
              - a new perspective on group streaming 
              - customization for game nights with friends/family
              - an easy way to host tournaments with each team(s) perspective
              
              If this sounds interesting to you, consider joining our discord server (link above) for future updates)
              """
          )
          st.write("##")
      with right_column:
        st_lottie(lottie_coding, height=350, key="coding")
        
# -- Projects --
with st.container():
    st.write("---")
    st.header("Duo's Project")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_duo_form)
    with text_column:
        st.subheader("##")
        st.write(
            """
            This will be when 2 members can host their stream with their live feed camera's
            """
        )

with st.container():
    st.write("---")
    st.header("Trio's Project")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_trio_form)
    with text_column:
        st.subheader("##")
        st.write(
            """
            This will be when 3 members can host their stream with their live feed camera's
            """
        )
        
with st.container():
    st.write("---")
    st.header("Chaos Project")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_chaos_form)
    with text_column:
        st.subheader("##")
        st.write(
            """
            This will be when 4 members can host their stream with their live feed camera's
            """
        )
        
# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Us")
    st.write("##")
    
    # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/jaredyoung.dev@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()