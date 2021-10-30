from instapy import InstaPy

session = InstaPy(username="be_ayushmann", password="XXXXXXX")
session.login()
# scoobyDoo_nonfollowers = session.pick_nonfollowers(username="be_ayushmann", live_match=True, store_locally=True)
# #now, `scoobyDoo_nonfollowers` variable w hich is a list- holds the `Nonfollowers` data of "ScoobyDoo" at requested time
#
# print(scoobyDoo_nonfollowers)

print("End of insta-py")
# non_followers = ['jasi3116', 'kanchan.chetry.165', 'shiwangi_thapa', 'priyanegi_101', 'blingbrushblush', 'sunidhi_agg', 'kavitaladia', 'uttarabharadwaj', 'binitasaha15', 'shreya_26sharma', 'ritika_921', 'pallavi_97a', 'cutie_pie_cute_pooja', 'shruti_rawat_', 'ayushi_tyagi_19', 'mahima0799', 'kbisht99', 'tanuja__shah', 'ki_yara_kapoor24', 'imkoyeldasgupta', 'pratimagurungp.g', 'blumaan', 'dilawish_8076', 'karla_vegas2', 'manali_pant', 'p.r.e.r.n.a_01', 'kanikaa_dobhal11', 'sakshijindal_', 'silk_thapa_09', 'nainagurung8', 'innocentnikita', 't.anu.ft', 'jyotika_gurung', 'laxmii95', 'richa.bansal.5209', 'neha_mahar', 'nisha_panwar21', 'shalini.raikwal', 'iam_sng', 'foodgram9', 'sonasonalimamgain', 'ojasviverma20', 'tanvishrsth', 'thapliyalprietypari', 'samuel_anisha', 'rana_simmu', 'md_artisticsoul', 'mishi.sethi', 'shubu_rana_7279', 'mishty_soni', 'shinu.5218', 'payallgurung', 'suhani__gurung', 'mom_stagramm', 'rana.meenal', 'luv_ruchi', 'cornflower1870', 'saviipasbola', 'conor_sketches', 'tradingcafeindia', 'snehallmahajan', 'officialkeane16', 'lkpsecuritiesltd', 'businessaims', 'investywise', 'unfinance', 'goldbridgemark', 'movie__gasm', 'djmartinjensen', 'thevamps', 'salmahayek', 'aletrevino95', 'onefuckingsuccess', 'javascript.js', 'iansomerhalder', 'obx', 'banterfifa', 'mikaela', 'skysports', 'oneplus', 'oneplus_india', 'cherdleys', 'm10_official', 'josemourinho', 'transferscorner', 'sportbible', 'transfermarkt_official', 'fabriziorom', 'ambsphillips', 'spursofficial', 'buzzfeedtasty', 'davidbeckham', 'drdisrespect', 'two_and_a_half_men_fanpage', 'kartikaaryan', 'lustyfacts', 'charlieputh', 'laurencohan', 'andrewschulz', 'teamcoco', 'henrycavill', 'brunofernandes.10', 'vivaladirt', 'natalia', 'sidemen', 'lenovolegion', 'bewarmers', 'xbox', 'masterigs', 'alienware', 'easportsfifa', 'amcthewalkingdead', 'thewalkingdead', 'premierleague', 'ksi', 'kygomusic', 'jailyneojeda', 'cristiano', 'manchesterunited', 'paulpogba', 'spotify', 'charliesheen', 'robertdowneyjr']
# custom_list = ["user_1", "user_2", "user_49", "user332", "user50921", "user_n"]

custom_list = ['jasi3116', 'kanchan.chetry.165', 'shiwangi_thapa', 'priyanegi_101', 'blingbrushblush', 'sunidhi_agg',
               'kavitaladia', 'uttarabharadwaj', 'binitasaha15', 'shreya_26sharma', 'ritika_921', 'pallavi_97a',
               'cutie_pie_cute_pooja', 'shruti_rawat_', 'ayushi_tyagi_19', 'mahima0799', 'kbisht99', 'tanuja__shah',
               'ki_yara_kapoor24', 'imkoyeldasgupta', 'pratimagurungp.g', 'blumaan', 'dilawish_8076', 'karla_vegas2',
               'manali_pant', 'p.r.e.r.n.a_01', 'kanikaa_dobhal11', 'sakshijindal_', 'silk_thapa_09', 'nainagurung8',
               'innocentnikita', 't.anu.ft', 'jyotika_gurung', 'laxmii95', 'richa.bansal.5209', 'neha_mahar',
               'nisha_panwar21', 'shalini.raikwal', 'iam_sng', 'foodgram9', 'sonasonalimamgain', 'ojasviverma20',
               'tanvishrsth', 'thapliyalprietypari', 'samuel_anisha', 'rana_simmu', 'md_artisticsoul', 'mishi.sethi',
               'shubu_rana_7279', 'mishty_soni', 'shinu.5218', 'payallgurung', 'suhani__gurung', 'mom_stagramm',
               'rana.meenal', 'luv_ruchi', 'cornflower1870', 'saviipasbola', 'snehallmahajan']
session.unfollow_users(amount=84, custom_list_enabled=True, custom_list=custom_list, custom_list_param="all",
                       style="RANDOM", unfollow_after=1, sleep_delay=1)

# for headless sessions
# session = InstaPy(username='test', password='test', headless_browser=True)
