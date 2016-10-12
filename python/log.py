import logging

import logging
logging.basicConfig(
    filename='/tmp/example.log',
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)
logging.debug('messagem debug')
logging.info('mensagem info')
logging.warning('mensagem Warning')
logging.critical('mensagem critica')
