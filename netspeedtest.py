import speedtest
import json
import os

test = speedtest.Speedtest()

#code

#get server
print ("#### loading server ") 
test.get_servers()

#get best server
print ("#### loading best server")
best_server = test.get_best_server()

#print(best_server)

#test moduals
print("#### testing download_speed")
download_speed = test.download() /1024 /1024

print("#### testing upload speed")
upload_speed = test.upload() /1024 /1024

print("#### testing ping")
ping = test.results.ping

print(download_speed)
print(upload_speed)
print(ping)

#server information
info = {
    "id" : best_server["id"],
    "host name": best_server["host"],
    "latency" : best_server["latency"],
    "city location" : best_server["name"],
    "country" : best_server["country"],
    "sponsor" : best_server["sponsor"],
    "server link" : best_server["url"],
    "speed test result": {
        "Downlaod speed" : str(download_speed),
        "upload speed" : str(upload_speed),
        "Ping speed" : str(ping)
    }
}

with open("test_result.json", "r+") as file:
    data = json.load(file)
    data.update(info)
    file.seek(0)
    json.dump(data, file)
