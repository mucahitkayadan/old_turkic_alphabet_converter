import streamlit as st

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
def turkish_to_old_turkic_converter(turkish_text):
    old_turkic_text = ''
    for char in turkish_text:
        old_turkic_text += turkish_to_old_turkic.get(char.lower(), '?')
    return old_turkic_text

# Function to convert Old Turkic text to Turkish
def old_turkic_to_turkish_converter(old_turkic_text):
    turkish_text = ''
    for char in old_turkic_text:
        turkish_text += old_turkic_to_turkish.get(char, '?')
    return turkish_text

# Set a custom background using CSS
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_url});
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background image (replace with your own image link)
background_image_url = "https://images.unsplash.com/photo-1563986768609-322da13575f3"  # Change this link to a cool background

# Call the function to set background
set_background(background_image_url)

# App title
st.title("Turkish ⇆ Old Turkic Converter")

# Two sections for conversion
st.header("Convert between Modern Turkish and Old Turkic Script")

# Input for Turkish to Old Turkic conversion
turkish_text = st.text_area("Enter Turkish text:", value="Merhaba dünya")
if st.button("Convert to Old Turkic"):
    old_turkic_result = turkish_to_old_turkic_converter(turkish_text)
    st.text_area("Old Turkic result:", value=old_turkic_result, height=200)

# Input for Old Turkic to Turkish conversion
old_turkic_text = st.text_area("Enter Old Turkic text:")
if st.button("Convert to Turkish"):
    turkish_result = old_turkic_to_turkish_converter(old_turkic_text)
    st.text_area("Turkish result:", value=turkish_result, height=200)
