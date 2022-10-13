"""
running the xetra etl app
"""

import  logging
import  logging.config
import  yaml


def main():
    """
    entry point to run the xetra etl job
    """
    print("running beya")
    #parsing the YAML file
    config_path = "C:\\pythonprojects\\xetra_project\\xetra_1234\\configs\\xetra_report1_config.yml"
    config = yaml.safe_load(open(config_path))
    #print(config)
    #configure logging
    log_config = config['logging']
   # print(type(log_config))
   # print(log_config)
   # for k,v in log_config.items():
   #     print(k,v)

    logging.config.dictConfig(log_config)
    logger= logging.getLogger(__name__)
    logger.info("tst bu beya")

   # print(log_config)

if __name__ == '__main__':
    main()
