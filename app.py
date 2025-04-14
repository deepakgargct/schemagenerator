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

elif schema_type == "Service":
    st.subheader("Service Schema Fields")
    name = st.text_input("Service Name")
    service_type = st.text_input("Service Type")
    provider_name = st.text_input("Service Provider Name")
    provider_url = st.text_input("Service Provider URL")
    description = st.text_area("Description")
    price = st.text_input("Price")
    currency = st.text_input("Currency")
    valid_from = st.text_input("Valid From (Date)")

    if st.button("Generate Schema Markup"):
        service_schema = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": name,
            "serviceType": service_type,
            "provider": {
                "@type": "Organization",
                "name": provider_name,
                "url": provider_url
            },
            "description": description,
            "offers": {
                "@type": "Offer",
                "price": price,
                "priceCurrency": currency,
                "validFrom": valid_from
            }
        }
        schema = service_schema

elif schema_type == "Event":
    st.subheader("Event Schema Fields")
    name = st.text_input("Event Name")
    start_date = st.text_input("Start Date (ISO Format)")
    end_date = st.text_input("End Date (ISO Format)")
    location = st.text_input("Event Location")
    description = st.text_area("Event Description")
    organizer_name = st.text_input("Organizer Name")
    organizer_url = st.text_input("Organizer URL")
    ticket_url = st.text_input("Ticket URL")
    
    if st.button("Generate Schema Markup"):
        event_schema = {
            "@context": "https://schema.org",
            "@type": "Event",
            "name": name,
            "startDate": start_date,
            "endDate": end_date,
            "location": {
                "@type": "Place",
                "name": location
            },
            "description": description,
            "organizer": {
                "@type": "Organization",
                "name": organizer_name,
                "url": organizer_url
            },
            "offers": {
                "@type": "Offer",
                "url": ticket_url
            }
        }
        schema = event_schema

elif schema_type == "Video":
    st.subheader("Video Schema Fields")
    name = st.text_input("Video Title")
    description = st.text_area("Video Description")
    url = st.text_input("Video URL")
    thumbnail = st.text_input("Thumbnail URL")
    upload_date = st.text_input("Upload Date (ISO Format)")

    if st.button("Generate Schema Markup"):
        video_schema = {
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "name": name,
            "description": description,
            "url": url,
            "thumbnailUrl": thumbnail,
            "uploadDate": upload_date
        }
        schema = video_schema

elif schema_type == "Blog Post":
    st.subheader("Blog Post Schema Fields")
    title = st.text_input("Blog Post Title")
    author = st.text_input("Author Name")
    date_published = st.text_input("Date Published (ISO Format)")
    blog_url = st.text_input("Blog URL")
    content = st.text_area("Content")
    
    if st.button("Generate Schema Markup"):
        blog_post_schema = {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": title,
            "author": {
                "@type": "Person",
                "name": author
            },
            "datePublished": date_published,
            "url": blog_url,
            "articleBody": content
        }
        schema = blog_post_schema

elif schema_type == "Article":
    st.subheader("Article Schema Fields")
    headline = st.text_input("Article Headline")
    author = st.text_input("Author Name")
    date_published = st.text_input("Date Published (ISO Format)")
    article_url = st.text_input("Article URL")
    article_body = st.text_area("Article Body")
    
    if st.button("Generate Schema Markup"):
        article_schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": headline,
            "author": {
                "@type": "Person",
                "name": author
            },
            "datePublished": date_published,
            "url": article_url,
            "articleBody": article_body
        }
        schema = article_schema

elif schema_type == "Breadcrumb":
    st.subheader("Breadcrumb Schema Fields")
    breadcrumb_name = st.text_input("Breadcrumb Name")
    breadcrumb_url = st.text_input("Breadcrumb URL")
    
    if st.button("Generate Schema Markup"):
        breadcrumb_schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "name": breadcrumb_name,
                    "item": breadcrumb_url
                }
            ]
        }
        schema = breadcrumb_schema

# Display the generated Schema Markup
if schema:
    st.subheader("Generated Schema Markup")
    st.code(json.dumps(schema, indent=2), language="json")
