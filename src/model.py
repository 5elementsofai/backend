from allennlp.predictors import Predictor
from allennlp.models.archival import load_archive

class Model:
    def __init__(self, archive_file: str, predictor_name: str, max_request_length: int,
                 overrides: str = "") -> None:
        self.archive_file = archive_file
        self.predictor_name = predictor_name
        self.max_request_length = max_request_length
        self.overrides = overrides

    def predictor(self) -> Predictor:
        archive = load_archive(self.archive_file, overrides=self.overrides)
        return Predictor.from_archive(archive, self.predictor_name)
