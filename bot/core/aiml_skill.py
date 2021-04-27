import typing as t
import uuid
from pathlib import Path

import aiml
from loguru import logger


class AIMLSkill:
    def __init__(
        self,
        path_to_aiml_scripts: str,
        positive_confidence: float = 0.7,
        null_response: str = "I don't know what to answer you",
        null_confidence: float = 0.3
    ) -> None:
        self.path_to_aiml_scripts = Path(path_to_aiml_scripts).expanduser().resolve()

        self.positive_confidence = positive_confidence
        self.null_confidence = null_confidence
        self.null_response = null_response

        self.kernel = aiml.Kernel()
        self._load_scripts()
        logger.info("AIML KERNEL STARTED!")

    def _load_scripts(self) -> None:
        all_files = sorted(self.path_to_aiml_scripts.rglob('*.*'))
        learned_files = []

        for each_file_path in all_files:
            if each_file_path.suffix in ['.aiml', '.xml']:
                self.kernel.learn(str(each_file_path))
                learned_files.append(each_file_path)

        if not learned_files:
            logger.warning(f"No .aiml or .xml files found for AIML Kernel in directory {self.path_to_aiml_scripts}")

    def process_step(self, utterance_str: str, user_id: any) -> t.Tuple[str, float]:
        response = self.kernel.respond(utterance_str, sessionID=user_id)

        if response:
            confidence = self.positive_confidence
        else:
            response = self.null_response
            confidence = self.null_confidence

        return response, confidence

    @staticmethod
    def _generate_user_id() -> str:
        return uuid.uuid1().hex

    def __call__(
            self,
            utterances_batch: t.List[str],
            states_batch: t.Optional[t.List] = None
    ) -> t.Tuple[t.List[str], t.List[float], list]:
        output_states_batch = []
        user_ids = []

        if states_batch is None:
            states_batch = [None] * len(utterances_batch)

        for state in states_batch:
            if not state:
                user_id = self._generate_user_id()
                new_state = {'user_id': user_id}

            elif 'user_id' not in state:
                new_state = state
                user_id = self._generate_user_id()
                new_state['user_id'] = self._generate_user_id()

            else:
                new_state = state
                user_id = new_state['user_id']

            user_ids.append(user_id)
            output_states_batch.append(new_state)

        confident_responses = map(self.process_step, utterances_batch, user_ids)
        responses_batch, confidences_batch = zip(*confident_responses)

        return responses_batch, confidences_batch, output_states_batch
