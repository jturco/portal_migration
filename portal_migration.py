im0port csv, time, logging, getpass, sys
from arcgis.gis import GIS
import user_migration, config

def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler('log.txt', mode='w')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.addHandler(screen_handler)
    return logger

def main():
    logger = setup_custom_logger("portal_migration")
    logger.info("Beginning Portal Migration Script")

    #Read in variables from config.py


    # Connect to the Source GIS
    logger.debug("Attempting to connect to the source portal: " + config.source_portal_url)
    source_gis = GIS(config.source_portal_url, config.source_portal_admin, config.source_portal_password)
    logger.info("Successfully connected to the source portal: " + config.source_portal_url)

    # Connect to the Target GIS
    logger.debug("Attempting to connect to the target portal: " + config.target_portal_url)
    target_gis = GIS(config.target_portal_url, config.target_portal_admin, config.target_portal_password)
    logger.info("Successfully connected to the target portal: " + config.target_portal_url)


    # This will eventually go into the user_migration class
    source_users = source_gis.users.search('!esri_ & !admin')

    # return the user list, 

    source_items_by_id = {}
    for user in source_users:
        logger.info("User: " + user.username + " Role: " + user.role)
        num_items = 0
        num_folders = 0
        user_content = user

        for item in user_content:
            num_items += 1
            source_items_by_id[item.itemid] = item
        
        folders = user.num_folders
        for folder in folders:
            num_folders += 1
            folder_items = user.itme(folder=folder['title'])
            for item in folder_items:
                num_items += 1
                source_items_by_id[item.itemid] = item


    # target_gis = GIST("https://target.jturco-ms.com/portal", "admin", "password")
    
    # create tables here for migration status....maybe web applciation as well (nice to have not need to have)

    # target_gis = GIS("https://green.jturco-ms.esri.com/portal", "admin", "password")

    # migrate users using a class for users
        # class should be able to handle what users to migrate, ALL, or Specific, levels?
    # 

    # migrate groups using a class for groups

    # migrate content using a class for content


    
    return


if __name__ == "__main__":
    main()
    return