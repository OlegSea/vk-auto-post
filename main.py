import vk, json, requests, time, datetime, os, random
with open("settings.json", 'r', encoding="utf-8") as f:
    settings = json.load(f)

with open("credentials.json", 'r', encoding="utf-8") as f:
    credentials = json.load(f)
login = credentials['login']
password = credentials['password']
session = vk.AuthSession(settings["appID"], login, password, scope="wall, photos")
vk_api = vk.API(session, v="5.102")

def publish (fileName, date):
    files = {"photo" : open(settings["inputFolder"] + fileName, 'rb')}

    uploadServer = vk_api.photos.getWallUploadServer(group_id=settings["groupID"])
    with requests.post(uploadServer["upload_url"], files = files) as temp:
        uploadedData = json.loads(temp.text)
    timeUnix = time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y %H:%M:%S").timetuple())
    savedPhoto = vk_api.photos.saveWallPhoto(server = uploadedData["server"], hash = uploadedData["hash"], photo = uploadedData["photo"], group_id = settings["groupID"])
    attachments = "photo" + str(savedPhoto[0]["owner_id"]) + "_" + str(savedPhoto[0]["id"])
    try:
        vk_api.wall.post(owner_id= int(settings["groupID"]) * -1 , attachments=attachments, publish_date=int(timeUnix))
    except Exception:
        print ("Skipped that one")

d0 = datetime.datetime.strptime(settings["dateStart"], '%d/%m/%Y')
d1 = datetime.datetime.strptime(settings["dateFinish"], '%d/%m/%Y')
delta = (d1 - d0)
count = 0
i = time.mktime(datetime.datetime.strptime(settings["dateStart"] + " 00:00:00", "%d/%m/%Y %H:%M:%S").timetuple())+ 3600 * int(settings["timeZone"])
while i < time.mktime(datetime.datetime.strptime(settings["dateFinish"] + " 00:00:00", "%d/%m/%Y %H:%M:%S").timetuple()) + 3600 * int(settings["timeZone"]):
    try:
        fileSelected = random.choice(os.listdir(settings["inputFolder"]))
    except Exception:
        print ("No Files!")
        break
    publish(fileSelected, str(datetime.datetime.utcfromtimestamp(i).strftime('%d/%m/%Y %H:%M:%S')))
    print (str(datetime.datetime.utcfromtimestamp(i).strftime('%d/%m/%Y %H:%M:%S')) + "    " + fileSelected)
    try:
        os.remove(settings["inputFolder"] + fileSelected)
    except Exception:
        print("There is a post on that time already")
        break
    time.sleep(int(settings["postDelay"]))
    i += int(float(settings["step"]) * 3600)