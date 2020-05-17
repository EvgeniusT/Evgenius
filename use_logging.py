import os, platform, logging

if platform.platform().startswith('Mac Os'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), \
                                os.getenv('HONEPATH'), \
                                'telt.log')
else:
    logging_file = os.path.join(os.getenv('HOME'), 'test.log')

print('Сохраняем лок в ', logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : % (levelname)s : %(messege)s',
    fileneme = logging_file,
    filemode = 'w',
)

logging.debug("Начало программы")
logging.info("Какие-то действия")
logging.warning("Программа умирает")