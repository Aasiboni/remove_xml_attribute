import os
import xml.etree.ElementTree as ET
import sys

class CommentedTreeBuilder(ET.TreeBuilder):
    def comment(self, data):
        self.start(ET.Comment, {})
        self.data(data)
        self.end(ET.Comment)

def removeattribute(tag, attribute, xml_file):
    print('################# '+xml_file+' START #################')
    manifest_file = os.path.abspath(os.path.join(xml_file))
    xml_tree = ET.parse(manifest_file, parser=ET.XMLParser(target=CommentedTreeBuilder()))
    root = xml_tree.getroot()

    for child in root:

        if child.tag == tag and attribute in child.attrib:
                print('Before: ' + child.tag, child.attrib)
                del child.attrib[attribute]
                print('After: ' + child.tag, child.attrib)
                print('\n')
        xml_tree.write(xml_file)
    print('################# '+xml_file+' END #################')

tag = sys.argv[1]
attribute_to_remove = sys.argv[2]
print("tag=" + tag)
print("attribute_to_remove=" + attribute_to_remove)

if len(sys.argv) != 3:
    print("Invalid number of arguments, script should receive 2 args:\n"
          "Example: remove_attribute.py tag_name attribute_name\n")
    sys.exit()

for filename in os.listdir('.'):
    if filename.endswith(".xml"):
        removeattribute(tag, attribute_to_remove, filename)
    else:
        continue

print("Done!")
