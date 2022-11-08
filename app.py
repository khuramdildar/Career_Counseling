import streamlit as st
from PIL import Image
import pickle
import pandas as pd

icon = Image.open('icon.jpeg')
st.set_page_config(page_title='Career Counseler', page_icon = icon)
st.header('Career Counseling')

with open("./weights.pkl", 'rb') as file:
    model = pickle.load(file)

def convert_to_float_7(marks1, marks2, marks3, marks4, marks5, marks6, marks7):
  m1 = float(marks1)
  m2 = float(marks2)
  m3 = float(marks3)
  m4 = float(marks4)
  m5 = float(marks5)
  m6 = float(marks6)
  m7 = float(marks7)
  return m1, m2, m3, m4, m5, m6, m7

def convert_to_float_12(marks1, marks2, marks3, marks4, marks5, marks6, marks7, marks8, marks9, marks10, marks11, marks12):
  m1 = float(marks1)
  m2 = float(marks2)
  m3 = float(marks3)
  m4 = float(marks4)
  m5 = float(marks5)
  m6 = float(marks6)
  m7 = float(marks7)
  m8 = float(marks8)
  m9 = float(marks9)
  m10 = float(marks10)
  m11 = float(marks11)
  m12 = float(marks12)
  return m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12

prof = ['Teacher', 'Artist', 'Businessman', 'Engineer', 'Sportsman', 'Accountant' , 'Computer_Scientist', 'Lawyer', 'Doctor']

def predict():
  df = pd.DataFrame.from_dict(labels)
  suggested_career = model.predict(df)
  prof.sort()
  result = prof[suggested_career[0]]
  st.write("Suggested Career: ",result)

def tech_non_tech(tech):
  if tech == "Tech":
    tech_option = 1.0
  elif tech == "Non-Tech":
    tech_option = 0.0

  return tech_option


labels = {'ENGLISH' : [0], 'URDU': [0], 'MATHS': [0], 'ISLAMIAT_PAK_STUDIES': [0], 'PHYSICS': [0],
      'CHEMISTRY': [0], 'BIOLOGY': [0], 'COMPUTER': [0], 'CIVICS': [0], 'HOME_ECONOMICS': [0],
      'GENERAL_SCIENCES': [0], 'CLOTHING_AND_TEXTILE': [0], 'AGRICULTURE': [0], 'STATS': [0],
      'ENVIRONMENTAL_SCIENCE': [0], 'GEOGRAPHY': [0], 'DIET_AND_NUTRITION': [0], 'POULTRY': [0],
      'PHYSICAL_EDUCATION': [0], 'PHYSIOLOGY': [0], 'ARTS_AND_DESIGNS': [0],
      'GEOMETRICALANDTECHNICALDRAWING': [0] , 'CHILDRENSGROWTHANDDOMESTICLIFE': [0],
      'DRESS_DESIGNING': [0], 'TECHNICAL': [0]}

option = st.selectbox(
    'Select Your Respective Group: ',
    ('Select Group:', 'Science ft Biology', 'Science ft Computer Science',
    'Arts', 'Arts(Combined)', 'Science(Combined)'))

#<-----------------------|||||----------------------->    

if 'Science ft Biology' in option:
  english = st.text_input('English: ')
  urdu = st.text_input('Urdu: ')
  math = st.text_input('Mathematics: ')
  isl = st.text_input('Islamiat: ')
  phy = st.text_input('Physics: ')
  chem = st.text_input('Chemistry: ')
  bio = st.text_input('Bio: ')

  tech = st.radio(
    "Would you like take technical or non-technical profession",
    ('Tech', 'Non-Tech'))

  submit = st.button('Submit')
  if submit:
    english, urdu, math, isl, phy, chem, comp = convert_to_float_7(english, urdu, math, isl, phy, chem, bio)
    labels["ENGLISH"] = english
    labels["URDU"] = urdu
    labels["MATHS"] = math
    labels["ISLAMIAT_PAK_STUDIES"] = isl
    labels["PHYSICS"] = phy
    labels["CHEMISTRY"] = chem
    labels["BIOLOGY"] = comp
    labels["TECHNICAL"] = tech_non_tech(tech)
    predict()

#<-----------------------|||||----------------------->

elif 'Science ft Computer Science' in option:
  english = st.text_input('English: ')
  urdu = st.text_input('Urdu: ')
  math = st.text_input('Mathematics: ')
  isl = st.text_input('Islamiat: ')
  phy = st.text_input('Physics: ')
  chem = st.text_input('Chemistry: ')
  comp = st.text_input('Computer: ')

  tech = st.radio(
    "Would you like take technical or non-technical profession",
    ('Tech', 'Non-Tech'))

  submit = st.button('Submit')
  if submit:
    english, urdu, math, isl, phy, chem, comp = convert_to_float_7(english, urdu, math, isl, phy, chem, comp)
    labels["ENGLISH"] = english
    labels["URDU"] = urdu
    labels["MATHS"] = math
    labels["ISLAMIAT_PAK_STUDIES"] = isl
    labels["PHYSICS"] = phy
    labels["CHEMISTRY"] = chem
    labels["COMPUTER"] = comp
    labels["TECHNICAL"] = tech_non_tech(tech)
    predict()

