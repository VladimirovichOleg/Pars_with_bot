import logging

from parser.main_pars import main

logger = logging.getLogger()
FORMAT = "%(asctime)s %(name)s %(levelname)s %(message)s"
logging.basicConfig(level=logging.INFO, filename=f"main_pars.log", filemode="w", format=FORMAT)

if __name__ == '__main__':
    main()
