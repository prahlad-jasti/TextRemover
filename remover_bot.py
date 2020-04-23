import praw
import os
from imgurpython import ImgurClient
from PIL import Image
from no_remove import remove_text
import urllib.request as req

reddit = praw.Reddit(client_id='acrtj7jRqKQlSw',
                     client_secret='3dOyTX5ijxMYhgca02T32Ptt-y0',
                     user_agent='<console:new_bot:0.0.1 (by /u/str1kebeam)>',
                     username='str1kebeam',
                     password='stg90shredder')

bot_command = "!nooneremover"
rat = reddit.submission(id = 'g6saca')
for comment in rat.comments.list():
	if bot_command in comment.body:
		im_url = rat.url
		im = Image.open(req.urlopen(im_url))
		fixed_im = remove_text(im)

		imgur_id = '005256541d37601'
		imgur_secret = 'f9201c7f160d580c760b9309b89cd860abfc8810'
		access_token = 'bea39eedbfe832ebfe5f2e119b2f823f875788d4'
		refresh_token = '89575a19c0b720f56421dbc5806061219336e06e'
		client = ImgurClient(imgur_id, imgur_secret, access_token, refresh_token)
		config = {
				'album': None,
				'name':  'Catastrophe!',
				'title': 'Catastrophe!',
				'description': 'doge'
			}
		fixed_im.save('fixed.jpg')

		image = client.upload_from_path('fixed.jpg', config = config, anon = False)
		fixed_im_link = format(image['link'])
		comment.reply(fixed_im_link)
		break
