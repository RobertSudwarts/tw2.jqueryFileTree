import os
import glob
import tw2.core as twc


filetree_js = twc.JSLink(modname=__name__, 
                            filename='static/jqueryFileTree.js')

filetree_css = twc.CSSLink(modname=__name__,
                            filename='static/jqueryFileTree.css')


pth = os.path.dirname(os.path.abspath(__file__))
img_pth = os.path.join(pth, 'static/images', '*.*')
# hmmm... really?? you can't simplify this any further??
images = map(os.path.basename, glob.glob(img_pth))

image_links = [twc.Link(modname=__name__, 
                        filename='static/images/%s' % img ) for img in images]