#<-----------------------|||||----------------------->

elif 'Arts' in option:
  english = st.text_input('English: ')
  urdu = st.text_input('Urdu: ')
  math = st.text_input('Mathematics: ')
  isl = st.text_input('Islamiat: ')
  civics = st.text_input('Civics: ')
  home_E = st.text_input('Home Economics: ')
  gen_S = st.text_input('General Science: ')

  tech = st.radio(
    "Would you like take technical or non-technical profession",
    ('Tech', 'Non-Tech'))

  submit = st.button('Submit')
  if submit:
    english, urdu, math, isl, civics, home_E, gen_S = convert_to_float_7(english, urdu, math, isl, civics, home_E, gen_S)
    labels["ENGLISH"] = english
    labels["URDU"] = urdu
    labels["MATHS"] = math
    labels["ISLAMIAT_PAK_STUDIES"] = isl
    labels["CIVICS"] = civics
    labels["HOME_ECONOMICS"] = home_E
    labels["GENERAL_SCIENCES"] = gen_S
    labels["TECHNICAL"] = tech_non_tech(tech)
    predict()

#<-----------------------|||||----------------------->

elif 'Arts(Combined)' in option:
  math = st.text_input('Mathematics: ')
  art_D = st.text_input('Art & Design: ')
  home_E = st.text_input('Home Economics: ')
  gen_S = st.text_input('General Science: ')
  Geo_TD = st.text_input('Geometrical & Technical Drawing: ')
  chilren_GD = st.text_input('Children Grwoth & Domestic Life: ')
  dress_D = st.text_input('Dress Design: ')

  tech = st.radio(
    "Would you like take technical or non-technical profession",
    ('Tech', 'Non-Tech'))

  submit = st.button('Submit')
  if submit:
    art_D, home_E, math, Geo_TD, chilren_GD, dress_D, gen_S = convert_to_float_7(art_D, home_E, math, Geo_TD, chilren_GD, dress_D, gen_S)
    labels["ARTS_AND_DESIGNS"] = art_D
    labels["HOME_ECONOMICS"] = home_E
    labels["MATHS"] = math
    labels["GEOMETRICALANDTECHNICALDRAWING"] = Geo_TD
    labels["CHILDRENSGROWTHANDDOMESTICLIFE"] = chilren_GD
    labels["DRESS_DESIGNING"] = dress_D
    labels["GENERAL_SCIENCES"] = gen_S
    labels["TECHNICAL"] = tech_non_tech(tech)

#<-----------------------|||||----------------------->

elif 'Science(Combined)' in option:
  math = st.text_input('Mathematics: ')
  home_E = st.text_input('Home Economics: ')
  phy = st.text_input('Physics: ')
  Cloth_T = st.text_input('Clothing & Textile: ')
  agri = st.text_input('Agriculture: ')
  stats = st.text_input('Statistics: ')
  env_S = st.text_input('Environmental Science: ')
  geo = st.text_input('Geography: ')
  diet_N = st.text_input('Diet & Nutrition: ')
  poultry = st.text_input('Poultry: ')
  physical_E = st.text_input('Physical Education: ')
  physiology = st.text_input('Physiology: ')

  tech = st.radio(
    "Would you like take technical or non-technical profession",
    ('Tech', 'Non-Tech'))

  submit = st.button('Submit')
  if submit:
    math, home_E, phy, Cloth_T, agri, stats, env_S, geo, diet_N, poultry, physical_E, physiology = convert_to_float_12(math, home_E, phy, Cloth_T, agri, stats, env_S, geo, diet_N, poultry, physical_E, physiology)
    labels["MATHS"] = math
    labels["HOME_ECONOMICS"] = home_E
    labels["PHYSICS"] = phy
    labels["CLOTHING_AND_TEXTILE"] = Cloth_T
    labels["AGRICULTURE"] = agri
    labels["STATS"] = stats
    labels["ENVIRONMENTAL_SCIENCE"] = env_S
    labels["GEOGRAPHY"] = geo
    labels["DIET_AND_NUTRITION"] = diet_N
    labels["POULTRY"] = poultry
    labels["PHYSICAL_EDUCATION"] = physical_E
    labels["PHYSIOLOGY"] = physiology
    labels["TECHNICAL"] = tech_non_tech(tech)

#<-----------------------|||||----------------------->