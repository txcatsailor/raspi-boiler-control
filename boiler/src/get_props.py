from lxml import etree

def prop(tag): 
    xml = etree.parse('boiler_props.xml').getroot()
    
    path = '/config/'+tag+'/text()'
    
    text = xml.xpath(path)
    
    return text