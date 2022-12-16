import unittest
from task4.task4 import TaskManager


class TestTaskManager(unittest.TestCase):
    def test_add_delete(self):
        manager = TaskManager()
        task = manager.create_task('Go to them gym', 'Pump musclues')
        manager.remove_task_by_id(task.get_id())
        result = manager.get_tasks_by_id(task.get_id())
        self.assertEqual(result, None)

    def test_add_status_complex(self):
        manager = TaskManager()
        big_task = manager.create_complex_task("do hw", "description")
        subtask1 = manager.create_subtask(big_task, "open copybook", "smth")
        subtask2 = manager.create_subtask(big_task, "write in date", "today is ...")
        stat1 = manager.update_status(big_task)
        self.assertEqual(stat1.value,1)
        manager.update_status(subtask1)
        manager.update_status(subtask2)
        stat2 = manager.update_status(big_task)
        self.assertEqual(stat2.value,2)
        manager.update_status(subtask1)
        self.assertEqual(subtask1.status.value, 3)
        manager.update_status(subtask2)
        stat3 = manager.update_status(big_task)
        self.assertEqual(stat3.value, 3)

    def test_add_delete_subtasks(self):
        manager = TaskManager()
        big_task = manager.create_complex_task("do hw", "description")
        subtask1 = manager.create_subtask(big_task, "open copybook", "smth")
        subtask2 = manager.create_subtask(big_task, "write in date", "today is ...")
        sub1_id = subtask1.get_id()
        manager.remove_subtask_by_id(sub1_id)
        self.assertEqual(len(big_task.subtasks), 1)
        big_id = big_task.get_id()
        manager.remove_complex_task_by_id(big_id)
        self.assertEqual(len(manager.subtasks), 0)
        self.assertEqual(len(manager.complex_tasks), 0)



if __name__ == '__main__':
    unittest.main()
