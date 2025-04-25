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

def generate_product():
    st.subheader("Product Schema Markup")
    name = st.text_input("Product Name")
    description = st.text_area("Product Description")
    sku = st.text_input("SKU (Stock Keeping Unit)")
    brand = st.text_input("Brand")
    price = st.number_input("Price", min_value=0.0, format="%.2f")
    currency = st.text_input("Currency (e.g., USD)")
    availability = st.selectbox("Availability", ["InStock", "OutOfStock", "PreOrder"])
    product_url = st.text_input("Product URL")
    image_url = st.text_input("Product Image URL")

    if st.button("Generate JSON-LD", key="product_btn"):
        product_schema = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": name,
            "description": description,
            "sku": sku,
            "brand": brand,
            "offers": {
                "@type": "Offer",
                "price": price,
                "priceCurrency": currency,
                "availability": f"https://schema.org/{availability}",
                "url": product_url
            },
            "image": image_url
        }
        st.code(json.dumps(product_schema, indent=2), language="json")

def generate_service():
    st.subheader("Service Schema Markup")
    service_name = st.text_input("Service Name")
    service_description = st.text_area("Service Description")
    service_provider = st.text_input("Service Provider")
    service_url = st.text_input("Service URL")

    if st.button("Generate JSON-LD", key="service_btn"):
        service_schema = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": service_name,
            "description": service_description,
            "provider": {
                "@type": "Organization",
                "name": service_provider
            },
            "url": service_url
        }
        st.code(json.dumps(service_schema, indent=2), language="json")

# Event Schema
def generate_event():
    st.subheader("Event Schema Markup")
    event_name = st.text_input("Event Name")
    event_description = st.text_area("Event Description")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    location_name = st.text_input("Event Location Name")
    street_address = st.text_input("Street Address")
    city = st.text_input("City")
    state = st.text_input("State")
    postal_code = st.text_input("Postal Code")
    country = st.text_input("Country")

    if st.button("Generate JSON-LD", key="event_btn"):
        event_schema = {
            "@context": "https://schema.org",
            "@type": "Event",
            "name": event_name,
            "description": event_description,
            "startDate": start_date.isoformat(),
            "endDate": end_date.isoformat(),
            "location": {
                "@type": "Place",
                "name": location_name,
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": street_address,
                    "addressLocality": city,
                    "addressRegion": state,
                    "postalCode": postal_code,
                    "addressCountry": country
                }
            }
        }
        st.code(json.dumps(event_schema, indent=2), language="json")

# Video Schema
def generate_video():
    st.subheader("Video Schema Markup")
    video_name = st.text_input("Video Name")
    description = st.text_area("Video Description")
    video_url = st.text_input("Video URL")
    upload_date = st.date_input("Upload Date")
    duration = st.text_input("Duration (e.g., PT15M for 15 minutes)")

    if st.button("Generate JSON-LD", key="video_btn"):
        video_schema = {
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "name": video_name,
            "description": description,
            "url": video_url,
            "uploadDate": upload_date.isoformat(),
            "duration": duration
        }
        st.code(json.dumps(video_schema, indent=2), language="json")

# Blog Post Schema
def generate_blog_post():
    st.subheader("Blog Post Schema Markup")
    title = st.text_input("Blog Post Title")
    description = st.text_area("Blog Post Description")
    author = st.text_input("Author")
    date_published = st.date_input("Date Published")
    article_body = st.text_area("Article Body")

    if st.button("Generate JSON-LD", key="blog_post_btn"):
        blog_post_schema = {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": title,
            "description": description,
            "author": {
                "@type": "Person",
                "name": author
            },
            "datePublished": date_published.isoformat(),
            "articleBody": article_body
        }
        st.code(json.dumps(blog_post_schema, indent=2), language="json")

# Breadcrumb Schema
def generate_breadcrumb():
    st.subheader("Breadcrumb Schema Markup")
    breadcrumb_items = []
    count = st.number_input("How many Breadcrumbs do you want to add?", min_value=1, max_value=10, value=1)

    for i in range(count):
        with st.expander(f"Breadcrumb {i+1}"):
            name = st.text_input(f"Breadcrumb Name {i+1}", key=f"b_name{i}")
            url = st.text_input(f"Breadcrumb URL {i+1}", key=f"b_url{i}")
            if name and url:
                breadcrumb_items.append({
                    "@type": "ListItem",
                    "position": i + 1,
                    "name": name,
                    "item": url
                })

    if breadcrumb_items and st.button("Generate JSON-LD", key="breadcrumb_btn"):
        breadcrumb_schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": breadcrumb_items
        }
        st.code(json.dumps(breadcrumb_schema, indent=2), language="json")

# Select Schema Type
if schema_type == "FAQ":
    generate_faq()
elif schema_type == "Entity":
    generate_entity()
elif schema_type == "Product":
    generate_product()
elif schema_type == "Service":
    generate_service()
elif schema_type == "Event":
    generate_event()
elif schema_type == "Video":
    generate_video()
elif schema_type == "Blog Post":
    generate_blog_post()
elif schema_type == "Article":
    generate_blog_post()  # Same structure as Blog Post for simplicity
elif schema_type == "Breadcrumb":
    generate_breadcrumb()
else:
    st.info("Please select a valid schema type.")
