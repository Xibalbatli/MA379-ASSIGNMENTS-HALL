import streamlit as st
import random as rng

st.title('What Makes You S.P.E.C.I.A.L.?')
st.caption('The following test will analyze you Strength, Perception, Endurance, Charisma, Intelligence, Agility, '
           'and Luck. Let us find out if you have what it takes to survive in a harsh world.')
st.divider()
############ BEGIN STATS #############
st.session_state.strength = 0
st.session_state.perception = 0
st.session_state.endurance = 0
st.session_state.charisma = 0
st.session_state.intelligence = 0
st.session_state.agility = 0
st.session_state.luck = 0
############# END STATS #############

### Race Selection ###
st.session_state.race = st.selectbox('What is your race?',
                    ('Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc',
                     'Halfling', 'Human', 'Tiefling'), index=None)
if st.session_state.race == 'Dwarf':
    st.session_state.race = st.radio('What type of Dwarf?',
             ['Hill Dwarf', 'Mountain Dwarf'], index=None)
elif st.session_state.race == 'Elf':
    st.session_state.race = st.radio('What type of Elf',
             ['High Elf', 'Wood Elf'], index=None)
elif st.session_state.race == 'Halfling':
    st.session_state.race = st.radio('What type of Halfling?',
                    ['Lightfoot Halfling', 'Stout Halfling'], index=None)
if st.session_state.race == None:
    pass
else:
    st.success(f'Neat, you\'re the first {st.session_state.race} I\'ve met.')
## Race specific traits
# Dragonborn
if st.session_state.race == 'Dragonborn':
    ancestry = st.radio('What is your ancestry?',
             ('Black', 'Blue', 'Brass', 'Bronze', 'Copper', 'Gold',
              'Green', 'Red', 'Silver', 'White'), index=None)
    st.session_state.endurance += 1
    st.session_state.strength += 2
# Hill Dwarf
elif st.session_state.race == 'Hill Dwarf':
    st.session_state.perception += 2
    st.session_state.endurance += 1
    st.session_state.intelligence += 3
    st.session_state.strength += 2
# Mountain Dwarf
elif st.session_state.race == 'Mountain Dwarf':
    st.session_state.perception += 2
    st.session_state.endurance += 2
    st.session_state.intelligence += 3
# High Elf
elif st.session_state.race == 'High Elf':
    st.session_state.perception += 4
    st.session_state.luck += 1
    st.session_state.charisma += 1
    st.session_state.endurance += 2
    st.session_state.intelligence += 2
    st.session_state.strength += 1
# Wood Elf
elif st.session_state.race == 'Wood Elf':
    st.session_state.perception += 4
    st.session_state.luck += 2
    st.session_state.charisma += 1
    st.session_state.endurance += 2
    st.session_state.intelligence += 3
    st.session_state.strength += 1
    st.session_state.agility += 2
# Gnome
elif st.session_state.race == 'Gnome':
    st.session_state.perception += 2
    st.session_state.intelligence += 5
    st.session_state.charisma += 2
    st.session_state.luck += 2
# Half-Elf
elif st.session_state.race == 'Half-Elf':
    st.session_state.charisma += 4
    st.session_state.luck += 3
    st.session_state.perception += 4
    st.session_state.intelligence += 3
# Half-Orc
elif st.session_state.race == 'Half-Orc':
    st.session_state.perception += 2
    st.session_state.strength += 4
    st.session_state.luck += 2
    st.session_state.endurance += 2
# Lightfoot Halfling
elif st.session_state.race == 'Lightfoot Halfling':
    st.session_state.luck += 3
    st.session_state.endurance += 2
    st.session_state.agility += 2
# Stout Halfling
elif st.session_state.race == 'Stout Halfling':
    st.session_state.luck += 2
    st.session_state.endurance += 4
    st.session_state.agility += 2
# Human
elif st.session_state.race == 'Human':
    st.session_state.agility += 2
    st.session_state.intelligence += 3
# Tiefling
elif st.session_state.race == 'Tiefling':
    st.session_state.perception += 2
    st.session_state.endurance += 2
    st.session_state.strength += 2

### Class Selection ###
st.session_state.classs = st.selectbox('What is your class?',
                    ('Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
                     'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard'), index=None)
if st.session_state.classs == None:
    pass
else:
    st.success(f'Wow, a {st.session_state.classs}? How interesting.')
## Class Specific Traits
# Barbarian
if st.session_state.classs == 'Barbarian':
    st.session_state.strength += 4
    st.session_state.endurance += 3
    st.session_state.luck += 2
    st.session_state.perception += 3
    st.session_state.agility += 1
# Bard
elif st.session_state.classs == 'Bard':
    st.session_state.charisma += 4
    st.session_state.intelligence += 3
    st.session_state.endurance += 4
# Cleric
elif st.session_state.classs == 'Cleric':
    st.session_state.charisma += 3
    st.session_state.intelligence += 3
    st.session_state.luck += 4
    st.session_state.strength += 2
# Druid
elif st.session_state.classs == 'Druid':
    st.session_state.intelligence += 6
    st.session_state.endurance += 3
    st.session_state.strength += 2
    st.session_state.luck += 1
    st.session_state.perception += 1
# Fighter
elif st.session_state.classs == 'Fighter':
    st.session_state.strength += 6
    st.session_state.endurance += 3
    st.session_state.intelligence += 3
    st.session_state.agility += 1
    st.session_state.perception += 1
# Monk
elif st.session_state.classs == 'Monk':
    st.session_state.intelligence += 5
    st.session_state.strength += 7
    st.session_state.endurance += 4
    st.session_state.agility += 4
