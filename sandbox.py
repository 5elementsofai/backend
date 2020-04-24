import logging
import posixpath

from mlflow.models import Model
from mlflow.models.flavor_backend_registry import get_flavor_backend
from mlflow.tracking.artifact_utils import _download_artifact_from_uri
from mlflow.utils.file_utils import TempDir


model_uri = ""
with TempDir() as tmp:
    local_path = _download_artifact_from_uri(posixpath.join(model_uri, "MLmodel"), output_path=tmp.path())
    model = Model.load(local_path)
    flavor_name, flavor_backend = get_flavor_backend(model)
    