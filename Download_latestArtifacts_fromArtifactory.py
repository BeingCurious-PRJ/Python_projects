from pyartifactory import Artifactory
from artifactory import ArtifactoryPath
from datetime import date
import os, re, sys


def save_artifacts_to_local_folder(art_, repo_name, current_date, local_folder_path):
    folder_info = art_.artifacts.info(repo_name)
    children_files = folder_info.children
    latest_file = children_files[len(children_files) - 1]
    latest_file_path = repo_name + latest_file.uri
    latest_file_info = art_.artifacts.info(latest_file_path)
    date_created = latest_file_info.created.date()
    if current_date == date_created:
        artifact_download = art.artifacts.download(latest_file_path, local_folder_path )
        [head_part,tail_part] = os.path.split(artifact_download) # to remove the frontslash'/' in downloaded local path
        artifact_localpath = os.path.join(head_part, tail_part)
        return artifact_localpath


#  initialization and function calls
art = Artifactory(url="ARTIFACTORY PATH URL",
                  auth=('ARTIFACTORY USERNAME', 'PASSWORD'), api_version=2) # api version could be 1 or 2..better use 2 to be compatible
today_date = date.today()
local_folderpath = r'local folder path'
repository_name1 = "my_python_projects-pypi-local" #repo name in jfrog artifactory where the files are to be downloaded from
# function call #any number of function calls for different repositories
artifact_downloaded_path = save_artifacts_to_local_folder(art, repository_name1,
                               today_date,local_folderpath)
