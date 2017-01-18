import sys
import os
path = os.path.dirname(sys.modules[__name__].__file__)
path = os.path.join(path, '..')
sys.path.insert(0, path)
from pytib import getSylComponents, Agreement, Segment
from pytib.common import open_file
import re

#print(getSylComponents().get_parts('དེའིའོ'))

#print(getSylComponents().get_info('ཤིའི'))

#print(Agreement().part_agreement('ཁྲིས', 'གི'))

#print(AntTib().to_ant_text('དེའིའོ'))
#print(Segment().segment('འདི་ནི་ཕལ་ཆེ་བས་བསྟན་པ་ཡིན་ཏེ།', unknown=1, space_at_punct=False))

t = '''༄༅། །བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའི་ཆོ་ག
༄༅༅། །རྒྱ་གར་སྐད་དུ། བོ་དྷི་ཙིཏྟ་ཨུཏྤཱ་ད་བི་དྷི། བོད་སྐད་དུ། བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའི་ཆོ་ག །
སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ། །

ཕྱོགས་བཅུའི་འཇིག་རྟེན་གྱི་ཁམས་མཐའ་ཡས་མུ་མེད་པ་དག་ན་བཞུགས་པའི་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་དང་། དམ་པའི་ཆོས་དང་། བྱང་ཆུབ་སེམས་དཔའི་དགེ་འདུན་ཆེན་པོ་དང་བཅས་པ་ཐམས་ཅད་ལ་ཕྱག་འཚལ་ལོ་། །སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་བདག་ལ་དགོངས་སུ་གསོལ། །དག་མིང་འདི་ཞེས་བགྱི་བས། ཐོག་མ་དང་ཐ་མ་མ་མཆིས་པའི་འཁོར་བ་ན་འཁོར་བའི་ཚེ། ལུས་དང་ངག་དང་ཡིད་ཀྱིས། སངས་རྒྱས་དང་ཆོས་དང་། དགེ་འདུན་དང་། ཕ་མ་དང་། སེམས་ཅན་དག་ལ་སྡིག་པ་མི་དགེ་བའི་ལས་བགྱིད་པ་དང་བགྱིད་དུ་སྩལ་བ་དང་། བགྱིད་པ་ལ་རྗེས་སུ་ཡི་རང་བ་ཅི་མཆིས་པ་དེ་དག་ཐམས་ཅད་གཅིག་ཏུ་བསྡོམས་ཤིང་བསྡུས་ཏེ། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ཀྱི་སྤྱན་སྔར་བླ་ན་མེད་པའི་སོ་སོར་བཤགས་པས་འཆགས་སོ། །མི་འཆབ་བོ། །སླན་ཆད་འདི་ལྟ་བུ་མི་བགྱིད་དོ། །དེ་སྐད་ལན་གསུམ་བཟླས། སྡིག་པ་བཤགས་པའོ། །

སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་བདག་ལ་དགོངས་སུ་གསོལ། །ཇི་ལྟར་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་ཀྱིས་བསོད་ནམས་ཀྱི་རྗེས་སུ་ཡི་རང་བ་བླ་ན་མེད་པ་ཐུགས་སུ་ཆུད་པ་དེ་བཞིན་དུ་བདག་མིང་འདི་ཞེས་བགྱི་བ་ཡང་སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་དང་རང་སངས་རྒྱས་དང་འཕགས་པ་ཉན་ཐོས་ཐམས་ཅད་དང་། འགྲོ་བ་མ་ལུས་པའི་བསོད་ནམས་ཐམས་ཅད་ལ་རྗེས་སུ་ཡི་རང་ངོ༌། །དེ་སྐད་ལན་གསུམ་བཟླས། བསོད་ནམས་ལ་རྗེས་སུ་ཡི་རང་བའོ། །

སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་བདག་ལ་དགོངས་སུ་གསོལ། །བདག་མིང་འདི་ཞེས་བགྱི་བས་སངས་རྒྱས་ཀྱི་གདུང་རྒྱུན་མི་འཆད་པར་བགྱི་བའི་སླད་དུ། དུས་འདི་ནས་བཟུང་སྟེ། བྱང་ཆུབ་སྙིང་པོ་ལ་མཆིས་ཀྱི་བར་དུ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་རྐང་གཉིས་ཀྱི་མཆོག་ལ་སྐྱབས་སུ་མཆི་སྟེ། ཐུགས་རྗེ་ཆེན་པོ་དང་ལྡན་པ། ཐམས་ཅད་མཁྱེན་པ། ཐམས་ཅད་གཟིགས་པ། འཇིགས་པ་ཐམས་ཅད་དང་བྲལ་བ། སྐྱེས་བུ་ཆེན་པོ། །སྐྱེས་བུ་ཁྱུ་མཆོག་སྐུ་བསམ་གྱིས་མི་ཁྱབ་པ། བླ་ན་མེད་པའི་སྐུ། ཆོས་ཀྱི་སྐུ་མངའ་བ་ལ་སྐྱབས་སུ་མཆིའོ། །ཆོས་འདོད་ཆགས་དང་བྲལ་བའི་མཆོག་ལ་སྐྱབས་སུ་མཆི་སྟེ། བླ་ན་མེད་པ་དེ་བཞིན་གཤེགས་པ་ལ་མངའ་བ། ཞི་བ་ཆོས་ཀྱི་སྐུ་སོ་སོར་རང་གིས་རིག་པ་ལ་སྐྱབས་སུ་མཆིའོ། །དགེ་འདུན་དུལ་བ་ཚོགས་ཀྱི་མཆོག་ལ་སྐྱབས་སུ་མཆི་སྟེ། ཕྱོགས་བཞིའི་འཕགས་པ་ཕྱིར་མི་ལྡོག་པའི་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོའི་དགེ་འདུན་ལ་སྐྱབས་སུ་མཆིའོ། །དེ་སྐད་ལན་གསུམ་བཟླས། སྐྱབས་སུ་འགྲོ་བའོ། །

སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་བདག་ལ་དགོངས་སུ་གསོལ། །བདག་མིང་འདི་ཞེས་བགྱི་བ་དུས་འདི་ནས་བཟུང་སྟེ་བྱང་ཆུབ་ཀྱི་སྙིང་པོ་ལ་གནས་ཀྱི་བར་དུ། སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་ལ་དུས་ཇི་ལྟ་བ་དང་སྟོབས་ཅི་མཆིས་པ་བཞིན་དུ་བདག་དབུལ་ཞིང་མཆིས་ན། མགོན་པོ་ཐུགས་རྗེ་ཆེན་པོ་དང་ལྡན་པ་དག་བདག་བཞེས་སུ་གསོལ། །དེ་སྐད་ལན་གསུམ་བཟླས། བདག་དབུལ་བའོ། །

སངས་རྒྱས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཐམས་ཅད་བདག་ལ་དགོངས་སུ་གསོལ། །ཇི་ལྟར་སྔོན་གྱི་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་རྫོགས་པའི་སངས་རྒྱས་དག་སྔོན་བྱང་ཆུབ་སེམས་དཔའི་སྤྱད་པ་སྤྱོད་པའི་ཚེ། སེམས་ཅན་ཐམས་ཅད་བསྒྲལ་བ་དང་། སེམས་ཅན་ཐམས་ཅད་དགྲོལ་བ་དང་། སེམས་ཅན་ཐམས་ཅད་དབུགས་དབྱུང་བ་དང་། སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་དང་། སེམས་ཅན་ཐམས་ཅད་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ལ་དགོད་པའི་སླད་དུ་ཅི་ལྟར་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ཐུགས་བསྐྱེད་པ་དེ་བཞིན་དུ་བདག་མིང་འདི་ཞེས་བགྱི་བ་ཡང་དུས་འདི་ནས་བཟུང་སྟེ། བྱང་ཆུབ་སྙིང་པོ་ལ་མཆིས་ཀྱི་བར་དུ་སེམས་ཅན་ཐམས་ཅད་བསྒྲལ་བ་དང་། སེམས་ཅན་ཐམས་ཅད་དགྲོལ་བ་དང་། སེམས་ཅན་ཐམས་ཅད་དབུགས་དབྱུང་བ་དང༌། སེམས་ཅན་ཐམས་ཅད་ཡོངས་སུ་མྱ་ངན་ལས་འདའ་བ་དང་། སེམས་ཅན་ཐམས་ཅད་ཐམས་ཅད་མཁྱེན་པའི་ཡེ་ཤེས་ལ་དགོད་པའི་སླད་དུ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་དོ། །ཇི་ལྟར་སྔོན་གྱི་སངས་རྒྱས་བཅོམ་ལྡན་འདས་རྣམས་དང་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོ་དེ་དག་གིས་དངོས་པོ་ཐམས་ཅད་དང་བྲལ་བ་ཕུང་པོ་དང་ཁམས་དང་སྐྱེ་མཆེད་དང༌ཟུང་བ་དང་འཛིན་པ་རྣམ་པར་སྤངས་པ། ཆོས་བདག་མེད་པ་མཉམ་པ་ཉིད་ཀྱིས་རང་གི་སེམས་གཟོད་མ་ནས་མ་སྐྱེས་པ། སྟོང་པ་ཉིད་ཀྱི་ངོ་བོ་ཉིད་ཀྱི་བྱང་ཆུབ་ཀྱི་སེམས་བསྐྱེད་པ་དེ་བཞིན་དུ། བདག་མིང་འདི་ཞེས་བགྱི་བ་ཡང་དུས་འདི་ནས་བཟུང་སྟེ། བྱང་ཆུབ་ཀྱི་སྙིང་པོ་ལ་མཆིས་ཀྱི་བར་དུ་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་དོ། །ཇི་ལྟར་སྔོན་གྱི་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་དེ་དག་གིས་བདུད་དཔུང་དང་བཅས་པ་ཕམ་པར་མཛད་དེ། ཉིད་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་པ་དེ་བཞིན་དུ། བདག་མིང་འདི་ཞེས་བགྱི་བ་ཡང་བདུད་དཔུང་དང་བཅས་པ་མཐའ་དག་ཕམ་པར་བགྱིས་ཏེ། བདག་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་བགྱིའོ། །ཇི་ལྟར་སྔོན་གྱི་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་དེ་དག་གིས་ཉིད་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས་ཆོས་ཀྱི་འཁོར་ལོ་རབ་ཏུ་བསྐོར་བ་དེ་བཞིན་དུ། བདག་མིང་འདི་ཞེས་བགྱི་བ་ཡང་ཉིད་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ཏེ། ཆོས་ཀྱི་འཁོར་ལོ་རབ་ཏུ་བསྐོར་བར་བགྱིའོ། །ཇི་ལྟར་སྔོན་གྱི་དེ་བཞིན་གཤེགས་པ་དགྲ་བཅོམ་པ་ཡང་དག་པར་རྫོགས་པའི་སངས་རྒྱས་དེ་དག་གིས་ཉིད་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ནས་ཚོགས་ཡོངས་སུ་བསྡུས་པ་དེ་བཞིན་དུ། བདག་མིང་འདི་ཞེས་བགྱི་བ་ཡང་ཉིད་མངོན་པར་རྫོགས་པར་སངས་རྒྱས་ཏེ་ཚོགས་ཡོངས་སུ་བསྡུ་བར་བགྱིའོ། །བྱང་ཆུབ་མཆོག་ཏུ་སེམས་ནི་བསྐྱེད་པར་བགྱི། །སེམས་ཅན་ཐམས་ཅད་བདག་གིས་མགྲོན་དུ་གཉེར། །བྱང་ཆུབ་སྤྱོད་མཆོག་ཡིད་འོང་སྤྱད་པར་བགྱི། །འགྲོ་ལ་ཕན་ཕྱིར་སངས་རྒྱས་འགྲུབ་པར་ཤོག །དེ་སྐད་ལན་གསུམ་བཟླས། བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའོ། །

བདག་གིས་བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའི་དགེ་བའི་རྩ་བ་འདི་དང་། གཞན་ཡང་བདག་གིས་བསོད་ནམས་ཅུང་ཟད་ཅི་བགྱིས་པ་དང་། བགྱིད་པ་དང་བགྱིད་པར་འགྱུར་བ་དེ་དག་ཐམས་ཅད་ཕ་མ་ལ་སོགས་པ་སེམས་ཅན་ཐམས་ཅད་དང་བདག་གི་དོན་དུ་བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ཏུ་ཡོངས་སུ་བསྔོའོ། །བདག་གིས་བསོད་ནམས་འདིས་ཕ་མ་ལ་སོགས་པ་སེམས་ཅན་མ་བརྒལ་བ་རྣམས་ནི་བསྒྲལ་ལོ། །མ་གྲོལ་བ་རྣམས་ནི་དགྲོལ་ལོ། །དབུགས་མ་ཕྱིན་པ་རྣམས་ནི་དབུགས་དབྱུང་ངོ༌། །ཡོངས་སུ་མྱ་ངན་ལས་མ་འདས་པ་རྣམས་ནི། ཡོངས་སུ་མྱ་ངན་ལས་བཟླའོ། །མངོན་པར་རྫོགས་པར་སངས་མ་རྒྱས་པ་རྣམས་ནི་མངོན་པར་རྫོགས་པར་འཚང་རྒྱ་བར་བགྱིའོ། །སྐྱབས་མ་མཆིས་པ་དང་། གནས་མ་མཆིས་པ་དང་། དཔུང་གཉེན་མ་མཆིས་པའི་འཇིག་རྟེན་གྱི་སྐྱབས་དང་གནས་དང་། དཔུང་གཉེན་དུ་གྱུར་ཅིག །བསོད་ནམས་འདི་ཡིས་ཐམས་ཅད་གཟིགས་པ་ཉིད། །ཐོབ་ནས་ཉེས་པའི་དགྲ་རྣམས་ཕམ་བྱས་ཏེ། རྒ་ནད་འཆི་བའི་རླབས་ཆེན་འཁྲུགས་པ་ཡི། །སྲིད་པའི་མཚོ་ལས་འགྲོ་བ་འདོན་པར་བགྱི། །དེ་ནས་བདག་སྦྱིན་པ་སྩོལ་བ་དང་། ཚུལ་ཁྲིམས་བསྲུང་བ་དང་། བཟོད་པ་བསྒོམ་པ་དང་། བརྩོན་འགྲུས་བརྩམ་པ་དང་། བསམ་གཏན་ལ་མཉམ་པར་གཞག་པ་དང་། ཤེས་རབ་རྣམ་པར་དཔྱོད་པ་དང་། ཐབས་མཁས་པ་ལ་སློབ་པ་ཅི་ཡང་རུང་སྟེ། དེ་དག་ཐམས་ཅད་སེམས་ཅན་ཐམས་ཅད་ཀྱི་དོན་དང་ཕན་པ་དང་བདེ་བའི་སླད་དུ། བླ་ན་མེད་པ་ཡང་དག་པར་རྫོགས་པའི་བྱང་ཆུབ་ལས་བརྩམས་ཏེ། འདས་པ་དང༌། མ་འོངས་པ་དང་། ད་ལྟར་བྱུང་བའི་བྱང་ཆུབ་སེམས་དཔའ་ཆེན་པོ་སྙིང་རྗེ་ཆེན་པོ་དང་ལྡན་པ། ཐེག་པ་ཆེན་པོ་ལ་ཡང་དག་པར་ཞུགས་པ་ས་ཆེན་པོ་ལ་གནས་པ་རྣམས་ཀྱི་རྗེས་སུ་མཐུན་པར་འཇུག་གོ། །འཕགས་པ་ངག་བདག་བྱང་ཆུབ་སེམས་དཔའ་ལགས་ཀྱི། བྱང་ཆུབ་སེམས་དཔའ་ལགས་པར་གཟུང་དུ་གསོལ། །ས་དང་ཆུ་དང་མེ་དང་རླུང་། །རྩི་དང་ནགས་ཀྱི་ཤིང་ལྟ་བུར། །རྟག་ཏུ་སྲོག་ཆགས་ཐམས་ཅད་ཀྱིས། །འདོད་དགུར་དཔག་མེད་སྤྱོད་པར་ཤོག །མཐོང་བ་དང་ནི་རེག་པ་དང་། །ཐོས་པ་དང་ནི་དྲན་པས་ཀྱང་། །བདག་ནི་སེམས་ཅན་ཐམས་ཅད་ཀྱི། །ནད་རྣམས་གསོ་བར་བགྱིད་གྱུར་ཅིག །སེམས་ཅན་ཐམས་ཅད་བདེ་དང་ལྡན་གྱུར་ཅིག །ངན་འགྲོ་ཐམས་ཅད་རྟག་ཏུ་སྟོངས་པར་ཤོག །བྱང་ཆུབ་སེམས་དཔའ་གང་དག་སུ་བཞུགས་པ། །དེ་དག་ཀུན་གྱི་སྨོན་ལམ་འགྲུབ་གྱུར་ཅིག །དེ་སྐད་ལན་གསུམ་བཟླས། བསོད་ནམས་བསྔོ་བའོ། །

བྱང་ཆུབ་ཏུ་སེམས་བསྐྱེད་པའི་ཆོ་ག །སློབ་དཔོན་མཁས་པ་ཆེན་པོ་འཕགས་པ་ཀླུ་སྒྲུབ་ཀྱི་ཞལ་སྔ་ནས་མཛད་པ་རྫོགས་སྟོ།། །།རྒྱ་གར་གྱི་མཁན་པོ་སུ་རན་དྲ་བོདྷི་དང་། ཞུ་ཆེན་གྱི་ལོ་ཙཱ་བ་བན་དེ་ཡེ་ཤེས་སྡེས་བསྒྱུར་ཅིང་ཞུས་ཏེ་གཏན་ལ་ཕབ་པའོ།། '''

print(Segment().segment('ནམ་མཁར་མཐར་', reinsert_aa=True))
print(Segment().segment('ནམ་མཁར་མཐར་', distinguish_ra_sa=True))
print(Segment().segment('ནམ་མཁར་མཐར་', reinsert_aa=True, distinguish_ra_sa=True))

