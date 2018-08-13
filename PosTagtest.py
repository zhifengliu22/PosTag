import requests
import json

def postTest():
    url = "http://127.0.0.1:5000/POSTagging/"
    data = {"content": "“我最想感谢的人是我的导师付磊教授。在他的指导下，我发表8篇SCI论文，总影响因子超过110，这是我给自己最好的毕业礼物。”“希望以后有很多钱，给母校盖几栋楼。”“室友在外地实习，我们带着他的照片来参加典礼，没想到这家伙一早赶回来了。”现场采访环节，毕业生们说着笑着哭着，话语里满含眷恋与感恩。"}
    headers = {"Content-Type" : "application/json"}
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(r.text)

if __name__ == "__main__":
    postTest()