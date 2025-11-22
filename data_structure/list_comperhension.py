domains = ['www.google.com',
           'www.facebook.com',
           'www.twitter.com',
           'www.linkedin.com',
           'localhost',
           'openai.com',
           'WWW.ExquIsItE-DomAin.Org'
           ]

# List comprehension to extract domain names without 'www.' and convert to lowercase
cleaned_domains = [
                domain.lower().replace('www.', '') #Data Transformation
                for domain in domains              #Looping
                if '.' in domain       #Condition Filtering
                ]

print("Original domains: ", domains)
print("Cleaned domains: ", cleaned_domains)
print("#" * 50)
