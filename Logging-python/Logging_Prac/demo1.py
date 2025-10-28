import logging
import mylib


logging.basicConfig(
    filename="demo1.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("Imani")

def main():
    logger.info("Started")
    mylib.do_something()
    logger.info("Finished")

if __name__ == "__main__":
    main()
