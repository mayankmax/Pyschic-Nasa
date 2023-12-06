
from DataIngestion import Apod_ingestion
import sys

sys.path.insert(0,'/home/mayank/Desktop/Project/DE/NASA/DataIngestion')

result = Apod_ingestion.ApodIngestion();

print(result.get('explanation'))
print("Title " + result.get('title'))
print(result.get('url'))