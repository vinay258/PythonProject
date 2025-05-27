#logging-->logging mechanism to maintain the work/program flow into file

import logging

logger=logging.getLogger()
logger.setLevel(logging.INFO)
file_handler=logging.FileHandler("C:\\Users\\vinay\\PycharmProjects\\PythonProject\\Logs1")
logger.addHandler(file_handler)

try:
    a=10
    b="20"
    logger.info("the value of a is {}".format(a))
    logger.info("the value of b is {}".format(b))
    c=a+b
    logger.info("the sum of two values is {}".format(c))
except Exception as es:
    print(es)
    logger.error(es)
finally:
    logger.info("iam done")
