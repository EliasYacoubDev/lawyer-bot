import scrapy
from courtlistener_rag.items import CourtlistenerRagItem
import re
class CourtSpider(scrapy.Spider):
    name = "court_spider"
    allowed_domains = ["courtlistener.com"]
    start_urls = [
        "https://www.courtlistener.com/opinion/10640395/united-states-v-richard-walker/"
    ]

    def parse(self, response):
        item = CourtlistenerRagItem()

        # Extracting the key fields
        item["case_title"] = response.css("h1#caption::text").get(default="").strip()
        item["court_name"] = response.css("h4.case-court::text").get(default="").strip()
        item["docket_number"] = response.xpath("//strong[contains(text(),'Docket Number')]/following-sibling::text()").get(default="").strip()
        item["citations"] = response.xpath("//strong[contains(text(),'Citations')]/following-sibling::text()").get(default="").strip()
        item["judges"] = response.xpath("//strong[contains(text(),'Judges')]/following-sibling::text()").get(default="").strip()
        item["opinion_author"] = response.css("h3.opinion-section-title::text").get(default="").strip()
        raw_text = response.css("div.plaintext > pre.inline::text").getall()
        joined_text = " ".join(raw_text)
        item["opinion_text"] = re.sub(r"\s+", " ", joined_text).strip()


        self.logger.info("Parsed item: %s", item)
        yield item