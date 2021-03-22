import json
from typing import Any, Dict

class Utils:

    @staticmethod
    def get_config_file() -> Dict[str, Any]:
        with open("./config.json") as file_handle:
            config = json.load(file_handle)
        return config

    # @staticmethod
    # def serialize(data, restrict=False):
    #     """Convert given object to printable structure
    #     Args:
    #         request: Generic object to be converted in string with json structure
    #         :param data: request to be converted
    #         :param restrict: hide sensitive request
    #     """
    #     dumped = json.dumps(data, default=lambda o: getattr(o, '__dict__', str(o)), check_circular=False)
    #     return Utils.drop_restricted_data(json.loads(dumped)) if restrict else json.loads(dumped)

    # @staticmethod
    # def drop_restricted_data(param):
    #     params = deepcopy(param)
    #     if params and isinstance(params, dict):
    #         for param_key in params.keys():
    #             if str(param_key).upper() in Globals.RESTRICTED_KEYS:
    #                 params[param_key] = "####-###-####"
    #             elif params[param_key] and isinstance(params[param_key], dict):
    #                 params[param_key] = Utils.drop_restricted_data(params[param_key])
    #
    #     return params

    @staticmethod
    def is_null_or_empty(value):
        return value is None or value == 0 or len(value) == 0

    # @staticmethod
    # def get_status_code(info):
    #     return info['statusCode'] if 'statusCode' in info else ''

    @staticmethod
    def get_item_by_id(items, item_id) -> object:
        for item in items:
            if item['id'] == item_id:
                return item
        raise Exception('Item {id} not found.'.format(id=item_id))

    # @staticmethod
    # def is_downsize_request(items):
    #     for item in items:
    #         if item.old_quantity > item.quantity:
    #             return True
    #
    #     return False

    # @staticmethod
    # def check_previous_active_subscription(filter):
    #     config_file = Utils.get_config_file()
    #     fulfilment_resource = FulfillmentResource(Config(
    #         api_url=config_file['apiEndpoint'],
    #         api_key=config_file['apiKey'],
    #         products=config_file['products']
    #     ))
    #     return fulfilment_resource.search_asset_request(filter)


def get_basic_value(base, value):
    if base and value in base:
        return base[value]
    return '-'

def get_value(base, prop, value):
    if prop in base:
        return get_basic_value(base[prop], value)
    return '-'

# def get_param_by_id(param_id):
#     """ Get a parameter of the asset.
#             :param str param_id: Id of the the parameter to get.
#             :return: The parameter with the given id, or ``None`` if it was not found.
#             :rtype: :py:class:`.Param` | None
#             """
#     try:
#         return list(filter(lambda param: param.id == param_id, params))[0]
#     except IndexError:
#         return None
