from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My webpage", page_icon=":boom:",layout="wide")

def load_lottie(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_wave= load_lottie("https://assets1.lottiefiles.com/packages/lf20_coahzstz.json")
img1= Image.open("images/rovin.jpg")

with st.container():
    st.subheader("Hey, this is Charan :wave:")
    st.title("Welcome to my Website")

with st.container():
    st.write("---")
    left_c,right_c= st.columns(2)
    with right_c:
        st_lottie(lottie_wave, height=300, key="wave")
    with left_c:
        st.header("LGBTQ")
        st.write("##")
        st.write(
            """
Ladies and gentlemen, honored guests, and esteemed colleagues,

Today, I stand before you to address a topic that has sparked important conversations around the world – the subject of homosexuality and the LGBTQ+ community. It is my belief that equality and acceptance should be the cornerstones of our society, and I want to take this opportunity to shed light on the experiences and challenges faced by gay individuals.

Firstly, it is essential to recognize that being gay is not a choice. Sexual orientation, like the color of our eyes or the tone of our skin, is an inherent part of who we are as individuals. It is not a flaw or a deviation from the norm, but rather a natural and beautiful variation of human diversity. By acknowledging this fact, we take a step towards creating a society that celebrates uniqueness rather than perpetuating prejudice.

Throughout history, LGBTQ+ individuals have endured discrimination, marginalization, and even violence. They have faced legal persecution and societal stigmatization. However, the LGBTQ+ community has shown immense strength and resilience in the face of adversity. They have fought for their rights, demanding equality, and challenging the status quo. Their struggle for acceptance is not just about their rights but about the values we hold as a society – values of compassion, empathy, and inclusivity.

It is crucial to recognize that the fight for LGBTQ+ rights is not about special privileges or asking for more than others have. It is about seeking the same fundamental rights and opportunities that all individuals deserve. It is about equal access to education, employment, healthcare, and the freedom to love who they choose without fear of prejudice or persecution.

When we embrace diversity and support the LGBTQ+ community, we enrich our society as a whole. We tap into a vast array of talents, perspectives, and contributions that would otherwise remain untapped. The creative arts, sciences, business, and many other fields have been greatly enriched by the contributions of LGBTQ+ individuals throughout history. Their unique experiences, struggles, and triumphs have shaped our world in countless positive ways.

To those who may hold reservations or harbor prejudice, I urge you to approach this topic with an open heart and an open mind. Educate yourself about the challenges faced by the LGBTQ+ community, engage in dialogue, and strive for understanding. By challenging our own biases, we can build bridges of empathy and create a more inclusive society for all.

In closing, let us embrace the words of Martin Luther King Jr., who said, "Injustice anywhere is a threat to justice everywhere." Let us stand together and work towards a future where sexual orientation is not a basis for discrimination or judgment. Let us celebrate love, acceptance, and equality for all individuals, regardless of their sexual orientation.

Thank you.
""")

with st.container():
    st.write("---")
    st.header("How Gay people would look")
    st.write("##")
    l_c,r_c=st.columns(2)
    with l_c:
        st.image(img1)
        
        
    

        
