import streamlit as st
import json

st.set_page_config(page_title="Schema Markup Generator", layout="wide")
st.title("📄 Schema Markup Generator")

schema_type = st.selectbox("Select a schema type", [
    "Entity", "FAQ", "Product", "Local Business",
    "Service", "Event", "Video", "Blog Post",
    "Article", "Breadcrumb"
])

schema = {
    "@context": "https://schema.org",
    "@type": schema_type.replace(" ", "")
}

if schema_type == "Entity":
    schema["name"] = st.text_input("Name")
    schema["description"] = st.text_area("Description")
    schema["url"] = st.text_input("URL")
    schema["logo"] = st.text_input("Logo URL")
    same_as = st.text_area("Same As (comma separated social/profile URLs)")
    if same_as:
        schema["sameAs"] = [s.strip() for s in same_as.split(",")]

elif schema_type == "FAQ":
    st.subheader("Add FAQ Entries")
    faq_items = []
    num_faqs = st.number_input("How many FAQs?", min_value=1, value=1, step=1)
    for i in range(int(num_faqs)):
        q = st.text_input(f"Question {i+1}")
        a = st.text_area(f"Answer {i+1}")
        if q and a:
            faq_items.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a
                }
            })
    if faq_items:
        schema["mainEntity"] = faq_items

elif schema_type == "Product":
    schema["name"] = st.text_input("Product Name")
    schema["description"] = st.text_area("Product Description")
    schema["sku"] = st.text_input("SKU")
    schema["brand"] = {
        "@type": "Brand",
        "name": st.text_input("Brand Name")
    }
    schema["offers"] = {
        "@type": "Offer",
        "priceCurrency": st.text_input("Price Currency", value="USD"),
        "price": st.text_input("Price"),
        "availability": st.text_input("Availability", value="https://schema.org/InStock"),
        "url": st.text_input("Offer URL")
    }

elif schema_type == "Local Business":
    schema["name"] = st.text_input("Business Name")
    schema["description"] = st.text_area("Description")
    schema["url"] = st.text_input("Website URL")
    schema["logo"] = st.text_input("Logo URL")
    schema["image"] = [st.text_input("Image URL")]

    schema["sameAs"] = st.text_area("SameAs (comma-separated URLs)").split(",")

    schema["address"] = {
        "@type": "PostalAddress",
        "streetAddress": st.text_input("Street Address"),
        "addressLocality": st.text_input("City"),
        "addressRegion": st.text_input("Region/State"),
        "postalCode": st.text_input("Postal Code"),
        "addressCountry": st.text_input("Country")
    }
    schema["geo"] = {
        "@type": "GeoCoordinates",
        "latitude": st.text_input("Latitude"),
        "longitude": st.text_input("Longitude")
    }
    schema["hasMap"] = st.text_input("Google Maps URL")
    schema["contactPoint"] = {
        "@type": "ContactPoint",
        "contactType": st.text_input("Contact Type (e.g. Sales, Support)"),
        "url": st.text_input("Contact URL")
    }

elif schema_type == "Service":
    schema["name"] = st.text_input("Service Name")
    schema["description"] = st.text_area("Service Description")
    schema["provider"] = {
        "@type": "Organization",
        "name": st.text_input("Provider Name")
    }

elif schema_type == "Event":
    schema["name"] = st.text_input("Event Name")
    schema["startDate"] = st.text_input("Start Date (YYYY-MM-DD)")
    schema["endDate"] = st.text_input("End Date (optional)")
    schema["eventAttendanceMode"] = st.text_input("Attendance Mode")
    schema["eventStatus"] = st.text_input("Event Status")

elif schema_type == "Video":
    schema["name"] = st.text_input("Video Title")
    schema["description"] = st.text_area("Description")
    schema["thumbnailUrl"] = [st.text_input("Thumbnail URL")]
    schema["uploadDate"] = st.text_input("Upload Date")
    schema["contentUrl"] = st.text_input("Video Content URL")

elif schema_type == "Blog Post" or schema_type == "Article":
    schema["headline"] = st.text_input("Headline")
    schema["author"] = {
        "@type": "Person",
        "name": st.text_input("Author Name")
    }
    schema["publisher"] = {
        "@type": "Organization",
        "name": st.text_input("Publisher Name"),
        "logo": {
            "@type": "ImageObject",
            "url": st.text_input("Publisher Logo URL")
        }
    }
    schema["datePublished"] = st.text_input("Date Published")

elif schema_type == "Breadcrumb":
    st.subheader("Breadcrumb List")
    item_list = []
    num_items = st.number_input("How many breadcrumb items?", min_value=1, value=2, step=1)
    for i in range(int(num_items)):
        item_name = st.text_input(f"Item {i+1} Name")
        item_url = st.text_input(f"Item {i+1} URL")
        item_list.append({
            "@type": "ListItem",
            "position": i+1,
            "name": item_name,
            "item": item_url
        })
    schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": item_list
    }

st.subheader("Generated Schema Markup")
st.code(json.dumps(schema, indent=2), language="json")
