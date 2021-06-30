# arvancloud_storage_sdk

list = r1_strg_sdk.list_items(bucket_name='mtbr-test')
put = r1_strg_sdk.put(bucket_name='mtbr-test',path='/home/alirezajalili/Pictures/external-content.duckduckgo.com.jpeg', name='avatar.jpeg')

list_buckets = r1_strg_sdk.list_buckets()
print(list)
print(put)
print(upload(bucket_name='mtbr-test', path='/home/alirezajalili/Pictures/2305863_0.png', name="it--works2.png"))
print(list('mtbr-test'))
print(r1_strg_sdk.get(bucket_name='mtbr-test', name='avatar.jpeg',
download_path='/home/alirezajalili/test/'))
r1_strg_sdk.delete(bucket_name='mtbr-test', name='avatar.jpeg')