# Arvancloud Storage SDK
## a simple python package to work with Arvanlocud Object Storage.


i really did nothig. just make it classy :) i mean add all functions from [ArvanCloud Python Doc](https://npanel.arvancloud.com/storage/docs/python) to a `R1StrgSDK` class and add some usefull responses to it. just it.
but fell free to contact me if you need any change to package.


## Usage
### install the package.
```sh
pip install r1-strg-sdk
```
### import it.
```python
from r1_strg_sdk import R1StrgSDK
```

### Config 
```python
r1storage = R1StrgSDK(
    endpoint_url="Your EndPoint URL",
    access_key="Your Access Key",
    secret_key="Your Secret Key")
```
#### ! default value for all public pramets are `True`.

## working  with Buckets:
#### Create Bucket:
```python
result = r1storage.create_bucket(bucket_name="Your Bucket name",public=False)
```
#### delete Bucket:
```python
result = r1storage.delete_bucket("Your Bucket name")
```
#### Listing Buckets:
```python
result = r1storage.list_buckets()
```

## working  with Files of a Bucket:
#### Upload a File:
```python
result = r1storage.upload(
    bucket_name="the bucket you want work with it",
    path="path of file with exact name and extension",
    name="name of file")
```
#### Download a File:
```python
result = r1storage.download(
    bucket_name="the bucket you want work with it",
    name="name of file with extension",
    download_path="dir for downloading file")
```
#### Delete a File:
```python
result = r1storage.delete(
    bucket_name="the bucket you want work with it",
    name="name of file")
```
#### List Files of a Bucket:
```python
result = r1storage.list_items(bucket_name="the bucket you want work with it")
```


## License
MIT

