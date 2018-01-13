import requests

from ChWt_Warmind.settings import SOCIAL_AUTH_BUNGIE_API_KEY, SOCIAL_AUTH_BUNGIE_ORIGIN


# from django.core.serializers

class API(object):
    """
    Class to access Bungie.net User API
    """
    bungie = 'https://bungie.net'
    bungie_api = bungie + '/Platform'

    def __init__(self):
        api_key = SOCIAL_AUTH_BUNGIE_API_KEY
        origin_header = SOCIAL_AUTH_BUNGIE_ORIGIN
        self.api_headers = {'Origin': origin_header, "X-API-Key": api_key}
        # TODO: Add "Authorization: Bearer", access_token from social_auth_usersocialauth.extra_data

    def call_bungie_api(self, req: str) -> str:
        """
        Calls the Bungie API
        :param req: The request URL that is built by the calling function
        :type req: str
        :return: APi return data
        :rtype: json
        """
        request_session = requests.session()
        r = request_session.get(req, headers=self.api_headers)
        return_data = r.json()
        return return_data

    def int32(self, hash_id: int) -> int:
        # Required to convert the integers for looking up hashes in the manifest DB
        """
        Convert hash to unsigned 32 bit for Manifest DB Lookup
        :param hash_id: vendor, item or activity hash
        :return: unsigned 32 bit int
        """
        hash_id = int(hash_id)
        if hash_id > 0xFFFFFFFF:
            raise OverflowError
        if hash_id > 0x7FFFFFFF:
            hash_id = int(0x100000000 - hash_id)
            if hash_id < 2147483648:
                return -hash_id
            else:
                return -2147483648
        return hash_id