# Paladin
elif st.session_state.classs == 'Paladin':
    st.session_state.strength += 5
    st.session_state.charisma += 2
    st.session_state.intelligence += 4
    st.session_state.perception += 2
    st.session_state.luck += 3
    st.session_state.endurance += 3
# Ranger
elif st.session_state.classs == 'Ranger':
    st.session_state.strength += 6
    st.session_state.intelligence += 5
    st.session_state.luck += 4
    st.session_state.perception += 5
# Rogue
elif st.session_state.classs == 'Rogue':
    st.session_state.strength += 4
    st.session_state.intelligence += 5
    st.session_state.luck += 4
    st.session_state.agility += 3
    st.session_state.perception += 1
# Sorcerer
elif st.session_state.classs == 'Sorcerer':
    st.session_state.strength += 3
    st.session_state.charisma += 4
    st.session_state.intelligence += 5
# Warlock
elif st.session_state.classs == 'Warlock':
    st.session_state.charisma += 4
    st.session_state.intelligence += 5
    st.session_state.luck += 3
# Wizard
elif st.session_state.classs == 'Wizard':
    st.session_state.intelligence += 8
    st.session_state.endurance += 2
    st.session_state.luck += 1

### Abilities ###
st.write('Click the button below to see what the gods have in store for '
           'you along your journey. Their decision can be seen later.')
if st.button(':red[Ask for Blessing]'):
    st.session_state.strength += rng.randint(1, 6)
    st.session_state.strength += rng.randint(1, 6)
    st.session_state.strength += rng.randint(1, 6)
    st.session_state.perception += rng.randint(1, 6)
    st.session_state.perception += rng.randint(1, 6)
    st.session_state.perception += rng.randint(1, 6)
    st.session_state.endurance += rng.randint(1, 6)
    st.session_state.endurance += rng.randint(1, 6)
    st.session_state.endurance += rng.randint(1, 6)
    st.session_state.charisma += rng.randint(1, 6)
    st.session_state.charisma += rng.randint(1, 6)
    st.session_state.charisma += rng.randint(1, 6)
    st.session_state.intelligence += rng.randint(1, 6)
    st.session_state.intelligence += rng.randint(1, 6)
    st.session_state.intelligence += rng.randint(1, 6)
    st.session_state.agility += rng.randint(1, 6)
    st.session_state.agility += rng.randint(1, 6)
    st.session_state.agility += rng.randint(1, 6)
    st.session_state.luck += rng.randint(1, 6)
    st.session_state.luck += rng.randint(1, 6)
    st.session_state.luck += rng.randint(1, 6)
    st.info('You have been blessed.')
### Background ###
st.session_state.background = st.selectbox('What is your background?',
                    ('Acolyte', 'Criminal', 'Folk Hero', 'Haunted One', 'Noble', 'Sage',
                     'Soldier'), index=None)
if st.session_state.background == None:
    pass
else:
    st.warning(f'Your background is {st.session_state.background}? Are you sure you\'re '
               f'ready for your quest?')
## Background Traits
# Acolyte
if st.session_state.background == 'Acolyte':
    st.session_state.perception += 2
    st.session_state.luck += 2
# Criminal
elif st.session_state.background == 'Criminal':
    st.session_state.charisma += 2
    st.session_state.perception += 2
# Folk Hero
elif st.session_state.background == 'Folk Hero':
    st.session_state.luck += 2
    st.session_state.endurance += 2
# Haunted One
elif st.session_state.background == 'Haunted One':
    st.session_state.intelligence += 2
    st.session_state.luck += 2
# Noble
elif st.session_state.background == 'Noble':
    st.session_state.charisma += 2
    st.session_state.intelligence += 2
# Sage
elif st.session_state.background == 'Sage':
    st.session_state.intelligence += 4
# Soldier
elif st.session_state.background == 'Soldier':
    st.session_state.charisma += 2
    st.session_state.agility += 2

### Equipment ###
st.write('I have a few items lying around, feel free to take what you\'d like.')
st.session_state.equipment = st.multiselect('Items', ['A Martial Melee Weapon', 'A Simple Weapon', 'A Dagger',
                                                      'A Broken Blade', 'A Piece of Banner', 'A Set of Dice',
                                                      'A Deck of Cards'])
if st.session_state.equipment == []:
    pass
else:
    st.warning(f'Remember that you do not want to be over-cumbered on your journey.')

#### RESULTS ####


if st.button('SUBMIT'):
    st.balloons()

    st.session_state.total = (st.session_state.strength + st.session_state.perception + st.session_state.endurance +
                              st.session_state.charisma + st.session_state.intelligence + st.session_state.agility +
                              st.session_state.luck)
    st.session_state.Spercent = round(st.session_state.strength / st.session_state.total * 100)
    st.session_state.Ppercent = round(st.session_state.perception / st.session_state.total * 100)
    st.session_state.Epercent = round(st.session_state.endurance / st.session_state.total * 100)
    st.session_state.Cpercent = round(st.session_state.charisma / st.session_state.total * 100)
    st.session_state.Ipercent = round(st.session_state.intelligence / st.session_state.total * 100)
    st.session_state.Apercent = round(st.session_state.agility / st.session_state.total * 100)
    st.session_state.Lpercent = round(st.session_state.luck / st.session_state.total * 100)
    st.info(f'You have {st.session_state.Spercent}% Strength, '
            f'{st.session_state.Ppercent}% Perception, {st.session_state.Epercent}% Endurance,'
            f'{st.session_state.Cpercent}% Charisma, {st.session_state.Ipercent}% Intelligence, '
            f'{st.session_state.Apercent}% Agility, and {st.session_state.Lpercent}% Luck!')
st.divider()
if st.checkbox('Are you ready to continue your journey?'):
    st.write('Congratulations Traveler, you now know what makes you S.P.E.C.I.A.L!')

