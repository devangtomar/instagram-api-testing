from instapy import InstaPy

session = InstaPy(username="be_ayushmann", password="XXXXXX", headless_browser=True)
session.login()
celebs_IDs = ['cristiano', 'arianagrande', 'therock', 'kyliejenner', 'selenagomez', 'kimkardashian', 'leomessi',
              'beyonce', 'justinbieber', 'natgeo', 'kendalljenner', 'taylorswift', 'neymarjr', 'jlo', 'nike',
              'khloekardashian', 'nickiminaj', 'mileycyrus', 'katyperry', 'kourtneykardash', 'kevinhart4real',
              'ddlovato', 'virat.kohli', 'realmadrid', 'theellenshow', 'fcbarcelona', 'badgalriri', 'zendaya',
              'iamcardib', 'kingjames', 'chrisbrownofficial', 'billieeilish', 'champagnepapi', 'shakira',
              'championsleague', 'victoriassecret', 'vindiesel', 'davidbeckham', 'gigihadid', 'nasa', 'dualipa',
              'priyankachopra', 'justintimberlake', 'emmawatson', 'shawnmendes', 'shraddhakapoor', 'maluma', '9gag',
              'snoopdogg', 'iamsrk', 'sushantsinghrajput', 'leomessi', 'virat.kohli', 'cristiano', 'nike',
              'beingsalmankhan', 'sunnyleone', 'taylorswift', 'amitabhbachchan', 'natgeo', 'madhuridixitnene',
              'deepikapadukone', 'parineetichopra', 'jacquelinef143', 'gal_gadot', 'kiaraaliaadvani', 'priyankachopra',
              'norafatehi', 'anushkasharma', 'katrinakaif', 'therock', 'kevinhart4real', 'nehakakkar', 'aliaabhatt',
              'shraddhakapoor', 'urvashirautela', 'dishapatani', 'narendramodi', 'instagram']
session.follow_by_list(followlist=celebs_IDs, times=10, sleep_delay=0, interact=False)
session.end()
