import datetime
from STT import STT
from TTS import TTS

# credit Herishikesh Balgote (aka. the goat)

def convert_mmddyy(input):
    
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    raw = input.split(' ')
    curr_year = str(datetime.date.today().year)
    
    month_index = -1
    for i in range(len(months)):
        if months[i].lower() == raw[0].lower():
            month_index = i + 1
    month = str(month_index)
    if len(month) < 2:
        month = '0' + month
    
    day = ''
    for c in raw[1]:
        if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            day += c
    if len(day) < 2:
        day = '0' + day
    
    return curr_year + '-' + month + '-' + day


# print(convert_mmddyy('March 31st')) # output: 2023-03-31
# TTS.tts("What is the Date")
# test  = STT.recognize_speech(True)
# converted = convert_mmddyy(str(test))
# print(converted)
# TTS.tts("The Converted Date is " + str(converted)) 
