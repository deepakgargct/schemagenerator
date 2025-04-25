import streamlit as st
import json

st.set_page_config(page_title="Schema Markup Generator", layout="wide")
st.title("Schema Markup Generator")

schema_type = st.selectbox("Select Schema Type", [
    "FAQ", "Entity", "Product", "Local Business", "Service", "Event", "Video", "Blog Post", "Article", "Breadcrumb"
])

def generate_faq():
    st.subheader("FAQ Schema Markup")
    faq_items = []
    count = st.number_input("How many FAQs do you want to add?", min_value=1, max_value=20, value=1)

    for i in range(count):
        with st.expander(f"FAQ {i+1}"):
            question = st.text_input(f"Question {i+1}", key=f"q{i}")
            answer = st.text_area(f"Answer {i+1}", key=f"a{i}")
            if question and answer:
                faq_items.append({
                    "@type": "Question",
                    "name": question,
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": answer
                    }
                })

    if faq_items and st.button("Generate JSON-LD", key="faq_btn"):
        faq_schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_items
        }
        st.code(json.dumps(faq_schema, indent=2), language="json")

def generate_entity():
    st.subheader("Entity (LocalBusiness) Schema Markup")
    name = st.text_input("Business Name")
    description = st.text_area("Description")
    url = st.text_input("Website URL")
    logo = st.text_input("Logo URL")
    image_urls = st.text_area("Image URLs (comma-separated)")
    same_as = st.text_area("SameAs URLs (comma-separated)")

    contact_type = st.text_input("Contact Type")
    contact_url = st.text_input("Contact Page URL")

    subject_names = st.text_area("Subject Names (comma-separated)")
    subject_urls = st.text_area("Subject URLs (comma-separated)")

    knows_about = st.text_area("Knows About (comma-separated)")
    keywords = st.text_area("Keywords (comma-separated)")

    street_address = st.text_input("Street Address")
    locality = st.text_input("City / Locality")
    region = st.text_input("Region / State")
    postal_code = st.text_input("Postal Code")
    country = st.text_input("Country")

    latitude = st.text_input("Latitude")
    longitude = st.text_input("Longitude")
    map_url = st.text_input("Map URL")

    parent_name = st.text_input("Parent Org Name")
    parent_url = st.text_input("Parent Org URL")
    parent_area_served = st.text_input("Area Served")
    parent_description = st.text_area("Parent Org Description")

    if st.button("Generate JSON-LD", key="entity_btn"):
        entity_schema = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": name,
            "description": description,
            "url": url,
            "logo": logo,
            "image": [i.strip() for i in image_urls.split(",") if i.strip()],
            "sameAs": [s.strip() for s in same_as.split(",") if s.strip()],
            "contactPoint": {
                "@type": "ContactPoint",
                "contactType": [contact_type],
                "url": contact_url
            },
            "subjectOf": [
                {
                    "@type": "CreativeWork",
                    "name": n.strip(),
                    "sameAs": u.strip()
                }
                for n, u in zip(subject_names.split(","), subject_urls.split(","))
                if n.strip() and u.strip()
            ],
            "knowsAbout": [k.strip() for k in knows_about.split(",") if k.strip()],
            "keywords": [k.strip() for k in keywords.split(",") if k.strip()],
            "address": {
                "@type": "PostalAddress",
                "streetAddress": street_address,
                "addressLocality": locality,
                "addressRegion": region,
                "postalCode": postal_code,
                "addressCountry": country
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": latitude,
                "longitude": longitude
            },
            "hasMap": map_url,
            "parentOrganization": {
                "@type": "Organization",
                "name": parent_name,
                "url": parent_url,
                "areaServed": parent_area_served,
                "description": parent_description
            }
        }

        st.code(json.dumps(entity_schema, indent=2), language="json")

def generate_placeholder(schema_name):
    st.subheader(f"{schema_name} Schema Markup")
    st.info(f"The schema fields for {schema_name} are coming soon!")

if schema_type == "FAQ":
    generate_faq()
elif schema_type == "Entity":
    generate_entity()
else:
    generate_placeholder(schema_type)
