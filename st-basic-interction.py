"""
Discussion Topics
=====================
* Adding Interactive Components to a Streamlit App
* button, selectbox, checkbox, radio, toggle, latex
* Adding an image

"""

# We need the following modules
import streamlit as st
from PIL import Image, ImageEnhance  # Needed for some image stuff
import random as rng

st.title('Adding Interactive Components')

st.header('st.button')

# Let's add a button here

if st.button('Don\'t Press'):
    st.write("No! WHY?")

st.divider()

st.header('st.selectbox')

# Let's add a selection box here

options = ['Blue', 'Green', 'Red']
selection = st.selectbox("What is your favorite color?", options)
ai_favorite_clr = rng.choice(options)
if selection == ai_favorite_clr:
    st.write(f"{selection} is my favorite color too.")
else:
    st.write(f"{selection} sucks, {ai_favorite_clr} is way better.")

st.divider()

st.header('st.checkbox + st.button')

st.write('What would you like to order?')

# Let's add some checkboxes here

icecream = st.checkbox('Ice Cream: 4$')
coffee = st.checkbox('Coffee: 2$')
beer = st.checkbox('Beer: 5$')

total = 0
order = ""
if icecream:
    total += 4
    order += " :icecream: "
if coffee:
    total += 2
    order += " :coffee: "
if beer:
    total += 5
    order += " :beer: "
if st.button('Done!'):
    if total == 0:
        st.write('Are you going to order?')
    else:
        st.write(f"Great, here's is your order: {order}")
        st.write(f"Pay {total}$")

st.divider()

st.header('st.radio + st.latex')

# Let's add some radio buttons and latex here

st.divider()

st.header('st.toggle + st.slider + st.image')

# Let's add a toggle button, slider and some image stuff here

on = st.toggle('Adjust Brightness')
image = Image.open('dog.jpg')
brightness = 1
if on:
    brightness = st.slider("Adjust Brightness", 0.0, 2.0, 1.0, 0.01)
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)
st.image(image, caption=f'Brightness = {brightness}')