from logging import getLogger
from typing import Self

from cqupt_jwnews_rss.const import NEWS_URL
from cqupt_jwnews_rss.grabber.base import BaseGrabber
from cqupt_jwnews_rss.model import News
from httpx2 import Client

from cqupt_jwnews_rss_grabber_sdenv.config import config

logger = getLogger(__name__)


class SdenvGrabber(BaseGrabber):
    """使用sdenv抓取教务通知"""

    client: Client

    def __init__(self):
        self.client = Client(
            proxy=config.SDENV_SERVER_URL, headers={"Accept-Encoding": "identity"}
        )

    def __enter__(self) -> Self:
        return self

    def get_news(self) -> list[News]:
        resp = self.client.get(NEWS_URL, verify=False)
        # del resp.headers["Content-Encoding"]
        # print(resp.headers)
        logger.debug(resp.text)
        return list(News.from_page_source(resp.text))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
