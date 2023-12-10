import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


st.title("Anime Wisdom Vault")


data= pd.read_csv("data/lessreal-data.csv", sep=';')


data.drop(columns=['ID'], inplace=True)
data=data.iloc[:,:3]
data = data.dropna(subset=['Quote'])



data.reset_index(drop=True, inplace=True)


# def display_cards(dataframe):
#     for index, row in dataframe.iterrows():
#         plt.figure()
#         plt.title(f"Card {index + 1}")
#         plt.axis('off')  # Turn off axis for a cleaner look
#         plt.table(cellText=row.values.reshape(1, -1), colLabels=row.index, cellLoc='center', loc='center')
#         plt.show()

# # Display each row as a card
# display_cards(data2)

card_template = """
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                    <div class="card bg-light mb-3" >
                            <div class="card-body">
                                <span class="card-text"><b>Anime: </b>{}</span><br/>
                                <span class="card-text"><b>Character: </b>{}</span><br/>
                                <span class="card-text"><b>Quote: </b>{}</span><br/>
                            </div>
                        </div>
                    </div>
        """

row_per_page=15


page_number = st.session_state.page_number if 'page_number' in st.session_state else 0
offset = page_number * row_per_page

print_data=data.iloc[offset:offset+row_per_page,:]

col1, col2 = st.columns(2)

with col1:
    if st.button('Previous') and page_number > 0:
        page_number -= 1
        st.session_state.page_number = page_number



with col2:
    if st.button('Next'):
        page_number += 1
        st.session_state.page_number = page_number



num_rows_len = len(data)


# if st.button("Random"):
#     for i in range(0, row_per_page):
#         index=random.randint(0, num_rows_len)
#         st.markdown(card_template.format(print_data['Anime'][index], print_data['Character'][index], print_data['Quote'][index]), unsafe_allow_html=True)
    
st.write("Current Page:", page_number + 1)
for i in range(offset,offset+row_per_page):
    st.markdown(card_template.format(print_data['Anime'][i], print_data['Character'][i], print_data['Quote'][i]), unsafe_allow_html=True)



with st.expander("Entire dataframe"):
    st.write(data)