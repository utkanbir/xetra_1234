"""
Tests3bucketconnectormethods
"""

import os
import unittest
import boto3
from moto import mock_s3
from xetra.common.s3 import S3BucketConnector


class TestS3BucketConnectorMethods(unittest.TestCase):
    """
    Testing the S3BucketConnector class
    """

    def setUp(self):
        """
        setting up the environment
        """
        print("inside setup")
        # mocking s3 connectionstart  
        self.mock_s3 = mock_s3()
        self.mock_s3.start()
        
        #defining the class arguments
        self.s3_access_key='AWS_KEY'
        self.s3_secret_key= 'AWS_SECRET'
        self.s3_endpoint_url='https://s3.eu-central-1.amazonaws.com'
        self.s3_bucket_name='test-bucket'
        os.environ[self.s3_access_key] = 'KEY1'
        os.environ[self.s3_secret_key] = 'KEY22'
        #creating bucket  
        self.s3 = boto3.resource(service_name='s3',endpoint_url=self.s3_endpoint_url)
        self.s3.create_bucket(Bucket=self.s3_bucket_name,CreateBucketConfiguration= {
            'LocationConstraint' : 'eu-central-1'
        })
        self.s3_bucket= self.s3.Bucket(self.s3_bucket_name)
        #creating a testing instance
        self.s3_bucket_conn = S3BucketConnector(self.s3_access_key,self.s3_secret_key,self.s3_endpoint_url,self.s3_bucket_name)
        print("endofsetup")



    def tearDown(self):
        """
        executing after unittests
        """
        #mocking s3 connection stop 
        print("inside teardown")
        self.mock_s3.stop()


    def test_list_files_in_prefix_ok(self):
        """
        tests the list_files_in_prefix method
        """
        print("in testlist1")
        
        #Expected results
        prefix_exp = 'prefix/'
        key1_exp = f'{prefix_exp}test1.csv'
        key2_exp = f'{prefix_exp}test2.csv'
        #Test init
        csv_content = """col1,col2
        valA,valB"""
        self.s3_bucket.put_object(Body=csv_content,Key=key1_exp)
        self.s3_bucket.put_object(Body=csv_content,Key=key2_exp)
        
           
        #Method execution
        list_result = self.s3_bucket_conn.list_files_in_prefix(prefix_exp)

        
        #Tests after method execution
        self.assertEqual(len(list_result),2)
        self.assertIn(key1_exp,list_result)
        self.assertIn(key2_exp,list_result)
        
        #Cleanup after tests
        self.s3_bucket.delete_objects(
            Delete={
                'Objects':[
                    {
                        'Key' : key1_exp
                    },
                    {
                        'Key' : key2_exp
                    }
                ]
            }
        )


    def test_list_files_in_prefix_wrong_prefix(self):
        """
        test the ....
        """
        print("test2")


#print(f'main:{__name__}')    
if __name__ == "__main__":
    #print("in 1")
    unittest.main()
    #testInstance = TestS3BucketConnectorMethods()
    #testInstance.setUp()
    #testInstance.test_list_files_in_prefix_ok()



        


