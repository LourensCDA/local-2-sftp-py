import logging
import pysftp
import os
from pathlib import Path

# this process will sync a local folder with an SFTP server
# no default location is assumed

# set logging level
default_level = "debug"
numeric_level = getattr(logging, default_level.upper(), None)
logging.basicConfig(level=numeric_level)

# set variables
local_folder = "path to local folder"

remote_host = "sftp host name"
remote_user = "sftp user name"
remote_pass = "sftp password"
remote_port = 22


# connect to SFTP
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

try:
    logging.info("Connecting to SFTP")
    with pysftp.Connection(
        host=remote_host,
        username=remote_user,
        password=remote_pass,
        port=remote_port,
        cnopts=cnopts,
    ) as sftp:
        logging.info("Connected to SFTP")

        # walk through files and subfolders in local_folder
        logging.info("Sync with SFTP")
        for folder, subfolders, files in os.walk(local_folder):
            if folder != local_folder:
                # check if folder exists on SFTP, if not create it
                logging.info(folder)
                if not sftp.exists(folder.replace(local_folder, "").replace("\\", "/")):
                    logging.info(
                        "Creating folder: "
                        + folder.replace(local_folder, "").replace("\\", "/")
                    )
                    sftp.mkdir(folder.replace(local_folder, "").replace("\\", "/"))

                # check if files exist on SFTP, if not upload them
                for f in os.listdir(folder):
                    if os.path.isfile(os.path.join(folder, f)):
                        if not sftp.exists(
                            folder.replace(local_folder, "").replace("\\", "/")
                            + f"/{f}"
                        ):
                            logging.info(f"Copying {f}")
                            if sftp.put(
                                os.path.join(folder, f),
                                folder.replace(local_folder, "").replace("\\", "/")
                                + f"/{f}",
                            ):
                                logging.info(f"Copied {f} to SFTP")


except Exception as e:
    logging.error("Error connecting to SFTP: " + str(e))
    exit()
