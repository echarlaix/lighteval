# ruff: noqa: F405, F403, F401
"""
Custom evaluation tasks for lighteval. Copy this file and complete it with the info for your task.

This file generally create just a TASKS_TABLE and TASKS_GROUPS which are then imported by LightEval.

Author:
"""
from lighteval.tasks.lighteval_task import LightevalTaskConfig
from lighteval.tasks.requests import Doc
from lighteval.tasks.tasks_prompt_formatting import LETTER_INDICES


## EVAL WITH NO SUBSET ##
# This is how you create a simple tasks (like hellaswag) which has one single subset
# attached to it, and one evaluation possible.
task = LightevalTaskConfig(
    name="myothertask",
    prompt_function="prompt_fn",  # must be defined in the file or imported from src/lighteval/tasks/tasks_prompt_formatting.py
    suite=["community"],
    hf_repo="",
    hf_subset="default",
    hf_avail_splits=[],
    evaluation_splits=[],
    few_shots_split="",
    few_shots_select="",
    metric=[""],
)

## EVALS WITH SUBSET
# This is how you create a subset task (like MMLU), which has several subset
# each being its own evaluation task.

# fmt: off
SAMPLE_SUBSETS = [] # list of all the subsets to use for this eval
# fmt: on


class CustomSubsetTask(LightevalTaskConfig):
    def __init__(
        self,
        name,
        hf_subset,
    ):
        super().__init__(
            name=name,
            hf_subset=hf_subset,
            prompt_function="prompt_fn",  # must be defined in the file
            hf_repo="",
            metric=[""],
            hf_avail_splits=[],
            evaluation_splits=[],
            few_shots_split="",
            few_shots_select="",
            suite=["community"],
            generation_size=-1,
            stop_sequence=None,
            output_regex=None,
            frozen=False,
        )


## DEFINE YOUR PROMPT FUNCTIONS
# Define as many as you need for your different tasks
def prompt_fn(line, task_name: str = None):
    """Defines how to go from a dataset line to a doc object.
    Follow examples in src/lighteval/tasks/tasks_prompt_formatting.py, or get more info
    about what this function should do in the README.
    """
    return Doc(
        task_name=task_name,
        query="",
        choices="",
        gold_index=0,
        instruction="",
    )


## STORE YOUR EVALS
SUBSET_TASKS = [CustomSubsetTask(name=f"mytask:{subset}", hf_subset=subset) for subset in SAMPLE_SUBSETS]
_TASKS = SUBSET_TASKS + [task]

## MODULE LOGIC
# You should not need to touch this
# Convert to dict for lighteval
TASKS_TABLE = [task.as_dict() for task in _TASKS]

if __name__ == "__main__":
    print(t["name"] for t in TASKS_TABLE)
    print(len(TASKS_TABLE))
