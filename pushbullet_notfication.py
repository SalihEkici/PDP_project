from pushbullet import PushBullet
import key

API_KEY = key.API_KEY

pb = PushBullet(API_KEY)
push = pb.push_note("ALERT","There is a gas leak!!")