from urllib import request
url_requested = request.urlopen('https://simaticit.amb2.siemens.de/snr/Default.aspx?SN=SC-PDK60274')

if 200 == url_requested.code:
    html_content = str(url_requested.read())


html_index_min = 0
html_index_max = 0

material_index = html_content.index("Materialnummer der gescannten Seriennummer")

html_index_min = material_index
html_index_max = material_index + 250

html_index = html_content.index('A5E', html_index_min, html_index_max)

a5e_erg = html_content[html_index]+html_content[html_index+1]+html_content[html_index+2]+html_content[html_index+3]+html_content[html_index+4]+html_content[html_index+5]+html_content[html_index+6]+html_content[html_index+7]+html_content[html_index+8]+html_content[html_index+9]+html_content[html_index+10]

print(a5e_erg)