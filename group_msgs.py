import json                                                             
import numpy as np
jsFile = json.load( open('U1ZQR43RB.json','r') )                        

users_list = np.unique([js['user'] for js in jsFile])

msgs_per_user = {}

for user in users_list: 
	ts = [js['ts'] for js in jsFile if js['user'] == user] 
	text = [js['text'] for js in jsFile if js['user'] == user] 
	msgs_per_user[user] = list(zip([float(w) for w in ts], text))

for user in msgs_per_user.keys(): 
	user_dict = {} 
	msgs = sorted(msgs_per_user[user]) 
	ts_key = msgs[0][0] 
	while ts_key < msgs[-1][0]: 
		grouped_msgs = [w[1] for w in msgs if (w[0] >= ts_key) and (w[0] < ts_key+120)] 
		if grouped_msgs: 
			user_dict[ts_key] = grouped_msgs 
		ts_key += 120 
	with open(user+'.json','w') as wfile: 
		json.dump(user_dict, wfile) 