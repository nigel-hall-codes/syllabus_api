from __future__ import print_function
import requests
import json
import cv2

class Tests():
    def test_image_sent(self):


        addr = 'http://localhost:5000'
        test_url = addr + '/api/send_syllabus'

        # prepare headers for http request
        content_type = 'image/jpeg'
        headers = {'content-type': content_type}

        img = cv2.imread(r'C:\PycharmProjects\BOT_ENV\SyllabusAPI\IMG_2114.jpeg')
        # encode image as jpeg
        _, img_encoded = cv2.imencode('.jpg', img)
        # send http request with image and receive response
        response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
        # decode response
        print(json.loads(response.text))


t = Tests()
t.test_image_sent()


