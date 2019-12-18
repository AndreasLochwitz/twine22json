from util.TextBuffer import TextBuffer

print("Hello, World!")

f = open('data/Twine2Test.html')
content = f.read()
f.close()

t = TextBuffer(content)
r = t.get_text_part("<tw-storydata", "</tw-storydata")
print(r)
t.set_text(r)
t.reset()
r = t.get_text_part("tw-passagedata", ">")
print(r)
print(t.get_parameter_data(r, "name"))
print(t.get_parameter_data(r, "pid"))
print(t.get_parameter_data(r, "tags"))

t.reset()

result = t.get_text_part("<tw-passagedata", "</tw-passagedata>")
z = 1
while result is not False:
    print("z = " + str(z))
    print(result)
    # temp = TextBuffer(result)
    scene_content = TextBuffer.get_text_til_end(result, "\">")
    temp = TextBuffer(scene_content)
    link_result = temp.get_text_part("[[", "]]")
    while link_result is not False:
        print(link_result)
        temp.replace_string("[[" + link_result + "]]", "")
        link_result = temp.get_text_part("[[", "]]")
        print(temp.get_text())
    z = z + 1
    result = t.get_text_part("<tw-passagedata", "</tw-passagedata>")

