import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

BA_AirlineReviews = pd.read_csv('BA_AirlineReviews.csv')

st.image('BritishAirways.jpg')

st.title('Visualization of British Airways Customer Reviews')
st.title('_____________________________')

#Overall Rating by Year

st.title('Overall Rating out of 10 by Year')

BA_AirlineReviews['Year'] = BA_AirlineReviews['Datetime'].str[-4:]

average_rating_by_Year = BA_AirlineReviews.groupby('Year')['OverallRating'].mean()

plt.figure(figsize=(10, 6))
plt.plot(average_rating_by_Year.index, average_rating_by_Year.values, marker='o')
plt.xlabel('Year')
plt.ylabel('Overall Rating Out Of 10')
st.pyplot(plt.gcf())

#Overall Ratings Filter by Travel Class

st.title('British Airways Rating by Travel Class')

BA_AirlineReviews_filtered = BA_AirlineReviews.dropna(subset=['SeatType'])
BA_AirlineReviews_filtered = BA_AirlineReviews_filtered[BA_AirlineReviews_filtered['SeatType'] != 'NONE']

travel_classes = BA_AirlineReviews_filtered['SeatType'].unique()

selected_class = st.sidebar.selectbox('Select Travel Class', travel_classes)

filtered_data = BA_AirlineReviews_filtered[BA_AirlineReviews_filtered['SeatType'] == selected_class]

overall_rating_count = filtered_data['OverallRating'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
overall_rating_count.plot(kind='bar', color='blue')
plt.xlabel('Overall Rating')
plt.ylabel('Count')
plt.title(f'Ratings For {selected_class}')
plt.xticks(rotation=0)
st.pyplot(plt.gcf())



#Category Scores
st.title('British Airways Miscellaneous Category Ratings out of 5')

categories = ['SeatComfort', 'CabinStaffService', 'GroundService', 'ValueForMoney', 'Food&Beverages', 'InflightEntertainment', 'Wifi&Connectivity']

selected_category = st.sidebar.selectbox('Select Miscellaneous Category', categories)

filtered_category_data = BA_AirlineReviews.dropna(subset=[selected_category])

plt.figure(figsize=(8, 6))
filtered_category_data[selected_category].value_counts().sort_index().plot(kind='barh', color='blue')
plt.xlabel('Count')
plt.ylabel('Score')
plt.title(f'{selected_category} Ratings')
st.pyplot(plt.gcf())



#Random Review Button

st.title('Random Review Button')

def display_full_text():
    random_entry = BA_AirlineReviews['ReviewBody'].sample().iloc[0]
    st.write(random_entry)

if st.button('Show Random Review'):
    display_full_text()



#Word Cloud for Review Header

st.title('Word Cloud for Review Header')

# Exclude specific words: Flight, British, Airways, BA
stopwords = set(['Flight', 'British', 'Airways', 'BA', 'Customer', 'Review', 'A', 'And', 'To', 'The', 'I', 'Experience', 'Was', 'For', 'Is', 'It', 'With', 'In', 'Of', 'My'])
wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords).generate(' '.join(BA_AirlineReviews['ReviewHeader']))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt.gcf())