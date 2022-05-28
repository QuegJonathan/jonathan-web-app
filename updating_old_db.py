import json
from main import db, BlogPost
from datetime import date

with open('blog.json', "r") as data:
    # Reading old data
    data_read = json.load(data)

for i in data_read:
    new_post = BlogPost(
        title=data_read[i]['Title'],
        subtitle=data_read[i]['Subtitle'],
        body=data_read[i]['Body'],
        img_url=data_read[i]['img_url'],
        author_id=1,
        date=date.today().strftime("%B %d, %Y")
    )
    db.session.add(new_post)
    db.session.commit()
