import streamlit as st
from scraper import (
    extract_body_content,
    scrape_website_with_sbr,
    clean_body_content,
    chunk_cleaned_content,
)
from parse import parse_with_ollama

st.title("Web Scraping with LLMs")

url = st.text_input("Paste the URL of the website:")

if st.button("Scrape it"):
    result = scrape_website_with_sbr(url)
    body_content = extract_body_content(result)
    clean_content = clean_body_content(body_content)

    # Saves the content in Streamlit for futher use
    st.session_state.dom_content = clean_content

    with st.expander("Sections Possible to Scrape"):
        st.text_area(
            label="",
            value=clean_content,
            height=300,
        )

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want from the website?")

    if st.button("Parse Content:"):
        if parse_description:
            st.write("Parsing the content...")

            dom_chunks = chunk_cleaned_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)

            st.write(result)
