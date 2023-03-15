def extract_url(xml_string):
    start = xml_string.find("<url>") + len("<url>")
    end = xml_string.find("</url>")

    if start >= len("<url>") and end > start:
        url = xml_string[start:end]
        if url.startswith("http://"):
            url = url[len("http://"):]
        elif url.startswith("https://"):
            url = url[len("https://"):]
        return url