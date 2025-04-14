import streamlit as st
import json

st.set_page_config(page_title="Schema Markup Generator", layout="centered")
st.title("🧩 Schema Markup Generator")

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

# The rest of the existing schema inputs... (unchanged for Organization, FAQ, Product, Local Business)

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

elif schema_type == "Service":
    st.subheader("Service Schema Fields")
    name = st.text_input("Service Name")
    service_type = st.text_input("Service Type")
    provider = st.text_input("Provider Name")
    area_served = st.text_input("Area Served")
    url = st.text_input("URL")

    if st.button("Generate Schema Markup"):
        schema = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": name,
            "serviceType": service_type,
            "provider": {
                "@type": "Organization",
                "name": provider
            },
            "areaServed": area_served,
            "url": url
        }

elif schema_type == "Event":
    st.subheader("Event Schema Fields")
    name = st.text_input("Event Name")
    start_date = st.text_input("Start Date (YYYY-MM-DD)")
    end_date = st.text_input("End Date (YYYY-MM-DD)")
    location = st.text_input("Location Name")
    address = st.text_input("Location Address")
    url = st.text_input("Event URL")

    if st.button("Generate Schema Markup"):
        schema = {
            "@context": "https://schema.org",
            "@type": "Event",
            "name": name,
            "startDate": start_date,
            "endDate": end_date,
            "location": {
                "@type": "Place",
                "name": location,
                "address": address
            },
            "url": url
        }

elif schema_type == "Video":
    st.subheader("Video Schema Fields")
    name = st.text_input("Video Title")
    description = st.text_area("Description")
    upload_date = st.text_input("Upload Date (YYYY-MM-DD)")
    content_url = st.text_input("Video URL")
    thumbnail_url = st.text_input("Thumbnail URL")

    if st.button("Generate Schema Markup"):
        schema = {
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "name": name,
            "description": description,
            "uploadDate": upload_date,
            "contentUrl": content_url,
            "thumbnailUrl": thumbnail_url
        }

elif schema_type == "Blog Post" or schema_type == "Article":
    st.subheader(f"{schema_type} Schema Fields")
    headline = st.text_input("Headline")
    author = st.text_input("Author")
    date_published = st.text_input("Date Published (YYYY-MM-DD)")
    article_body = st.text_area("Article Body")
    url = st.text_input("URL")
    image = st.text_input("Image URL")

    if st.button("Generate Schema Markup"):
        schema = {
            "@context": "https://schema.org",
            "@type": "BlogPosting" if schema_type == "Blog Post" else "Article",
            "headline": headline,
            "author": {
                "@type": "Person",
                "name": author
            },
            "datePublished": date_published,
            "articleBody": article_body,
            "url": url,
            "image": image
        }

elif schema_type == "Breadcrumb":
    st.subheader("Breadcrumb Schema Fields")
    breadcrumb_list = st.text_area("Enter breadcrumb items in order (Format: Name|URL, one per line)")

    if st.button("Generate Schema Markup"):
        items = [line.split("|") for line in breadcrumb_list.strip().split("\n") if "|" in line]
        item_list = [{
            "@type": "ListItem",
            "position": i + 1,
            "name": name.strip(),
            "item": url.strip()
        } for i, (name, url) in enumerate(items)]

        schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": item_list
        }

if schema:
    st.subheader("Generated JSON-LD Schema Markup")
    st.code(json.dumps(schema, indent=2), language="json")
