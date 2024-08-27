import pyshorteners

def shorten_url(long_url):
   
    shortener = pyshorteners.Shortener()

    short_url = shortener.tinyurl.short(long_url)
    print("shorten URL is : ",short_url)

def main():
   
    long_url = input("Enter the long URL: ")
    short_url = shorten_url(long_url)

if __name__ == "__main__":
    main()