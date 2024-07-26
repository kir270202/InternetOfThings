import requests

a = message.voice

with open(f"{a.file_id}.{a.mime_type.split('/')[-1]}", "rb") as fstream:
    file_info = bot_client.download_file(a.file_id, fstream)
    FOLDER_ID, IAM_TOKEN = "", ""

    with open(f"{a.file_id}.{a.mime_type.split('/')[-1]}", "rb") as fileStream:
        params = {
        'topic': "general",
        'folderId': FOLDER_ID,
        'lang': 'ru-RU'
        }
        headers = {
        'Authorization': 'Bearer ' + IAM_TOKEN,
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        client = HttpClient()
        client.headers.add("Authorization", f"Bearer {IAM_TOKEN}")
        content = StreamContent(fileStream)

        response = requests.post('https://stt.api.cloud.yandex.net/speech/v1/stt:recognize',
        params=params, headers=headers,
        data=content)
        json_response = response.read().decode('utf-8')
        print(json_response)
        audioTest = AudioMessageResult(json_response)
        device_name = None
        value = None

        if audioTest.result.lower().contains("включить") or audioTest.result.lower().contains("включи"):
            value = 1
        elif audioTest.result.lower().contains("устройство 1"):
            device_name = "device1"
        elif audioTest.result.lower().contains ("устройство 2") :
            device_name = "device2"
        elif audioTest.result.lower().contains ("устройство 3") :
            device_name = "device3"
        if value is None or device_name is None:
            bot_client.send_text_message(chat.id, "Sorry, I didn't understand that.", reply_to_message_id=message.message_id)