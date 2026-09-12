import re
from urllib.parse import urlparse


def extract_features(url):

    # Make sure the URL has a scheme
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed_url = urlparse(url)

    domain = parsed_url.netloc
    path = parsed_url.path
    query = parsed_url.query

    # Remove port number from domain if present
    domain_without_port = domain.split(":")[0]

    features = {

        # 1. Total URL length
        "url_length": len(url),

        # 2. Domain length
        "domain_length": len(domain_without_port),

        # 3. Path length
        "path_length": len(path),

        # 4. Query length
        "query_length": len(query),

        # 5. Number of dots
        "dot_count": url.count("."),

        # 6. Number of hyphens
        "hyphen_count": url.count("-"),

        # 7. Number of underscores
        "underscore_count": url.count("_"),

        # 8. Number of slashes
        "slash_count": url.count("/"),

        # 9. Number of digits
        "digit_count": sum(char.isdigit() for char in url),

        # 10. Number of special characters
        "special_char_count": len(
            re.findall(r"[^a-zA-Z0-9]", url)
        ),

        # 11. Has @ symbol
        "has_at_symbol": int("@" in url),

        # 12. Has IP address
        "has_ip": int(
            bool(
                re.match(
                    r"^(?:\d{1,3}\.){3}\d{1,3}$",
                    domain_without_port
                )
            )
        ),

        # 13. Uses HTTPS
        "uses_https": int(parsed_url.scheme == "https"),

        # 14. Number of subdomains
        "subdomain_count": max(
            0,
            len(domain_without_port.split(".")) - 2
        ),

        # 15. Suspicious keyword
        "has_suspicious_keyword": int(
            any(
                word in url.lower()
                for word in [
                    "login",
                    "verify",
                    "verification",
                    "account",
                    "update",
                    "secure",
                    "bank",
                    "password",
                    "signin",
                    "confirm",
                    "credential"
                ]
            )
        ),

        # 16. URL contains double slash after protocol
        "has_double_slash": int("//" in path),

        # 17. URL contains a percent encoded character
        "has_percent_encoding": int("%" in url),

        # 18. URL contains a question mark
        "has_question_mark": int("?" in url),

        # 19. URL contains an equals sign
        "has_equal_sign": int("=" in url),

        # 20. URL contains a shortened URL service
        "is_shortened_url": int(
            any(
                service in domain_without_port.lower()
                for service in [
                    "bit.ly",
                    "tinyurl.com",
                    "t.co",
                    "goo.gl",
                    "ow.ly",
                    "is.gd",
                    "buff.ly"
                ]
            )
        )
    }

    return features

if __name__ == "__main__":

    test_url = "https://google.com"

    result = extract_features(test_url)

    print("\nURL:", test_url)
    print("\nExtracted Features:")

    for feature, value in result.items():
        print(f"{feature}: {value}")