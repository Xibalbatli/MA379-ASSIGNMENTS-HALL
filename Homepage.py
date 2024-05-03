import streamlit as st

st.title('Greetings Weary Traveler!')
st.header('The World Cannot Harm You Here')
st.divider()
st.subheader('Want to Know Your Host?')
st.write('I am nothing more than a checkpoint on your journey. A safe place for you to rest is this region before '
         'you. If you\'d like to know more about who I am, click the button below. No need to rush, rest here as long '
         'as you\'d like.')
if st.button('About Me'):
    st.switch_page('./Pages/1_About Me.py')
st.divider()
st.subheader('What Makes You S.P.E.C.I.A.L.?')
st.write('Have you ever wondered what makes you S.P.E.C.I.A.L.? The world can be a dangerous place for those '
         'unprepared. If interested, I can help you find out what makes you S.P.E.C.I.A.L. All you would '
         'need to do is answer a few questions and let me analyze your answers. I can tell you exactly '
         'how you can be the best you that you can be. Click the button below to find out what makes you '
         'S.P.E.C.I.A.L.')
if st.button('S.P.E.C.I.A.L.'):
    st.switch_page('./Pages/2_Quiz.py')
st.subheader('Do You Want to Play a Game?')
st.write('Might I interest you in a classic game that has not aged at all since it\'s introduction back in...the '
         'year it was created? Should you dare to test your luck, all you need to do is click the button below and '
         'we can see whether you have the knowledge and the strength to best me. Don\'t worry, no harm will come to '
         'you in this non-violent game. It has just been many moons since I was last bested, my champion now '
         'rests with the stars. Do you have the courage to take her title?')
if st.button('Challenge'):
    st.switch_page('./Pages/3_Hangman.py')
