from log import LogFileMixin

class Device:
    def __init__(self, name):
        self._name = name
        self._active = False

    def activate(self):
        if not self._active :
            self._active = True

    def desactivate(self):
        if self._active:
            self._active = False

class Television(Device, LogFileMixin):
    def activate(self):
        super().activate()
        
        if self._active:
            msg = f'{self._name} is active'
            self.log_sucess(msg)

    def desactivate(self):
        super().desactivate()

        if not self._active:
            msg = f'{self._name} is desactivate'
            self.log_sucess(msg)
