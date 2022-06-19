import re
text = "d dog  dgdfgdf dogog dogogog dogogogog"
result = re.findall(r'(d[og]{,4})+', text)
print(result)
