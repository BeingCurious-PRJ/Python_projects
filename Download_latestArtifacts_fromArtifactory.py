from pyartifactory import Artifactory
from artifactory import ArtifactoryPath
from datetime import date


def save_artifacts_to_local_folder(art_, repo_name, current_date):
    folder_info = art_.artifacts.info(repo_name)
    children_files = folder_info.children
    latest_file = children_files[len(children_files) - 1]
    latest_file_path = repo_name + latest_file.uri
    latest_file_info = art_.artifacts.info(latest_file_path)
    date_created = latest_file_info.created.date()
    if current_date == date_created:
        artifact_download = art.artifacts.download(latest_file_path, r'local folder path')


#  initialization and function calls
art = Artifactory(url="ARTIFACTORY PATH URL",
                  auth=('ARTIFACTORY USERNAME', 'PASSWORD'), api_version=1)
today_date = date.today()
repository_name1 = "my_python_projects-pypi-local"
# function call #any number of function calls for different repositories
save_artifacts_to_local_folder(art, repository_name1,
                               today_date)
