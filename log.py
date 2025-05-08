# Abstração
# Escolha composição ao inves de herança
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o Método Log')
    
    def log_error(self, msg):
        self._log(f'ERROR: {msg}')
    
    def log_sucess(self, msg):
        self._log(f'Sucess: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg},  ({self.__class__.__name__})'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(f'{msg_formatada}\n')
        print(msg_formatada) 
    
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg}, ({self.__class__.__name__})')



