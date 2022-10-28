from time import sleep
from urllib import request
from BlTochno.Hookah.hookasiteobject import HookaSiteObject, Page, SiteTreeBuilder, tree_traversal,url_parsers
from BlTochno.Telegram.main import main as teleg_main
from BlTochno.common_utils.parser import Parser
from BlTochno.common_utils.urlobject import UrlObject

# ur=UrlObject(url='https://hookah-cat.online/today-we-smoke/?limit=80',
#              parsers=[Parser(regex='class=\"product-layout.*?href=\"(.*?)\"'),Parser(regex=)])

# hrk=HookaSiteObject(
#     name='fdfd',
#     url=ur,
#     parser_deep_level=2
# )
# hrk.parse()
# print('dsds')



# reg='<span style=\"caret-color: rgb\(\d+, \d+, \d+\); (?:text-size-adjust: auto|background-color: transparent);\">(\w+)\W(?:\"<|<)\/span><a href.*?>(.*?)<\/a><span style=\"caret-color: rgb\(\d+, \d+, \d+\); (?:text-size-adjust: auto|background-color: transparent);\">\"*(?:&nbsp;|)(.{3,8})\W<|</span>(.{3,20})\W(.{3,20})<span style=\"caret-color:.*?> - (\d+)%<|<span style=\"margin: 0px;.*?vertical-align: baseline;\">(?:<br>|)(?:</span>|)<a href.*?>(\w+)\W(.*?)<\/a>(?:<span.*?>|) - (\d+)%<'


# tree=SiteTreeBuilder(
#     url_parsers=url_parsers
# )

# print(tree_traversal(tree.tree))
teleg_main()
