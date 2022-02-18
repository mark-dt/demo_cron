from ruxit.api.base_plugin import RemoteBasePlugin
from ruxit.api.exceptions import ConfigException
import logging
import datetime
import croniter

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class DemoCron(RemoteBasePlugin):
    def initialize(self, **kwargs):
        logger.info("Config: %s", self.config)
        self.cron_str = self.config["cron_str"]
        if not croniter.croniter.is_valid(self.cron_str):
            raise ConfigException(f"Invalid cron string {self.cron_str}")
        self.date_fmt = '%m/%d/%Y, %H:%M'
        now = datetime.datetime.now()
        cron = croniter.croniter(self.cron_str, now)
        self.next = cron.get_next(datetime.datetime)

    def query(self, **kwargs):
        now = datetime.datetime.now()
        _now = now.strftime(self.date_fmt)
        _next = self.next.strftime(self.date_fmt)
        logger.info(f'Now: {_now}')
        logger.info(f'Next: {_next}')
        if _now == _next:
            cron = croniter.croniter(self.cron_str, now)
            self.next = cron.get_next(datetime.datetime)
            logger.info('Do stuff')
            return
        logger.info('Waiting...')
            
