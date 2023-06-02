import streamlit as st
import plotly.express as px
from function import get_data

degree = ""
st.title("The Weather Forecast Web-App")
st.subheader("Your Key to Accurate Forecasting")
place = st.text_input("Enter Place for Forecast")
days = st.slider("Forcast Days", min_value=1, max_value=5, help="Select number of days you need forecast for")
display = st.selectbox("Select Display Views", ("Weather", "Temperature"))
if display == "Temperature":
    degree = st.selectbox("Select Temperature Type", ("Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"))
if place:
    text = f"{days} days"
    if days == 1:
        text = "day"
    place_t = place.title()
    st.subheader(f"{display} till next {text} in {place_t}")
    try:
        filter_data = get_data(place_t, days)
        dates = [item["dt_txt"] for item in filter_data]
        if display == "Temperature":
            temp = []
            if degree == "Celsius (°C)":
                temp = [float(tem["main"]["temp"]) / 10 for tem in filter_data]
            elif degree == "Fahrenheit (°F)":
                temp = [((float(tem["main"]["temp"]) / 10) * (9 / 5) + 32) for tem in filter_data]
            elif degree == "Kelvin (K)":
                temp = [((float(tem["main"]["temp"]) / 10) + 273.15) for tem in filter_data]
            y_label = f"Temperature {degree.split(' ')[1]}"
            figure = px.line(x=dates, y=temp, labels={"x": "Dates", "y": y_label})
            st.plotly_chart(figure)
        elif display == "Weather":
            weather_img = [weather["weather"][0]["main"] for weather in filter_data]
            weather_img = [f"images/{weather}.png" for weather in weather_img]
            st.image(weather_img, width=115,caption=dates)
    except KeyError:
        st.info("""You have entered non-existent place!
        Please enter correct place.
        """)
