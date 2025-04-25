from google.cloud import storage

def upload_to_gcs(filename: str, bucket_name: str):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    print(f"Uploaded {filename} to gs://{bucket_name}/{filename}")
