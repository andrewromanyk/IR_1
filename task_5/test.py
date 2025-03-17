import re
import basic

pattern = r'''(?x)
(?:[A-Z]\.)+
| \w+(?:-\w+)*
| \$?\d+(?:\.\d+)?%?
| \.\.\.
| [][.,;"’?():_!‘-]
'''

text = "That U.S.A. poster-print costs $12.4!"

import xml.etree.ElementTree as ET

# Default is only "end" events if not specified
context = ET.iterparse("../texts/harry_potter_stone.fb2", events=("start", "end"))


for event, elem in context:
    if event == "start":
        print(f"Opening: <{elem.tag}> with text {elem.text}")

    elif event == "end":
        print(f"Closing: </{elem.tag}> with tail {elem.tail}")
        elem.clear()



