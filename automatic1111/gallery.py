"""
Cycle through images in the specified directory, showing at full size with the file path.

This is helpful when inspecting images generated in batches.
"""

import os
import streamlit as st

# Specify the directory containing the images
image_directory = '/tmp/art-output'


@st.cache_data
def get_image_files(directory):
    image_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_files.append(os.path.join(directory, filename))
    return image_files

def main():
    # Get the list of image files in the directory
    image_files = get_image_files(image_directory)

    # Initialize the index of the currently displayed image
    current_image_index = st.session_state.get('current_image_index', 0)
 
    st.image(image_files[current_image_index])
    st.write(image_files[current_image_index])

    # Create next and back buttons
    # still buggy at beginning and end, requiring two button clicks
    col1, col2, col3 = st.columns(3)
    if col1.button("Back"):
        current_image_index = max(0, current_image_index - 1)
    if col3.button("Next"):
        current_image_index = min(len(image_files) - 1, current_image_index + 1)

    # Update the displayed image based on the button clicks
    st.session_state['current_image_index'] = current_image_index


if __name__ == "__main__":
    main()
