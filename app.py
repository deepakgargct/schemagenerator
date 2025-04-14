import streamlit as st
import json

st.set_page_config(page_title="Schema Markup Generator", layout="centered")
st.title("🧩 Schema Markup Generator")

schema_type = st.selectbox(
    "Select Schema Type", 
    ["Organization", "FAQ", "Product", "Local Business"]
)

schema = {}

if schema_type == "Organization":
    st.subheader("Organization Schema Fields")
    name = st.text_input("Organization Name")
    url = st.text_input("Website URL")
    logo = st.text_input("Logo URL")
    description = st.text_area("Description")

    if st.button("Generate Schema Markup"):
        schema = {
            "@context": "https://schema.org",
            "@type": "Organization",
            "name": name,
            "url": url,
            "logo": logo,
            "description": description
        }

elif schema_type == "FAQ":
    st.subheader("FAQ Schema Fields")
    num_faqs = st.number_input("How many FAQ items?", min_value=1, max_value=10, value=1, step=1)
    faq_items = []

    for i in range(num_faqs):
        question = st.text_input(f"Question {i+1}")
        answer = st.text_area(f"Answer {i+1}")
        if question and answer:
            faq_items.append({
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": answer
                }
            })

    if st.button("Generate Schema Markup") and faq_items:
        schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_items
        }

elif schema_type == "Product":
    st.subheader("Product Schema Fields")
    name = st.text_input("Product Name")
    description = st.text_area("Product Description")
    sku = st.text_input("SKU")
    brand = st.text_input("Brand")
    image = st.text_input("Image URL")
    price = st.text_input("Price")
    currency = st.text_input("Currency Code (e.g., USD)")
    availability = st.selectbox("Availability", ["InStock", "OutOfStock", "PreOrder"])
    url = st.text_input("Product URL")

    if st.button("Generate Schema Markup"):
        schema = {
            "@context": "https://schema.org/",
            "@type": "Product",
            "name": name,
            "image": image,
            "description": description,
            "sku": sku,
            "brand": {
                "@type": "Brand",
                "name": brand
            },
            "offers": {
                "@type": "Offer",
                "url": url,
                "priceCurrency": currency,
                "price": price,
                "availability": f"https://schema.org/{availability}"
            }
        }

elif schema_type == "Local Business":
    st.subheader("Local Business Schema Fields")
    name = st.text_input("Business Name")
    description = st.text_area("Description")
    url = st.text_input("Website URL")
    logo = st.text_input("Logo URL")
    phone = st.text_input("Phone Number")
    street = st.text_input("Street Address")
    city = st.text_input("City")
    state = st.text_input("State/Region")
    postal_code = st.text_input("Postal Code")
    country = st.text_input("Country")
    latitude = st.text_input("Latitude")
    longitude = st.text_input("Longitude")
    same_as = st.text_area("SameAs URLs (comma separated social or other profiles)")

    if st.button("Generate Schema Markup"):
        same_as_list = [s.strip() for s in same_as.split(",") if s.strip()]

        schema = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": name,
            "description": description,
            "url": url,
            "logo": logo,
            "telephone": phone,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": street,
                "addressLocality": city,
                "addressRegion": state,
                "postalCode": postal_code,
                "addressCountry": country
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": latitude,
                "longitude": longitude
            },
            "sameAs": same_as_list
        }

if schema:
    st.subheader("Generated JSON-LD Schema Markup")
    st.code(json.dumps(schema, indent=2), language="json")
