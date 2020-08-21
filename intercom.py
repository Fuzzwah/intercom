import configparser
import time

from client import MumbleClient


class InterCom:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('intercom.ini')
        self.mumble_client = MumbleClient(config['mumbleclient'])
        self.exit = False

    def run(self):
        self.mumble_client.send_input_audio()
    
    def stop(self):
        self.mumble_client.clear_input()

if __name__ == '__main__':
    try:
        InterCom().run()
    except KeyboardInterrupt:
        InterCom().stop()
    except Exception as e:
        raise e
