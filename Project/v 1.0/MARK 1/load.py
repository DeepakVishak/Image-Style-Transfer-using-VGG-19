import streamlit as st
from streamlit_lottie import st_lottie
import json
import time

class json_file:

    def __init__(self):
        pass

    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

class Load(json_file):

    def __init__(self):
        pass

    def display(self):
        st.title("Image Style Transfer using VGG - 19")
        file = json_file.load_lottiefile("load.json")
        print(file)

        st_lottie(
            file,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",  # medium ; high
            height=300,
            width=None,
            key=None,
        )

        progress_label = "Loading model..."
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress_text = f"{progress_label} {i+1}/100"
            progress.progress(i + 1,text=progress_text)


l = Load()
l.display()
