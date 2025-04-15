# Place this in your main if/elif chain after the other types like Entity, FAQ, etc.

elif schema_type == "Service":
    st.subheader("Service Schema Fields")
    service_name = st.text_input("Service Name")
    service_description = st.text_area("Service Description")
    service_provider_name = st.text_input("Provider Name")
    service_area = st.text_input("Service Area")

    if st.button("Generate Schema Markup"):
        schema = {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": service_name,
            "description": service_description,
            "provider": {
                "@type": "Organization",
                "name": service_provider_name,
                "areaServed": {
                    "@type": "Place",
                    "name": service_area
                }
            }
        }

elif schema_type == "Event":
    st.subheader("Event Schema Fields")
    event_name = st.text_input("Event Name")
    event_start = st.text_input("Start Date & Time (e.g., 2025-06-01T19:30)")
    event_end = st.text_input("End Date & Time (optional)")
    event_location = st.text_input("Location Name")
    event_address = st.text_input("Location Address")
    event_url = st.text_input("Event URL")

    if st.button("Generate Schema Markup"):
        schema = {
            "@context": "https://schema.org",
            "@type": "Event",
            "name": event_name,
            "startDate": event_start,
            "endDate": event_end if event_end else None,
            "location": {
                "@type": "Place",
                "name": event_location,
                "address": event_address
            },
            "url": event_url
        }

elif schema_type == "Video":
    st.subheader("Video Schema Fields")
    video_name = st.text_input("Video Name")
    video_description = st.text_area("Video Description")
    video_url = st.text_input("Content URL")
    embed_url = st.text_input("Embed URL")
    upload_date = st.text_input("Upload Date (e.g., 2025-04-01)")
    thumbnail_url = st.text_input("Thumbnail URL")

    if st.button("Generate Schema Markup"):
        schema = {
            "@context": "https://schema.org",
            "@type": "VideoObject",
            "name": video_name,
            "description": video_description,
            "contentUrl": video_url,
            "embedUrl": embed_url,
            "uploadDate": upload_date,
            "thumbnailUrl": [thumbnail_url]
        }

elif schema_type == "Blog Post" or schema_type == "Article":
    st.subheader(f"{schema_type} Schema Fields")
    title = st.text_input("Title")
    author = st.text_input("Author Name")
    date_published = st.text_input("Date Published (e.g., 2025-04-01)")
    article_body = st.text_area("Article Body")
    url = st.text_input("Article URL")
    image = st.text_input("Image URL")

    if st.button("Generate Schema Markup"):
        schema = {
            "@context": "https://schema.org",
            "@type": "BlogPosting" if schema_type == "Blog Post" else "Article",
            "headline": title,
            "author": {
                "@type": "Person",
                "name": author
            },
            "datePublished": date_published,
            "articleBody": article_body,
            "mainEntityOfPage": url,
            "image": [image]
        }

elif schema_type == "Breadcrumb":
    st.subheader("Breadcrumb Schema Fields")

    num_items = st.number_input("Number of breadcrumb items", min_value=2, max_value=10, value=3)
    breadcrumb_list = []

    for i in range(int(num_items)):
        name = st.text_input(f"Name for Breadcrumb {i+1}")
        item = st.text_input(f"URL for Breadcrumb {i+1}")
        breadcrumb_list.append({
            "@type": "ListItem",
            "position": i + 1,
            "name": name,
            "item": item
        })

    if st.button("Generate Schema Markup"):
        schema = {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": breadcrumb_list
        }
