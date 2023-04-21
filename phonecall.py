import messagebird
client = messagebird.Client('<your-api-key>')
try:
    msg = client.voice_message_creat('+254704666130 wanted a call!',{'voice' : 'male'})
    print(msg.__dict__)
except messagebird.client.ErrorExcetion:
    for error in e.errors:
        print(error)