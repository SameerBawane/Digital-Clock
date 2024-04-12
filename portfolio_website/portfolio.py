from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie



st.set_page_config(page_title="My Portfolio", page_icon=":maple_leaf:",layout="wide")

def load_lottieurl(url):
    r= requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

# use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("portfolio_website/style/style.css")


# load assets
lottie_coding=load_lottieurl("https://lottie.host/24ba237b-4a7c-4a40-aaeb-b76b87bfd501/i5BPd2e3Ki.json")
image_amiraa=Image.open("portfolio_website/images/img1.png")
image_browsy_net=Image.open("portfolio_website/images/img2.png")
image_digital_clock=Image.open("portfolio_website/images/img3.png")


# header
with st.container():
    st.subheader("Hi, I am Sameer :wave:")
    st.title("A front end Developer & cloud enthusiast from India")
    st.write("with little beginnings, the naive dreamer constructing the empire, one brick at a time")
    st.write("[Learn More >](https://www.linkedin.com/in/sameer-bawane-488b89293/)")

# what I do 
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("""
                - I am proficient in coding languages such as C, C++, and Python.
                - I have hands-on experience with cloud platforms like AWS & Microsoft Azure.
                - I've undertaken various projects using Python and machine learning techniques.
                - In my leisure time, I indulge in reading books, writing stuff and listening to Bollywood music from the 2000s.
                - I am passionate about personal growth and constantly seek opportunities for self-improvement.
                """)
        st.write()
    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")


#Browsy.net
with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##") #st.write("## Features")2nd level heading a bit bold and larger
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(image_browsy_net)
    with text_column:
        st.subheader("Browsy.Net")
        st.write(
            """
            A Python-based Custom Browser Interface tailored with the functionality of Google Chrome.
            - Built upon the robust PyQt5 and PyQtWebEngine frameworks.
            - Navigation Controls: Seamlessly navigate with intuitive Back, Forward, Reload, and Home page options.
            - URL Search: Conveniently conduct searches directly via URLs, enhancing browsing efficiency.
            """
        )
        st.markdown("[More >](https://www.linkedin.com/feed/update/urn:li:activity:7181261734337290240/)")


#Amiraa Ui
with st.container():
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(image_amiraa)
    with text_column:
        st.subheader("Amiraa UI")
        st.write(
            """
            - Introducing a recent project: a visually captivating website UI designed just days ago.
            - Offering a sneak peek into the world of a fictional watch brand, exuding Time-crafted Elegance.
            - Crafted with a blend of HTML, CSS, and JavaScript for seamless interactivity with minimal design.
            """
        )
        st.markdown("[More >](https://www.linkedin.com/feed/update/urn:li:activity:7180325864398577664/)")


#Digital clock
with st.container():
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(image_digital_clock)
    with text_column:
        st.subheader("Digital CLock")
        st.write(
            """
            - Utilizing Tkinter for GUI development, it presents a basic yet functional interface.
            - Upon execution, a window titled "Digital Clock" pops up displaying the current time.
            - It updates every 200 milliseconds to reflect the current time accurately.
            """
        )
        st.markdown("[More >](https://www.linkedin.com/in/sameer-bawane-488b89293/)")


# contact form
with st.container():
    st.write("---")
    st.header("Get in Touch with Me!") 
    st.write("##") #st.write("## Features")2nd level heading a bit bold and larger
    contact_form="""
                <form action="https://formsubmit.co/sameerbawane007@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Your name" required>
                    <input type="email" name="email" placeholder="Your email" required>
                    <textarea name="message" placeholder="Type your message here" required></textarea>
                    <button type="submit">Send</button>
                </form>
                """
                # <input type="hidden" name="_captcha" value="false"> to disable the bydefault recaptcha field
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()