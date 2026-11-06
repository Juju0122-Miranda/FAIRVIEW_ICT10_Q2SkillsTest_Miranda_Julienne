#Skills Test
from pyscript import document

# Dictionary of non-metal elements
elements = {
    "H": ("Hydrogen", 1, 1.008),
    "He": ("Helium", 2, 4.003),
    "C": ("Carbon", 6, 12.011),
    "N": ("Nitrogen", 7, 14.007),
    "O": ("Oxygen", 8, 15.999),
    "F": ("Fluorine", 9, 18.998),
    "Ne": ("Neon", 10, 20.180),
    "P": ("Phosphorus", 15, 30.974),
    "S": ("Sulfur", 16, 32.06),
    "Cl": ("Chlorine", 17, 35.45),
    "Ar": ("Argon", 18, 39.948),
    "Se": ("Selenium", 34, 78.971),
    "Br": ("Bromine", 35, 79.904),
    "Kr": ("Krypton", 36, 83.798),
    "I": ("Iodine", 53, 126.904),
    "Xe": ("Xenon", 54, 131.293),
    "Rn": ("Radon", 86, 222)
}

# Function to search for an element
def search_element(e):

    # Get the input from HTML
    Element1 = document.getElementById("Element").value.capitalize()

    # Retrieve information from the dictionary
    result = elements.get(Element1, ("Element not found...", "-", "-"))

    # Display the result in HTML
    document.getElementById("message").innerHTML = f"""
    Element Symbol: {Element1}<br>
    Element Name: {result[0]}<br>
    Atomic Number: {result[1]}<br>
    Atomic Mass: {result[2]}
    """

# Function to clear the input and result
def clear(e):

    # Clear the input field
    document.getElementById("Element").value = ""
    # Clear the displayed information
    document.getElementById("message").innerHTML = ""
