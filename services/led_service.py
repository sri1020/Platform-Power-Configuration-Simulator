from utils.logger import logger

class LedService:

    def runtime(self):
        logger.info(
            "LED State -> Runtime"
        )
        print("LED -> Runtime")

    def shutdown(self):
        logger.info(
            "LED State -> Shutdown"
        )

        print("LED -> Shutdown Complete")

    def hibernate(self):
        logger.info(
            "LED State -> Hibernate"
        )
        print("LED -> Hibernate Complete")