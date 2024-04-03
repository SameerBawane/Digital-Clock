import pyshorteners

def shorten_url(url):
    # Initialize a Shortener object
    s = pyshorteners.Shortener()

    # Shorten the URL
    shortened_url = s.tinyurl.short(url)

    return shortened_url

def main():
    print("Welcome to the URL Shortener!")
    url = input("Enter the URL to shorten: ")
    shortened_url = shorten_url(url)
    print("Shortened URL:", shortened_url)

if __name__ == "__main__":
    main()
