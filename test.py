import unittest
import os, json
from os.path import join, dirname
from dotenv import load_dotenv
from r1_strg_sdk import R1StrgSDK

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class TestSum(unittest.TestCase):
    my = R1StrgSDK(endpoint_url=os.environ.get("endpoint_url"),
                   access_key=os.environ.get("access_key"),
                   secret_key=os.environ.get("secret_key"))

    def test_upload(self):
        result = self.my.put(bucket_name="mtbr-test", path="./LICENSE.txt", name="LICENSE.txt")
        result = json.loads(result)
        self.assertEqual('ok', result['status'])

    # def test_download_item(self):
    #     result = self.my.get(bucket_name="mtbr-test", download_path="./", name="LICENSE2.txt")
    #     print(result)

    def test_delete(self):
        result = json.loads(self.my.delete(bucket_name="mtbr-test", name="LICENSE.txt"))
        self.assertEqual('ok', result['status'])

    def test_list_buckest(self):
        result = json.loads(self.my.list_buckets())
        self.assertEqual('motabare', result[0]['name'])


if __name__ == '__main__':
    unittest.main()
