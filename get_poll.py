import vk
import time
from pic_generator import *
import warnings
import os

def start_app(w, h,  rgb, f_s, link, b_rgb, b_thick):
    print "Loading..."
    warnings.filterwarnings("ignore")

    session = vk.AuthSession(app_id = '5813182', user_login = '89296301367',
                         user_password = 'danjusha', scope = "wall")
    api = vk.API(session)
    link = str(link.split('/')[-1][4:])
    info = {}
    info['user_id'], info['post_id'] = link.split('_')[0], link.split('_')[1]

    post = api.wall.getById(posts = link)[0]
    for i in range(len(post["attachments"])):
        if (post["attachments"][i]['type'] == 'poll'):
            info['poll_id'] = post["attachments"][i]['poll']['poll_id']

    poll = api.polls.getById(poll_id = info['poll_id'], owner_id = info['user_id'])


    poll_meta = {}
    poll_meta["question"] = poll["question"]
    poll_meta["votes"] = poll["votes"]
    poll_meta["answers_count"] = len(poll["answers"])
    poll_meta["answers"] = poll["answers"]

    poll_meta["question"] = poll_meta["question"][:poll_meta["question"].find("(")]

    poll_meta["question"] = poll_meta["question"]

    os.system("mode con cols=48 lines=40")
    time.sleep(0.5)
    print "App is running"
    print "Here is the input layout:\n"
    
    for i in range(poll_meta["answers_count"]):
        cur = poll_meta["answers"][i]
        
        print i

        print str(cur["rate"])
        for k in range(int(cur["rate"] // 10)):
            print "#",
            time.sleep(0.1)
        print ''
        time.sleep(0.2)

    print '\n'
    color = rgb
    width, height = w, h
    f_size = f_s


    
    while True:
       try:
           poll = api.polls.getById(poll_id = info['poll_id'], owner_id = info['user_id'])
       except:
           print 'no connection'
       poll_meta = {}
       poll_meta["question"] = poll["question"]
       poll_meta["votes"] = poll["votes"]
       poll_meta["answers_count"] = len(poll["answers"])
       poll_meta["answers"] = poll["answers"]
       poll_meta["question"] = poll_meta["question"][:poll_meta["question"].find("(")]
   
       new_img(poll_meta, width, height, color, f_size, b_rgb, b_thick)
       time.sleep(0.5)

