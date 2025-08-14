import pytest
from todo_list.todo_core import add_task, remove_task as core_add_task, core_remove_task

task_of_test1 = "Ir para academia!" # Variable to modify
task_of_test2 = "Ler jornal"

def test_add_task_success():
    tasks = []
    result = core_add_task(tasks, task_of_test1)
    assert task_of_test1 in result # If added in result -> Alright
    
def test_add_task_empty_raises():
    tasks = []
    with pytest.raises(ValueError):
        add_task(tasks, " ")
        
def test_remove_task_success():
    tasks = [task_of_test1, task_of_test2]
    result = core_remove_task(tasks, 0) # Remove task_of_test1
    assert task_of_test1 not in result # Verify if not in result
    assert len(result) == 1 # Verify if in result have only 1 object
    
def test_remove_task_invalid_index():
    tasks = [task_of_test1, task_of_test2]
    with pytest.raises(IndexError):
        core_remove_task(tasks, 2) # 0 until 1, not 2