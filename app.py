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

elif schema_type == "FAQ":
    st.subheader("FAQ Schema Fields")
    faq_question = st.text_input("FAQ Question")
    faq_answer = st.text_area("FAQ Answer")

    if st.button("Generate Schema Markup"):
        faq_schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": faq_question,
                    "acceptedAnswer": {
                        "@type": "Answer",
                        "text": faq_answer
                    }
                }
            ]
        }
        schema = faq_schema

elif schema_type == "Product":
    st.subheader("Product Schema Fields")
    product_name = st.text_input("Product Name")
    product_description = st.text_area("Product Description")
    product_sku = st.text_input("SKU")
    product_brand = st.text_input("Brand")
    product_category = st.text_input("Category")
    product_price = st.text_input("Price")
    product_currency = st.text_input("Currency")
    product_url = st.text_input("Product URL")
    product_image = st.text_input("Product Image URL")

    if st.button("Generate Schema Markup"):
        product_schema = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": product_name,
            "description": product_description,
            "sku": product_sku,
            "brand": {
                "@type": "Brand",
                "name": product_brand
            },
            "category": product_category,
            "offers": {
                "@type": "Offer",
                "price": product_price,
                "priceCurrency": product_currency,
                "url": product_url
            },
            "image": product_image
        }
        schema = product_schema

elif schema_type == "Local Business":
    st.subheader("Local Business Schema Fields")
    business_name = st.text_input("Business Name")
    business_description = st.text_area("Business Description")
    business_url = st.text_input("Website URL")
    business_phone = st.text_input("Phone Number")
    business_address = st.text_input("Business Address")
    business_city = st.text_input("City")
    business_state = st.text_input("State")
    business_zip = st.text_input("Zip Code")
    business_country = st.text_input("Country")
    business_logo = st.text_input("Logo URL")
    business_image = st.text_input("Image URL")
    business_opening_hours = st.text_area("Opening Hours")

    if st.button("Generate Schema Markup"):
        local_business_schema = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": business_name,
            "description": business_description,
            "url": business_url,
            "telephone": business_phone,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": business_address,
                "addressLocality": business_city,
                "addressRegion": business_state,
                "postalCode": business_zip,
                "addressCountry": business_country
            },
            "logo": business_logo,
            "image": business_image,
            "openingHours": business_opening_hours
        }
        schema = local_business_schema

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

# Display the generated Schema Markup
if schema:
    st.subheader("Generated Schema Markup")
    st.code(json.dumps(schema, indent=2), language="json")
