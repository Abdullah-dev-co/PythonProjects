print('WEBSITE URL CHECKER :')
url = input("\nEnter your website URL :")

if url.startswith("https://"):
    print('Website uses HTTPS (secure)')
elif url.startswith("http://"):
    print("Website uses HTTP (not secure)")
else:
    print("not a complete URL")