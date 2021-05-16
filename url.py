__author__ = "Manouchehr Rasouli, Amirreza Balaboland"
__date__ = "1/Aug/2017, 3/Aug/2017, 4/Aug/2017, 5/Aug/2017"

from flask import Flask
from flask_restful import Api

# This url file redirect urls for
from receive_service.receive_url import ReceiveUrl
from receive_service.remove_url import RemoveUrl
from config_pack import configuration_manager

try:
    app = Flask(__name__)
    api = Api(app)

    # Redirect received request to handlers
    config = configuration_manager.ConfigPack()
    receive_url = config.get_app_url_register_url()
    remove_url = config.get_app_url_remove_url()

    # And then add resources for the urls
    api.add_resource(ReceiveUrl, receive_url)
    api.add_resource(RemoveUrl, remove_url)

except Exception as e:
    pass
    # Pass all exception that accure after keyboard interupt
