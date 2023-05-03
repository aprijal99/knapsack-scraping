import scrapy, pandas as pd

class KnapsackScraper(scrapy.Spider):
  name = 'KnapsackScraper'
  allowed_domains = ['www.knapsackfamily.com']
  # start_urls = [
  #   'http://www.knapsackfamily.com/knapsack_core/information.php?sname=C_ID&word=C00035480',
  #   'http://www.knapsackfamily.com/knapsack_core/information.php?sname=C_ID&word=C00044142'
  # ]

  def start_requests(self):
    ids = pd.read_csv('knapsack_ids.csv')
    for i in ids.loc[:, 'ID Knapsack']:
      yield scrapy.Request(f'http://www.knapsackfamily.com/knapsack_core/information.php?sname=C_ID&word={i}', self.parse)
  
  def parse(self, response):
    knapsack_id = response.xpath('//font[@class="iw"]/text()').get().strip()
    property_table = response.xpath('//table[@class="d3"]/tr')
    organism_table = response.xpath('//table[@class="org"]/tr')

    for row in organism_table:
      organism = row.xpath('./td/text()').getall()
      yield {
        'Knapsack ID': knapsack_id,
        'Name': ', '.join(property_table[0].xpath('./td/text()').getall()),
        'Molecular Formula': property_table[1].xpath('./td/text()').get().strip(),
        'Molecular Weight': property_table[2].xpath('./td/text()').get().strip(),
        'InChlKey': property_table[5].xpath('./td/text()').get().strip(),
        'InChl': property_table[6].xpath('./td/text()').get().strip(),
        'SMILES': property_table[7].xpath('./td/text()').get().strip(),
        'Family': organism[1].strip(),
        'Species': organism[2].strip()
      }