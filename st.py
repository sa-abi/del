import streamlit as st

# Sample insights for each block
insights = {
    "Insight 1": "This is insight 1",
    "Insight 2": "This is insight 2",
    "Insight 3": "This is insight 3",
    "Insight 4": "This is insight 4"
}

# Sample sticky notes
sticky_notes = [
    "Note 1",
    "Note 2",
    "Note 3",
    "Note 4",
    "Note 5",
    "Note 6",
    "Note 7",
    "Note 8",
    "Note 9",
    "Note 10"
]

# Function to display insights in a 2x2 grid
def display_insight_block(insight):
    col1, col2 = st.columns(2)  # Create a layout with 2 columns
    with col1:
        st.markdown(f"**{insight[0][0]}**")
        st.write(insight[0][1])
        st.write("---")  # Add a separator

        st.markdown(f"**{insight[1][0]}**")
        st.write(insight[1][1])
        st.write("---")  # Add a separator

    with col2:
        st.markdown(f"**{insight[2][0]}**")
        st.write(insight[2][1])
        st.write("---")  # Add a separator

        st.markdown(f"**{insight[3][0]}**")
        st.write(insight[3][1])
        st.write("---")  # Add a separator

# Main function to create the app
def main():
    st.title("Streamlit App with Tabs")

    # Create 5 tabs
    tab_selected = st.sidebar.radio("Select Tab", ["Tab 1", "Tab 2", "Tab 3", "Tab 4", "Sticky Notes"])

    # Tab 1 to 4
    if tab_selected.startswith("Tab"):
        tab_number = int(tab_selected.split()[-1])  # Extract tab number
        st.write(f"This is {tab_selected}")
        display_insight_block(list(insights.items()))

    # Sticky Notes Sub-Tabs
    elif tab_selected == "Sticky Notes":
        st.write("Select a sticky note to view insights")

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab9 = st.tabs(sticky_notes)
        with tab1:
            st.write(f"Insights for {sticky_notes[0]}:")
            display_insight_block(list(insights.items()))
        with tab2:
            st.write(f"Insights for {sticky_notes[0]}:")
            display_insight_block(list(insights.items()))
        with tab3:
            st.write(f"Insights for {sticky_notes[0]}:")
            display_insight_block(list(insights.items()))
        with tab4:
            st.write(f"Insights for {sticky_notes[0]}:")
            display_insight_block(list(insights.items()))




if __name__ == "__main__":
    main()






