from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import HtmlFormatter
from pathlib import Path
import sys
import ntpath
import imgkit
import os

pathlist = Path(sys.argv[1]).glob('./*.*')
if not os.path.exists(sys.argv[2]):
    os.makedirs(sys.argv[2])
for path in pathlist:
    path_in_str = str(path)
    file_name_we = str(sys.argv[2]) + "/" + str(ntpath.basename(path_in_str).replace(".", "-")) + ".html"
    code = open(path_in_str, "r").read()
    f = open(file_name_we, "w")
    # save html
    print("Saving %s with %s highlighting" % (file_name_we, sys.argv[3]))
    filename = ntpath.basename(path_in_str)
    lexer = get_lexer_for_filename(filename)
    f.write((highlight(code, lexer, HtmlFormatter(full=True,highlight=sys.argv[3], linenos=True))))
    f.close()
    # gen png
    file_name_we_for_img = str(sys.argv[2]) + "/" + str(ntpath.basename(path_in_str).replace(".", "-")) + ".png"
    imgkit.from_file(file_name_we, file_name_we_for_img)
