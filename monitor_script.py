from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from pathlib import Path
import json
class MonitorVentas(PatternMatchingEventHandler, Observer):
    def __init__(self, path='.', patterns='*', logfunc=print):
        PatternMatchingEventHandler.__init__(self, patterns)
        Observer.__init__(self)
        self.schedule(self, path=path, recursive=False)
        self.log = logfunc 

    def on_created(self, event):
        # This function is called when a file is created
        extencion = Path(event.src_path).suffix
        if extencion == ".txt":
            archivo_txt = Path(event.src_path).name
            self.log(f"{archivo_txt} ¡Agregado!")
            path = Path(event.src_path)
            self.load_json(path)
    
    def load_json(self, ruta):
        f = open(ruta, "r")
        content = f.read()
        jsondecoded = json.loads(content)
        for key, value in jsondecoded.items():
            print(f"{key}: {value}")
