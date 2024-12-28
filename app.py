import streamlit as st
import pickle
import pandas as pd
#def recommend(rest):
    #rest_index = restaurant[restaurant['name'] == rest].index[0]
    #distances = similarity[rest_index]
    #restaurant_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    #recommended_rest = []
    #for i in restaurant_list:
      #  recommended_rest.append(restaurant.iloc[i[0]].name)
    #return recommended_rest


restaurant_dict = pickle.load(open('rest_name.pkl','rb'))
restaurant = pd.DataFrame(restaurant_dict)
#print(restaurant)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Restaurant Recommended System')
option = st.selectbox(
'Select your favorite restaurant?', restaurant['name'].values)
print('st.button:  ',st.button)
#if st.button('Recommend'):
    #recommendation= recommend(option)
    #for i in recommendation:
        #st.write(i)
