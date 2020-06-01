import re #for regular expressions
from urllib.parse import urlparse

def getDomain(url):
    parsed_uri = urlparse(url)
    result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return result;

def getDomainWithoutSchema(url):
    parsed_uri = urlparse(url)
    result = '{uri.netloc}'.format(uri=parsed_uri)
    return result;

def hasLinks(string): 
    links = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", string) 
    return len(links) > 0

def getlinks(string): 
    URL_REGEX = r"""((?:(?:https|ftp|http)?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|org|uk)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|uk|ac)\b/?(?!@)))"""
    links = re.findall(URL_REGEX, string)
    
    valid_links = []
    for link in links:
        ValidHostnameRegex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$";
        
        #valid hosts only allow some characters
        if re.match(ValidHostnameRegex, getDomainWithoutSchema(link)):
            valid_links.append(link)

    if(len(valid_links) > 0):
        return list(map(getDomain, valid_links))
    
    return ();

def limpiar_texto(x):
    x = re.sub(r"&amp", "and", x)
    x = re.sub(r"\x89Û_", "", x)
    x = re.sub(r"\x89ÛÒ", "", x)
    x = re.sub(r"\x89ÛÓ", "", x)
    x = re.sub(r"\x89ÛÏ", "", x)
    x = re.sub(r"let\x89Ûªs", "lets", x)
    x = re.sub(r"\x89Û÷", "", x)
    x = re.sub(r"\x89Ûª", "", x)
    x = re.sub(r"\x89Û\x9d", "", x)
    x = re.sub(r"å_", "", x)
    x = re.sub(r"\x89Û¢", "", x)
    x = re.sub(r"\x89Û¢åÊ", "", x)
    x = re.sub(r"åÊ", "", x)
    x = re.sub(r"åÈ", "", x)
    x = re.sub(r"Ì©", "e", x)
    x = re.sub(r"å¨", "", x)
    x = re.sub(r"SuruÌ¤", "suruc", x)
    x = re.sub(r"åÇ", "", x)
    x = re.sub(r"åÀ", "", x)
    x = re.sub(' +', ' ', x) #remove duplicated spaces
    x=x.lower()
    x=sacar_puntuacion(x)
    return x

def sacar_puntuacion(x):
  puntuacion="@#!?,¿+&*_[]-%.:/();$=><|{}^" + "'`"
  for p in puntuacion:
    x=x.replace(p, f'')
  return x 