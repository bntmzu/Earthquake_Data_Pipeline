import asyncio
from src.api import gather_data
from src.aggregator import save_to_file
from src.gcs_uploader import upload_to_gcs
from src.config import FILE_NAME, BUCKET_NAME

async def main():
    data = await gather_data()
    save_to_file(data, FILE_NAME)
    upload_to_gcs(FILE_NAME, BUCKET_NAME)

if __name__ == "__main__":
    asyncio.run(main())
