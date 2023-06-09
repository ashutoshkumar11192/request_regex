import requests
import re
link = requests.get('https://www.failory.com/startups/india#%E2%80%8D-300-startups-in-india')
a = link.text
l1 = re.findall('<h3>\d+\) (.*?)</h3>',a)
print(l1)
