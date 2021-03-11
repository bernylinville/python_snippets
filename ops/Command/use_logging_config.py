import logging
import logging.config

logging.config.fileConfig('logging.cnf')

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
