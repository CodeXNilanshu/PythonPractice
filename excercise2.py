##Exercise 2: Extract a product name from a website URL and output should be Iphone 16 Pro Max 256
##https://www.amazon.in/iPhone-16-Pro-Max-256/dp/B0DGHYDZR9

## Iphone 16 Pro Max 256

# url = 'https://www.amazon.in/iPhone-16-Pro-Max-256/dp/B0DGHYDZR9'

### method 1 :
# url = url[22:-14]
# url = url.replace('-',' ')
# url = url.title()
# print(url)

### method 2: Better way
# product_name_end_index = url.index('/dp')
# product_name_start_index = url.index('in/') + 3
#
# url = url[product_name_start_index:product_name_end_index]
# url = url.replace('-',' ')
# url = url.title()
# print(url)