import streamlit as st
import time


challenge = 'The Hanged Man'
hanged_man = st.progress(0, text=challenge)

for hp_hanged in range(100):
    time.sleep(.05)
    hanged_man.progress(hp_hanged + 1, text=challenge)

