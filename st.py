import streamlit as st

# Set page configuration
st.set_page_config(page_title="Client Portal", page_icon=":briefcase:")

# Client Title
st.title("Client Portal")

# Define color codes for insights
insight_colors = {
    "Insight 1": "info",
    "Insight 2": "warning",
    "Insight 3": "error"
}

# Row 1 - Metrics and Text for Insight 1 and Insight 2
with st.container():
    columns = st.columns([1.5, 1.5])  # Adjusted column widths

    # Insight 1
    with columns[0]:
        st.markdown(f'<div style="background-color: {insight_colors["Insight 1"]}; padding: 10px; border-radius: 5px;">', unsafe_allow_html=True)
        st.info("Insight 1")
        st.metric("Metric 1", value=42, delta=5)
        st.text("Sample text for Metric 1")
        st.markdown('</div>', unsafe_allow_html=True)

    # Insight 2
    with columns[1]:
        st.markdown(f'<div style="background-color: {insight_colors["Insight 2"]}; padding: 10px; border-radius: 5px;">', unsafe_allow_html=True)
        st.warning("Insight 2")
        st.metric("Metric 2", value=75, delta=-8)
        st.text("Sample text for Metric 2")
        st.markdown('</div>', unsafe_allow_html=True)

# Row 2 - Metrics and Text for Insight 3
with st.container():
    columns = st.columns(1)

    # Insight 3
    with columns[0]:
        st.markdown(f'<div style="background-color: {insight_colors["Insight 3"]}; padding: 10px; border-radius: 5px;">', unsafe_allow_html=True)
        st.error("Insight 3")
        st.metric("Metric 3", value=95, delta=12)
        st.text("Sample text for Metric 3")
        st.markdown('</div>', unsafe_allow_html=True)

# Additional content
st.title("Additional Content")
st.write("Add any additional content here.")
