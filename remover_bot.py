import praw
from PIL import Image
from no_remove import remove_text
import urllib.request
reddit = praw.Reddit(client_id='acrtj7jRqKQlSw',
                     client_secret='3dOyTX5ijxMYhgca02T32Ptt-y0',
                     user_agent='<console:new_bot:0.0.1 (by /u/str1kebeam)>',
                     username='str1kebeam',
                     password='stg90shredder')
bot_command = "!nooneremover"
rat = reddit.submission(id = 'fqpze2')
im_url = rat.url
print(im_url)
im = Image.open(urllib.request.urlopen(im_url))
remove_text(im).show()