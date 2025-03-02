import streamlit as st
import math

# Unit Conversion Factors
LENGTH_UNITS = {
    "Meters": 1,
    "Kilometers": 0.001,
    "Centimeters": 100,
    "Millimeters": 1000,
    "Inches": 39.3701,
    "Feet": 3.28084,
    "Yards": 1.09361,
    "Miles": 0.000621371,
}

# Conversion Formulas
CONVERSION_FORMULAS = {
    "Meters": {
        "Kilometers": "1 km = 1000 m",
        "Centimeters": "1 m = 100 cm",
        "Millimeters": "1 m = 1000 mm",
        "Inches": "1 m = 39.3701 in",
        "Feet": "1 m = 3.28084 ft",
        "Yards": "1 m = 1.09361 yd",
        "Miles": "1 mi = 1609.34 m",
    },
    "Kilometers": {
        "Meters": "1 km = 1000 m",
        "Centimeters": "1 km = 100,000 cm",
        "Millimeters": "1 km = 1,000,000 mm",
        "Inches": "1 km = 39,370.1 in",
        "Feet": "1 km = 3,280.84 ft",
        "Yards": "1 km = 1,093.61 yd",
        "Miles": "1 km = 0.621371 mi",
    },
    "Centimeters": {
        "Meters": "1 cm = 0.01 m",
        "Kilometers": "1 cm = 0.00001 km",
        "Millimeters": "1 cm = 10 mm",
        "Inches": "1 cm = 0.393701 in",
        "Feet": "1 cm = 0.0328084 ft",
        "Yards": "1 cm = 0.0109361 yd",
        "Miles": "1 cm = 0.00000621371 mi",
    },
    "Millimeters": {
        "Meters": "1 mm = 0.001 m",
        "Kilometers": "1 mm = 0.000001 km",
        "Centimeters": "1 mm = 0.1 cm",
        "Inches": "1 mm = 0.0393701 in",
        "Feet": "1 mm = 0.00328084 ft",
        "Yards": "1 mm = 0.00109361 yd",
        "Miles": "1 mm = 0.000000621371 mi",
    },
    "Inches": {
        "Meters": "1 in = 0.0254 m",
        "Kilometers": "1 in = 0.0000254 km",
        "Centimeters": "1 in = 2.54 cm",
        "Millimeters": "1 in = 25.4 mm",
        "Feet": "1 in = 0.0833333 ft",
        "Yards": "1 in = 0.0277778 yd",
        "Miles": "1 in = 0.000015783 mi",
    },
    "Feet": {
        "Meters": "1 ft = 0.3048 m",
        "Kilometers": "1 ft = 0.0003048 km",
        "Centimeters": "1 ft = 30.48 cm",
        "Millimeters": "1 ft = 304.8 mm",
        "Inches": "1 ft = 12 in",
        "Yards": "1 ft = 0.333333 yd",
        "Miles": "1 ft = 0.000189394 mi",
    },
    "Yards": {
        "Meters": "1 yd = 0.9144 m",
        "Kilometers": "1 yd = 0.0009144 km",
        "Centimeters": "1 yd = 91.44 cm",
        "Millimeters": "1 yd = 914.4 mm",
        "Inches": "1 yd = 36 in",
        "Feet": "1 yd = 3 ft",
        "Miles": "1 yd = 0.000568182 mi",
    },
    "Miles": {
        "Meters": "1 mi = 1609.34 m",
        "Kilometers": "1 mi = 1.60934 km",
        "Centimeters": "1 mi = 160,934 cm",
        "Millimeters": "1 mi = 1,609,340 mm",
        "Inches": "1 mi = 63,360 in",
        "Feet": "1 mi = 5,280 ft",
        "Yards": "1 mi = 1,760 yd",
    },
}

# Scientific Constants
SCIENTIFIC_CONSTANTS = {
    "Physics": {
        "Speed of Light (c)": "299,792,458 m/s",
        "Planck's Constant (h)": "6.62607015 × 10^-34 J·s",
        "Gravitational Constant (G)": "6.67430 × 10^-11 m^3·kg^-1·s^-2",
        "Electron Charge (e)": "1.602176634 × 10^-19 C",
    },
    "Chemistry": {
        "Avogadro's Number (NA)": "6.02214076 × 10^23 mol^-1",
        "Gas Constant (R)": "8.314462618 J·mol^-1·K^-1",
        "Boltzmann Constant (k)": "1.380649 × 10^-23 J·K^-1",
    },
    "Biology": {
        "Base Pair Length (DNA)": "0.34 nm",
        "ATP Energy Yield": "~30.5 kJ/mol",
    },
    "Math": {
        "Pi (π)": "3.141592653589793",
        "Euler's Number (e)": "2.718281828459045",
        "Golden Ratio (φ)": "1.618033988749895",
    },
}

# Streamlit App
st.title("🔬 Science Utility App")
st.write("This app provides three functionalities: Unit Converter, Scientific Constants, and Trigonometric Ratios.")

# Section 1: Unit Converter
st.header("📏 Unit Converter")
col1, col2, col3 = st.columns(3)

# Input
with col1:
    input_value = st.number_input("Enter value:", min_value=0.0, value=1.0)
with col2:
    input_unit = st.selectbox("From:", list(LENGTH_UNITS.keys()))
with col3:
    output_unit = st.selectbox("To:", list(LENGTH_UNITS.keys()))

# Conversion Logic
if input_unit and output_unit:
    base_value = input_value / LENGTH_UNITS[input_unit]  # Convert to base unit (meters)
    converted_value = base_value * LENGTH_UNITS[output_unit]  # Convert to target unit
    st.success(f"**Converted Value:** {converted_value:.4f} {output_unit}")

    # Display Formula
    if input_unit in CONVERSION_FORMULAS and output_unit in CONVERSION_FORMULAS[input_unit]:
        formula = CONVERSION_FORMULAS[input_unit][output_unit]
        st.info(f"**Conversion Formula:** {formula}")

# Section 2: Scientific Constants
st.header("🔭 Scientific Constants")
category = st.selectbox("Select Category:", list(SCIENTIFIC_CONSTANTS.keys()))

if category:
    st.write(f"### {category} Constants:")
    for constant, value in SCIENTIFIC_CONSTANTS[category].items():
        st.write(f"- **{constant}:** {value}")

# Section 3: Trigonometric Ratios
st.header("📐 Trigonometric Ratios")
angle = st.number_input("Enter angle (in degrees):", min_value=0.0, max_value=360.0, value=45.0)

if angle:
    radians = math.radians(angle)
    st.write(f"### Results for {angle}°:")
    st.write(f"- **Sine (sin):** {math.sin(radians):.4f}")
    st.write(f"- **Cosine (cos):** {math.cos(radians):.4f}")
    st.write(f"- **Tangent (tan):** {math.tan(radians):.4f}")
