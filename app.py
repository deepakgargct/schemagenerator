import streamlit as st
import json

# Function to generate Local Business schema
def generate_local_business():
    st.subheader("Local Business Schema Markup")
    name = st.text_input("Business Name")
    description = st.text_area("Business Description")
    url = st.text_input("Business Website URL")
    logo = st.text_input("Logo URL")
    image = st.text_input("Image URL")
    same_as = st.text_area("SameAs URLs (comma-separated)")
    telephone = st.text_input("Business Phone Number")
    email = st.text_input("Business Email")
    street_address = st.text_input("Street Address")
    city = st.text_input("City / Locality")
    region = st.text_input("State / Region")
    postal_code = st.text_input("Postal Code")
    country = st.text_input("Country")
    hours_of_operation = st.text_area("Business Hours (e.g., Mon-Fri 9AM-5PM)")

    if st.button("Generate JSON-LD", key="local_business_btn"):
        local_business_schema = {
            "@context": "https://schema.org",
            "@type": "LocalBusiness",
            "name": name,
            "description": description,
            "url": url,
            "logo": logo,
            "image": image,
            "sameAs": [s.strip() for s in same_as.split(",") if s.strip()],
            "telephone": telephone,
            "email": email,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": street_address,
                "addressLocality": city,
                "addressRegion": region,
                "postalCode": postal_code,
                "addressCountry": country
            },
            "openingHours": hours_of_operation
        }
        st.code(json.dumps(local_business_schema, indent=2), language="json")

# Function to generate Entity schema
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
        }
        st.code(json.dumps(entity_schema, indent=2), language="json")

# Function to generate FAQ schema
def generate_faq():
    st.subheader("FAQ Schema Markup")
    questions = st.number_input("How many questions to add?", min_value=1, step=1)
    
    faq_list = []
    for i in range(questions):
        question = st.text_input(f"Question {i+1}")
        answer = st.text_area(f"Answer {i+1}")
        faq_list.append({"@type": "Question", "name": question, "acceptedAnswer": {"@type": "Answer", "text": answer}})
    
    if st.button("Generate JSON-LD", key="faq_btn"):
        faq_schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faq_list
        }
        st.code(json.dumps(faq_schema, indent=2), language="json")

# Function to generate Product schema
def generate_product():
    st.subheader("Product Schema Markup")
    name = st.text_input("Product Name")
    description = st.text_area("Product Description")
    sku = st.text_input("Product SKU")
    price = st.number_input("Product Price", min_value=0.0, step=0.01)
    currency = st.selectbox("Currency", ["USD", "EUR", "GBP", "INR", "AUD"])
    availability = st.selectbox("Availability", ["InStock", "OutOfStock", "PreOrder"])
    url = st.text_input("Product URL")
    
    if st.button("Generate JSON-LD", key="product_btn"):
        product_schema = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": name,
            "description": description,
            "sku": sku,
            "offers": {
                "@type": "Offer",
                "url": url,
                "priceCurrency": currency,
                "price": price,
                "availability": f"https://schema.org/{availability}"
            }
        }
        st.code(json.dumps(product_schema, indent=2), language="json")

# Function to generate Service schema
def generate_service():
    st.subheader("Service Schema Markup")
    name = st.text_input("Service Name")
    description = st.text_area("Service Description")
    service_type = st.text_input("Service Type (e.g., Online, In-person)")
    url = st.text_input("Service Website URL")

    if st.button("Generate JSON-LD", key="service_btn"):
        service_schema = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": name,
            "description": description,
            "serviceType": service_type,
            "url": url
        }
        st.code(json.dumps(service_schema, indent=2), language="json")

# Function to generate Event schema
def generate_event():
    st.subheader("Event Schema Markup")
    name = st.text_input("Event Name")
    description = st.text_area("Event Description")
    start_date = st.text_input("Event Start Date (ISO 8601 format)")
    end_date = st.text_input("Event End Date (ISO 8601 format)")
    location = st.text_input("Event Location")
    
    if st.button("Generate JSON-LD", key="event_btn"):
        event_schema = {
            "@context": "https://schema.org",
            "@type": "Event",
            "name": name,
            "description": description,
            "startDate": start_date,
            "endDate": end_date,
            "location": {
                "@type": "Place",
                "name": location
            }
        }
        st.code(json.dumps(event_schema, indent=2), language="json")

# Function to generate Video schema
def generate_video():
    st.subheader("Video Schema Markup")
    name = st.text_input("Video Name")
    description = st.text_area("Video Description")
    upload_date = st.text_input("Video Upload Date (ISO 8601 format)")
    duration = st.text_input("Video Duration (e.g., PT2H for 2 hours)")

    if st.button("Generate JSON-LD", key="video_btn"):
        video_schema = {
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "name": name,
            "description": description,
            "uploadDate": upload_date,
            "duration": duration
        }
        st.code(json.dumps(video_schema, indent=2), language="json")

# Function to generate Blog Post schema
def generate_blog_post():
    st.subheader("Blog Post Schema Markup")
    headline = st.text_input("Headline")
    description = st.text_area("Description")
    date_published = st.text_input("Date Published (ISO 8601 format)")
    author = st.text_input("Author Name")
    
    if st.button("Generate JSON-LD", key="blog_post_btn"):
        blog_post_schema = {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": headline,
            "description": description,
            "datePublished": date_published,
            "author": {
                "@type": "Person",
                "name": author
            }
        }
        st.code(json.dumps(blog_post_schema, indent=2), language="json")

# Function to generate Article schema
def generate_article():
    st.subheader("Article Schema Markup")
    headline = st.text_input("Headline")
    description = st.text_area("Description")
    date_published = st.text_input("Date Published (ISO 8601 format)")
    author = st.text_input("Author Name")

    if st.button("Generate JSON-LD", key="article_btn"):
        article_schema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": headline,
            "description": description,
            "datePublished": date_published,
            "author": {
                "@type": "Person",
                "name": author
            }
        }
        st.code(json.dumps(article_schema, indent=2), language="json")

# Function to generate Breadcrumb schema
def generate_breadcrumb():
    st.subheader("Breadcrumb Schema Markup")
    item_name = st.text_input("Item Name")
    item_url = st.text_input("Item URL")
    
    breadcrumb_list = []
    breadcrumb_list.append({
        "@type": "ListItem",
        "position": 1,
        "name": item_name,
        "item": item_url
    })
    
    if st.button("Generate JSON-LD", key="breadcrumb_btn"):
        breadcrumb_schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": breadcrumb_list
        }
        st.code(json.dumps(breadcrumb_schema, indent=2), language="json")

# Streamlit Interface
st.title("Schema Markup Generator")

schema_type = st.selectbox("Select Schema Type", [
    "Entity", "Local Business", "FAQ", "Product", "Service", "Event", 
    "Video", "Blog Post", "Article", "Breadcrumb"
])

if schema_type == "Entity":
    generate_entity()
elif schema_type == "Local Business":
    generate_local_business()
elif schema_type == "FAQ":
    generate_faq()
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
    generate_article()
elif schema_type == "Breadcrumb":
    generate_breadcrumb()
