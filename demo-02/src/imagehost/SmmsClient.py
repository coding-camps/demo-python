# -*- coding: utf-8 -*-
import requests
import json
from urllib.parse import urljoin, urlunparse


class SMMS(object):
    baseUrl = r'https://sm.ms/api/v2'

    # init
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.token = None
        self.profile = None
        self.headers = None

    # user > get api token
    def get_api_token(self):
        url = self.__class__.baseUrl + '/token'
        data = {
            'username': self.username,
            'password': self.password
        }
        resp = requests.post(url, data=data).json()
        self.token = resp['data']['token']
        self.headers = {'Authorization': self.token}
        print(json.dumps(resp, indent=4))

    # user > get user profile
    def get_profile(self):
        url = self.__class__.baseUrl + '/profile'
        resp = requests.post(url, headers=self.headers).json()
        self.profile = resp['data']
        print(json.dumps(resp, indent=4))

    # image > Clear Temporary History - Clear IP Based Temporary Upload History
    def clear_ip_history(self):
        url = self.__class__.baseUrl + '/clear'
        resp = requests.get(url).json()
        print(json.dumps(resp, indent=4))

    # image > Temporary History - IP Based Temporary Upload History
    def get_ip_history(self):
        url = self.__class__.baseUrl + '/history'
        resp = requests.get(url).json()
        print(json.dumps(resp, indent=4))

    # image > Deletion - Image Deletion
    def delete_image(self, image_hash):
        url = self.__class__.baseUrl + '/delete/' + image_hash
        resp = requests.get(url).json()
        print(json.dumps(resp, indent=4))

    # image > Upload History - Upload History
    def get_uploaded_history(self):
        url = self.__class__.baseUrl + '/upload_history'
        resp = requests.get(url, headers = self.headers).json()
        self.upload_history = resp['data']
        print(json.dumps(resp, indent=4))

    # image > Upload - Upload Image
    def upload_image(self, path):
        url = self.__class__.baseUrl + '/upload'
        try:
            with open(path, 'rb') as file:
                files = {'smfile': file}
                resp = requests.post(url, files=files, headers=self.headers).json()
                print(json.dumps(resp, indent=4))
                if resp['success']:
                    self.url = resp['data']['url']
                    print(self.url)
                else:
                    print(resp['message'])
        except Exception as e:
            print(e)

    # Album > Edit Album Item - Add/Remove item to Album
    # GET /albums/:album_id/item
    def add_or_remove_item(self, album_id):
        pass

    # Album > Delete Album - Album Deletion
    # GET /albums/:album_id/delete
    def delete_album(self, album_id):
        pass

    # Album > Create Albums - Create Album
    # POST /albums
    def create_album(self, album_name, album_desc):
        url = self.baseUrl + '/albums'
        data = {
            'album_name': album_name,
            'album_description': album_desc
        }
        resp = requests.post(url, data=data, headers=self.headers)
        print(resp.status_code)
        resp=resp.json()
        print(json.dumps(resp, indent=4))
        return resp['data']['id']

    # Album > Get Album Items - Get All Album Items
    # GET /albums/:album_id
    def get_all_album_items(self, album_id):
        pass

    # Album > Get Albums - Get All Albums
    # GET /albums
    def get_all_albums(self):

        pass


if __name__ == '__main__':
    smmsClient = SMMS("coder211@163.com", "coder211@163")
    smmsClient.get_api_token();
    print(smmsClient.token)
    # smmsClient.get_profile()
    # smmsClient.get_ip_history()
    # smmsClient.upload_image('/Users/yuheng/Downloads/ycc.jpg')
    # smmsClient.get_ip_history()
    # smmsClient.clear_ip_history()
    # smmsClient.get_ip_history()
    # smmsClient.get_uploaded_history()
    # album_id = smmsClient.create_album('sugarCC', album_desc="sugarCC-photos");
    # print(album_id)
