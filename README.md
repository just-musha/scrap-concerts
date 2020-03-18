#### Web scraper

Collects info about concerts from specific sites.

Scraps the following data:

- name
- date
- description
- image

#### How to use

```$ scrapy crawl <SPIDER_NAME>```

Example:

```$ scrapy crawl glavclub```

#### Results
Result JSON file is located at ```~/scrap-concert-results``` dir.

Images are downloaded into ```~/scrap-concert-results/full``` directory.
