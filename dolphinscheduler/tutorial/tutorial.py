# -*- coding: utf-8 -*- 
# @Author : XuXu ClassMate
# @File : tutorial.py 
# username： xuxudemac
# @IDE: PyCharm
# @Time : 2022/4/9 17:40

# [start package_import]
# Import ProcessDefinition object to define your workflow attributes
from pydolphinscheduler.core.process_definition import ProcessDefinition

# Import task Shell object cause we would create some shell tasks later
from pydolphinscheduler.tasks.shell import Shell

# [end package_import]

# [start workflow_declare]
with ProcessDefinition(
        name="tutorial",
        schedule="0 0 0 * * ? *",
        start_time="2021-01-01",
        tenant="tenant_exists",
) as pd:
    # [end workflow_declare]
    # [start task_declare]
    task_parent = Shell(name="task_parent", command="echo hello pydolphinscheduler")
    task_child_one = Shell(name="task_child_one", command="echo 'child one'")
    task_child_two = Shell(name="task_child_two", command="echo 'child two'")
    task_union = Shell(name="task_union", command="echo union")
    # [end task_declare]

    # [start task_relation_declare]
    task_group = [task_child_one, task_child_two]
    task_parent.set_downstream(task_group)

    task_union << task_group
    # [end task_relation_declare]

    # [start submit_or_run]
    pd.run()
    # [end submit_or_run]
