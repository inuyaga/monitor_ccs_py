from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from pathlib import Path
import json
from request_appi import AppiResponseMonitor
class MonitorVentas(PatternMatchingEventHandler, Observer):
    def __init__(self, path='.', patterns='*', logfunc=print):
        PatternMatchingEventHandler.__init__(self, patterns)
        Observer.__init__(self)
        self.schedule(self, path=path, recursive=False)
        self.log = logfunc 

    def on_created(self, event):
        # This function is called when a file is created
        path = Path(event.src_path)
        if path.suffix == ".txt":
            self.log(f"{path.name} ¡Agregado!")
            # self.load_json(path)
            response_api = AppiResponseMonitor(path).send()
            print(response_api)
    
    # def load_json(self, ruta):
    #     f = open(ruta, "r")
    #     content = f.read()
    #     jsondecoded = json.loads(content)
    #     for key, value in jsondecoded.items():
    #         print(f"{key}: {value}")
