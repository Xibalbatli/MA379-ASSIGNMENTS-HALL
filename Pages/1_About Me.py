import streamlit as st
from PIL import Image

st.title('About Me')

st.write('Hello, you may not know me, but that\'s what this greeting is for. '
         'I am Andrés Pū\'Alilani "Pack-a-Punch" Hall. I was born on the 15th '
         'of December in the year 2002 in the city of Honolulu, Hawai\'i. This, '
         'however, is not my hometown. How is that possible? My old man was a '
         'sailor for the United States Navy and so we were able to move around '
         'a lot (not by choice). I was raised in a small town in central Texas '
         'called Brenham. One of my favorite hobbies - which is also an expensive '
         'one - is building Lego™ sets, particularly the Star Wars™ sets. My current '
         'career goal is to commission into the United States Army as an infantry '
         'officer and serve my country until it tells me to stop serving.')
me = Image.open('./Images/70939070829__5808615D-4DCA-4159-97E9-CF76E72CC13E.jpg').rotate(270)


st.image(me,caption='Image of Myself')