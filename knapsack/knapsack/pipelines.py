import json
from itemadapter import ItemAdapter

class KnapsackPipeline:
  # def open_spider(self, spider):
  #   self.file = open('output.json', 'w')
  
  # def close_spider(self, spider):
  #   self.file.close()

  def process_item(self, item, spider):
    # line = json.dumps(ItemAdapter(item).asdict()) + '\n'
    # self.file.write(line)
    return item