import configparser
import sys
import os
class duplotoken:
    def ChangeToken(Self,tenant,token):
        try:
            configParser = configparser.RawConfigParser()
            home = os.path.expanduser('~')
            configFilePath = home + "/.aws/config"
            configParser.read(configFilePath)
            newvalue = "duplo-jit aws --tenant={} --host https://uniphore-ds.duplocloud.net --token {}".format(tenant,token)
            configParser.set("default",'credential_process',newvalue)
            with open(configFilePath, 'w') as configfile:
                configParser.write(configfile)

        except Exception as e:
            raise e
