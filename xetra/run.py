"""
running the xetra etl app
"""

import  argparse
import  logging
import  logging.config
import  yaml

from  xetra.common.s3 import S3BucketConnector



def main():
    """
    entry point to run the xetra etl job
    """
    print("running beya")
    #parsing the YAML file
  #  config_path = "C:\\pythonprojects\\xetra_project\\xetra_1234\\configs\\xetra_report1_config.yml"
   # config = yaml.safe_load(open(config_path))
    #print(config)
    #configure logging

    parser = argparse.ArgumentParser(description='Run the Xetra ETL job')
    parser.add_argument('config',help='A config file in YAML format.')
    args = parser.parse_args()
    config = yaml.safe_load(open(args.config))


    log_config = config['logging']
   # print(type(log_config))
   # print(log_config)
   # for k,v in log_config.items():
   #     print(k,v)

    logging.config.dictConfig(log_config)
    logger= logging.getLogger(__name__)
    logger.info("tst bu beya")

    s3_config = config['s3']
    print(s3_config)

   # print(log_config)

 



if __name__ == '__main__':
    main()
