import streamlit as st
import json

st.set_page_config(page_title="Schema Markup Generator", layout="centered")
st.title("\U0001F9E9 Schema Markup Generator")

schema_type = st.selectbox(
    "Select Schema Type", 
    [
        "Organization", 
        "FAQ", 
        "Product", 
        "Local Business", 
        "Entity",
        "Service",
        "Event",
        "Video",
        "Blog Post",
        "Article",
        "Breadcrumb"
    ]
)

schema = {}

if schema_type == "Organization":
    st.subheader("Organization Schema Fields")
    name = st.text_input("Organization Name")
    url = st.text_input("Website URL")
    logo = st.text_input("Logo URL")
    contact = st.text_input("Contact Page URL")
    same_as = st.text_area("SameAs URLs (comma separated)")

    if st.button("Generate Schema Markup"):
        schema = {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": name,
            "url": url,
            "logo": logo,
            "contactPoint": {
                "@type": "ContactPoint",
                "contactType": "customer support",
                "url": contact
            },
            "sameAs": [s.strip() for s in same_as.split(",") if s.strip()]
        }

elif schema_type == "Entity":
    st.subheader("Entity Schema Fields")
    name = st.text_input("Entity Name")
    url = st.text_input("Website URL")
    logo = st.text_input("Logo URL")
    image = st.text_input("Main Image URL")
    description = st.text_area("Description")
    contact_url = st.text_input("Contact Page URL")
    keywords = st.text_area("Keywords (comma separated)")
    knows_about = st.text_area("Knows About Topics (comma separated)")
    subject_name_1 = st.text_input("Subject 1 Name")
    subject_sameas_1 = st.text_input("Subject 1 SameAs URL")
    subject_name_2 = st.text_input("Subject 2 Name")
    subject_sameas_2 = st.text_input("Subject 2 SameAs URL")
    same_as = st.text_area("SameAs URLs (comma separated)")
    parent_name = st.text_input("Parent Organization Name (optional)")
    parent_url = st.text_input("Parent Organization URL (optional)")
    parent_area_served = st.text_input("Parent Area Served (optional)")
    parent_description = st.text_area("Parent Organization Description (optional)")

    if st.button("Generate Schema Markup"):
        entity_schema = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": name,
            "description": description,
            "url": url,
            "logo": logo,
            "image": [image],
            "sameAs": [s.strip() for s in same_as.split(",") if s.strip()],
            "contactPoint": {
                "@type": "ContactPoint",
                "contactType": ["Contact Sales"],
                "url": contact_url
            },
            "subjectOf": [
                {
                    "@type": "CreativeWork",
                    "name": subject_name_1,
                    "sameAs": subject_sameas_1
                },
                {
                    "@type": "CreativeWork",
                    "name": subject_name_2,
                    "sameAs": subject_sameas_2
                }
            ],
            "knowsAbout": [k.strip() for k in knows_about.split(",") if k.strip()],
            "keywords": [k.strip() for k in keywords.split(",") if k.strip()]
        }

        if parent_name:
            entity_schema["parentOrganization"] = {
                "@type": "Organization",
                "name": parent_name,
                "url": parent_url,
                "areaServed": parent_area_served,
                "description": parent_description
            }

        schema = entity_schema

# Additional elif blocks for Service, Event, Video, Blog Post, Article, and Breadcrumb Schema would go here.

if schema:
    st.subheader("Generated Schema Markup")
    st.code(json.dumps(schema, indent=2), language="json")
