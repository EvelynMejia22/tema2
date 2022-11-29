import pandas as pd
import streamlit as st
import datetime

walmart_data = pd.read_csv('Superstore.csv')


# Create the title for the web app
st.title("WALMART USA ANALYSIS :us:")
st.write("By: Evelyn Mejía Jiménez_A01652115")

st.sidebar.title("This is the sidebar.")
st.sidebar.write("You can add any elements to the sidebar.")


# Give user the current date
today = datetime.date.today()
today_date = st.sidebar.date_input('Current date', today)
st.success('Current date: `%s`' % (today_date))

# radio
selected_ship_mode = st.sidebar.radio("Select Ship Mode", walmart_data['Ship Mode'].unique())
st.write("Selected Ship Mode:", selected_ship_mode)


# Display the content of the dataset if checkbox is true
st.header("Dataset :open_file_folder:")
agree = st.sidebar.checkbox("You want to show dataset overview? ")
if agree:
  st.dataframe(walmart_data)


st.header("Data Description :page_with_curl:")
st. write("Con este análsis, se espera predecir las ventas de productos de línea blanca en el noroeste de los Estados Unidos. Se utilizarán variables como la categoría a la que pertenece, el modo de embarque y el descuento que tenga.")
st.markdown("___")

# Select the gender and the display the dataset with this selection
selected_category = st.sidebar.selectbox("Select Category", walmart_data['Category'].unique())
st.write(f"Selected Option: {selected_category!r}")
st.write(walmart_data.query(f"""Category==@selected_category"""))
st.markdown("___")


# Select a range of the fare and then display the dataset with this selection
optionals = st.sidebar.expander("Discount", True)
discount_min = optionals.slider(
    "Minimum Discount",
    min_value=float(walmart_data['Discount'].min()),
    max_value=float(walmart_data['Discount'].max())
)
discount_max = optionals.slider(
    "Maximum Discount",
    min_value=float(walmart_data['Discount'].min()),
    max_value=float(walmart_data['Discount'].max())
)

subset_discount = walmart_data[ (walmart_data['Discount'] >= discount_min) & (walmart_data['Discount'] <= discount_max)]
st.write(f"Number of Orders With Discount Between {discount_min} and {discount_max}: {subset_discount.shape[0]} :moneybag:")

# Display of the dataset whith the max fare selected
st.write(subset_discount)