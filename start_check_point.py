__author__ = "Manouchehr Rasouli"
__date__ = "7/Aug/2017, 8/Aug/2017"

from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController
from url import app
from config_pack import configuration_manager

# Import services
import services


config = configuration_manager.ConfigPack()
version = config.get_app_version()
banner = """
Up time Application v %s
Copyright (c) 2017 Sanay
""" % version


class MyBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Up time check point service is a mini app that gather data for main service from whole points'
        arguments = [
            (['-v', '--version'], dict(action='version', version=banner)),
            ]


class UpTime(CementApp):
    class Meta:
        label = 'Uptime'
        base_controller = MyBaseController


with UpTime('app') as apps:
    try :
        # Read config pack to start app on this configuration
        apps.run()
        # Start services
        services.StartServices()
        app_port = config.get_app_port()
        app_host = config.get_app_host()
        app.run(debug=True, port=app_port, host=app_host, use_reloader=False)
    except Exception as e:
        print(str(e))
