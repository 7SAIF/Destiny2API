from warmind_d2.utils import API


class User(object):
    """
    Class to access Bungie.net User API
    """

    def __init__(self):
        pass

    @staticmethod
    def get_bungie_net_user_by_id(uid):
        this_api = API()
        req = API.bungie_api + '/User/GetBungieNetUserById/' + str(uid) + '/'
        return this_api.call_bungie_api(req)

    @staticmethod
    def search_users(display_name):
        this_api = API()
        req = API.bungie_api + '/Platform/User/SearchUsers/?q=' + display_name
        return this_api.call_bungie_api(req)

    @staticmethod
    def get_membership_data_by_id(uid):
        this_api = API()
        req = API.bungie_api + '/Platform/User/GetMembershipsById/' + str(uid) + '/254/'
        return this_api.call_bungie_api(req)

    @staticmethod
    def get_partnerships(uid):
        this_api = API()
        req = API.bungie_api + '/Platform/User/' + str(uid) + '/Partnerships/'
        return this_api.call_bungie_api(req)

    # @staticmethod
    # def get_destiny_single_definition(definition_type, this_hash):
    #     this_api = API()
    #     req = API.bungie + "/platform/Destiny/Manifest/" + definition_type + "/" + this_hash
    #     return this_api.call_bungie_api(req)


