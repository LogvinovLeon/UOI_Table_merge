import urllib.request

import lxml.html


def get_table_data(url):
    code = urllib.request.urlopen(url).read()
    return lxml.html.fromstring(code).xpath('//td')


def get_dict(table_data):
    db = [[element.text_content() for element in table_data][i::8][:-3] for i in range(1, 8)]
    res = dict()
    for i in range(len(db[0])):
        res[db[0][i]] = [List[i] for List in db][1:]
    return res

def th(s):
    return '<th>%s</th>' % s

def td(s):
    return '<td>%s</td>' % s

def tr(s):
    return '<tr>\n%s\n</tr>' % s


page1 = get_table_data('http://olymp.sumdu.edu.ua/tour1.html')
page2 = get_table_data('http://olymp.sumdu.edu.ua/tour2.html')
dict1 = get_dict(page1)
dict2 = get_dict(page2)
Dict = dict()
for key in dict1:
    Dict[key] = dict1[key][:-2] + dict2[key][:-2] + \
                [int(dict1[key][4]) + int(dict2[key][4])] + \
                [int(dict1[key][5]) + int(dict2[key][5])]
List = [[key] + Dict[key] for key in Dict]
List.sort(key=lambda x: x[10], reverse=1)
f = open('output.html', 'w', encoding='utf8')
html = '<table border=1>\n' +\
       tr('\n'.join(map(th, ['User'] + [chr(i+ord('A')) for i in range(8)] + ['Solved', 'Score']))) + \
       '\n'.join(map(tr, ['\n'.join([td(el[i]) for i in range(11)]) for el in List])) + \
       '\n</table>'
f.write(html)
f.close()

