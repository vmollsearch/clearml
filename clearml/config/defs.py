import tempfile

from ..backend_config import EnvEntry
from ..backend_config.converters import base64_to_text, or_
from pathlib2 import Path

SESSION_CACHE_FILE = ".session.json"
DEFAULT_CACHE_DIR = str(Path(tempfile.gettempdir()) / "trains_cache")

TASK_ID_ENV_VAR = EnvEntry("TRAINS_TASK_ID", "ALG_TASK_ID")
DOCKER_IMAGE_ENV_VAR = EnvEntry("TRAINS_DOCKER_IMAGE", "ALG_DOCKER_IMAGE")
LOG_TO_BACKEND_ENV_VAR = EnvEntry("TRAINS_LOG_TASK_TO_BACKEND", "ALG_LOG_TASK_TO_BACKEND", type=bool)
NODE_ID_ENV_VAR = EnvEntry("TRAINS_NODE_ID", "ALG_NODE_ID", type=int)
PROC_MASTER_ID_ENV_VAR = EnvEntry("TRAINS_PROC_MASTER_ID", "ALG_PROC_MASTER_ID", type=str)
LOG_STDERR_REDIRECT_LEVEL = EnvEntry("TRAINS_LOG_STDERR_REDIRECT_LEVEL", "ALG_LOG_STDERR_REDIRECT_LEVEL")
DEV_WORKER_NAME = EnvEntry("TRAINS_WORKER_NAME", "ALG_WORKER_NAME")
DEV_TASK_NO_REUSE = EnvEntry("TRAINS_TASK_NO_REUSE", "ALG_TASK_NO_REUSE", type=bool)
TASK_LOG_ENVIRONMENT = EnvEntry("TRAINS_LOG_ENVIRONMENT", "ALG_LOG_ENVIRONMENT", type=str)
TRAINS_CACHE_DIR = EnvEntry("TRAINS_CACHE_DIR", "ALG_CACHE_DIR")

LOG_LEVEL_ENV_VAR = EnvEntry("TRAINS_LOG_LEVEL", "ALG_LOG_LEVEL", converter=or_(int, str))

SUPPRESS_UPDATE_MESSAGE_ENV_VAR = EnvEntry("TRAINS_SUPPRESS_UPDATE_MESSAGE", "ALG_SUPPRESS_UPDATE_MESSAGE", type=bool)

# Repository detection
VCS_REPO_TYPE = EnvEntry("TRAINS_VCS_REPO_TYPE", "ALG_VCS_REPO_TYPE", default="git")
VCS_REPOSITORY_URL = EnvEntry("TRAINS_VCS_REPO_URL", "ALG_VCS_REPO_URL")
VCS_COMMIT_ID = EnvEntry("TRAINS_VCS_COMMIT_ID", "ALG_VCS_COMMIT_ID")
VCS_BRANCH = EnvEntry("TRAINS_VCS_BRANCH", "ALG_VCS_BRANCH")
VCS_ROOT = EnvEntry("TRAINS_VCS_ROOT", "ALG_VCS_ROOT")
VCS_STATUS = EnvEntry("TRAINS_VCS_STATUS", "ALG_VCS_STATUS", converter=base64_to_text)
VCS_DIFF = EnvEntry("TRAINS_VCS_DIFF", "ALG_VCS_DIFF", converter=base64_to_text)