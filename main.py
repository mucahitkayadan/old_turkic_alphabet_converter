import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header

# Define the mappings between Turkish and Old Turkic alphabets
turkish_to_old_turkic = {
    'a': '𐰀', 'b': '𐰉', 'c': '𐰲', 'ç': '𐰲', 'd': '𐰑', 'e': '𐰀',
    'f': '?', 'g': '𐰏', 'ğ': '𐰍', 'h': '𐰴', 'ı': '𐰃', 'i': '𐰃',
    'j': '?', 'k': '𐰴', 'l': '𐰞', 'm': '𐰢', 'n': '𐰤', 'o': '𐰆',
    'ö': '𐰇', 'p': '𐰯', 'r': '𐰺', 's': '𐰽', 'ş': '𐰾', 't': '𐱅',
    'u': '𐰇', 'ü': '𐰇', 'v': '?', 'y': '𐰘', 'z': '𐰔', ' ': ' '
}

# Reverse mapping for Old Turkic to Turkish
old_turkic_to_turkish = {v: k for k, v in turkish_to_old_turkic.items()}

# Function to convert Turkish text to Old Turkic
def turkish_to_old_turkic_converter(turkish_text: str) -> str:
    """
    Convert Turkish text to Old Turkic script.

    Args:
        turkish_text (str): The input Turkish text.

    Returns:
        str: The converted Old Turkic text.
    """
    return ''.join(turkish_to_old_turkic.get(char.lower(), '?') for char in turkish_text)

# Function to convert Old Turkic text to Turkish
def old_turkic_to_turkish_converter(old_turkic_text: str) -> str:
    """
    Convert Old Turkic text to Turkish.

    Args:
        old_turkic_text (str): The input Old Turkic text.

    Returns:
        str: The converted Turkish text.
    """
    return ''.join(old_turkic_to_turkish.get(char, '?') for char in old_turkic_text)

# Set a custom background using CSS
def set_background(image_url: str) -> None:
    """
    Set a custom background image for the Streamlit app.

    Args:
        image_url (str): The URL of the background image.
    """
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_url});
            background-size: cover;
            background-position: center;
        }}
        .stTextInput > div > div > input {{
            background-color: rgba(255, 255, 255, 0.8);
        }}
        .stTextArea > div > div > textarea {{
            background-color: rgba(255, 255, 255, 0.8);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background image
# background_image_url = "https://cdn.myfonts.net/cdn-cgi/image/width=417,height=208,fit=contain,format=auto/images/pim/10000/ULBvbeaaspohCtlBq9pEb1Jr_c3b3c4dde4732c971f1c4b33d433b9c2.png"
# set_background(background_image_url)

# Set a custom theme and styling
def set_custom_theme():
    st.markdown("""
    <style>
    :root {
        --primary-color: #1E88E5;
        --background-color: #F0F4F8;
        --secondary-background-color: #FFFFFF;
        --text-color: #333333;
        --font: 'Roboto', sans-serif;
    }
    .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
        font-family: var(--font);
    }
    .stTextInput > div > div > input {
        background-color: var(--secondary-background-color);
    }
    .stTextArea > div > div > textarea {
        background-color: var(--secondary-background-color);
    }
    .stButton > button {
        background-color: var(--primary-color);
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stDataFrame {
        background-color: var(--secondary-background-color);
        border-radius: 5px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Set the custom theme
set_custom_theme()

# App title and description
st.title("Turkish ⇆ Old Turkic Converter")
st.markdown("""
This app allows you to convert between Modern Turkish and Old Turkic script.
Enter your text in either Turkish or Old Turkic, and click the corresponding button to convert.
""")

# Create tabs for different sections
tab1, tab2, tab3 = st.tabs(["Turkish to Old Turkic", "Old Turkic to Turkish", "Character Mappings"])

with tab1:
    st.subheader("Turkish to Old Turkic")
    turkish_text = st.text_area("Enter Turkish text:", value="Merhaba dünya", key="turkish_input")
    if st.button("Convert to Old Turkic"):
        old_turkic_result = turkish_to_old_turkic_converter(turkish_text)
        st.text_area("Old Turkic result:", value=old_turkic_result, height=200, key="old_turkic_output")

with tab2:
    st.subheader("Old Turkic to Turkish")
    old_turkic_text = st.text_area("Enter Old Turkic text:", key="old_turkic_input")
    if st.button("Convert to Turkish"):
        turkish_result = old_turkic_to_turkish_converter(old_turkic_text)
        st.text_area("Turkish result:", value=turkish_result, height=200, key="turkish_output")

# Display the character mappings
with tab3:
    colored_header("Character Mappings", description="Table of character mappings used in the conversion", color_name="blue-70")
    mapping_df = pd.DataFrame(list(turkish_to_old_turkic.items()), columns=["Turkish", "Old Turkic"])
    st.dataframe(mapping_df, use_container_width=True, hide_index=True)
