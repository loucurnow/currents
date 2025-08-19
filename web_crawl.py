import boto3

# Connect to the Common Crawl S3 bucket
s3 = boto3.client("s3")

bucket_name = "commoncrawl"

# List available files (objects) in the bucket
response = s3.list_objects_v2(Bucket=bucket_name, MaxKeys=10)  # Get 10 files

# Print file names
for obj in response.get("Contents", []):
    print(obj["Key"])


file_key = "crawl-data/CC-MAIN-2024-10/segments/1707254401255.34/warc/CC-MAIN-20240206165939-20240206195939-00000.warc.gz"
local_filename = "data.warc.gz"

s3.download_file(bucket_name, file_key, local_filename)
print(f"Downloaded {file_key} to {local_filename}")
