import io
import os
import json
import requests
import pytesseract
from PIL import Image
from urllib import request
from quart import Quart

from utils import (
        INST_STORY_URL,
        SESSION_ID,
        USER_ID,
        GITHUB_API_URL
)

COOKIES = {
    'sessionid': SESSION_ID,
    'ds_user_id': USER_ID
}
app = Quart(__name__)


def post_stories_to_blog():
    temp_r = requests.get(INST_STORY_URL, cookies=COOKIES)
    raw_data = temp_r.json()
    stories = [s["display_url"] for s in raw_data['data']['reels_media'][0]['items']]

    for story in stories:
        dw = request.urlopen(story).read()
        stream = io.BytesIO(dw)
        im = Image.open(stream)
        text = pytesseract.image_to_string(im, lang='eng')
        # stories ment to be blogposts should start with @@
        blogtest = text[:2]
        if blogtest == '@@':
            text = text[2:].strip()
            if text[0] == '#':
                title = '# %s' % text[1:].partition('\n')[0]
                text = text[1:len(title)]
            else:
                title = '# %s' % text.partition('\n')[0]
            issue_body = {
                "title": title,
                "body": text,
                "labels": ["instagram"]
            }
            u = requests.post(GITHUB_API_URL, data=json.dumps(issue_body))
            print(u.text)
    return 'OK'


@app.route('/')
async def call_post():
    return post_stories_to_blog()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
