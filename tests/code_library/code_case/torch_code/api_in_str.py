import torch

torch.add

_LOCAL_PROCESS_GROUP = None
_MISSING_LOCAL_PG_ERROR = (
    "Local process group is not yet created! Please use detectron2's `launch()` "
    "to start processes and initialize pytorch process group. If you need to start "
    "processes in other ways, please call comm.create_local_process_group("
    "num_workers_per_machine) after calling torch.distributed.init_process_group()."
)

_MISSING_LOCAL_PG_ERROR = (
    'Local process group is not yet created! Please use detectron2 launch() '
    'to start processes and initialize pytorch process group. If you need to start '
    'processes in other ways, please call comm.create_local_process_group('
    'num_workers_per_machine) after calling torch.distributed.init_process_group().'
)

_MISSING_LOCAL_PG_ERROR = (
    "Local process group is not yet created! Please use detectron2's `launch()` to start processes and initialize pytorch process group. If you need to start processes in other ways, please call comm.create_local_process_group(num_workers_per_machine) after calling torch.distributed.init_process_group()."
)

_MISSING_LOCAL_PG_ERROR = (
    'Local process group is not yet created! Please use detectron2 launch() to start processes and initialize pytorch process group. If you need to start processes in other ways, please call comm.create_local_process_group(num_workers_per_machine) after calling torch.distributed.init_process_group().'
)

_MISSING_LOCAL_PG_ERROR = """
"Local process group is not yet created! Please use detectron2's `launch()` "
"to start processes and initialize pytorch process group. If you need to start "
"processes in other ways, please call comm.create_local_process_group("
"num_workers_per_machine) after calling torch.distributed.init_process_group()."
"""

"""
"Local process group is not yet created! Please use detectron2's `launch()` "
"to start processes and initialize pytorch process group. If you need to start "
"processes in other ways, please call comm.create_local_process_group("
"num_workers_per_machine) after calling torch.distributed.init_process_group()."
"""

_MISSING_LOCAL_PG_ERROR = """
Local process group is not yet created! Please use detectron2's `launch()` 
to start processes and initialize pytorch process group. If you need to start 
processes in other ways, please call comm.create_local_process_group(
num_workers_per_machine) after calling torch.distributed.init_process_group().
"""

"""
Local process group is not yet created! Please use detectron2's `launch()` 
to start processes and initialize pytorch process group. If you need to start 
processes in other ways, please call comm.create_local_process_group(
num_workers_per_machine) after calling torch.distributed.init_process_group().
"""
