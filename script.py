from util.TextBuffer import TextBuffer
import json


def writeFile(fileName, fileContent):
    f = open(fileName, 'wb')
    f.write(fileContent.encode('utf-8'))
    f.flush()
    f.close()

f = open('story.html')
content = f.read()
f.close()

t = TextBuffer(content)

result = t.get_text_part("<tw-passagedata", "</tw-passagedata>")
resultDict = dict()
while result is not False:

    title = TextBuffer.get_parameter_data(result, "name")
    scene_content = TextBuffer.get_text_til_end(result, "\">")
    temp = TextBuffer(scene_content)
    linksArray = []
    link_result = temp.get_text_part("[[", "]]")
    while link_result is not False:
        print(link_result)
        temp.replace_string("[[" + link_result + "]]", "")
        link_parts = link_result.split("|")
        link_desc = link_parts[0]
        link_target = link_parts[1]
        linksArray.append({'desc': link_desc, 'target': link_target})
        link_result = temp.get_text_part("[[", "]]")
    content = temp.get_text()
    resultDict[title] = {'content': content, 'links': linksArray}
    # Search next part
    result = t.get_text_part("<tw-passagedata", "</tw-passagedata>")
    print("Title = " + title)
jsonData = json.dumps(resultDict, sort_keys=True, indent=4, ensure_ascii=False)
print(jsonData)
writeFile('story.json', jsonData)

