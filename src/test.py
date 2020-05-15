from app import delete_task, add_one_task, get_todos, save_todos, load_todos, initialize_todos
import unittest, csv

class TestStringMethods(unittest.TestCase):

    def tearDownClass():
        print("\n\n \033[43m WARNING: The methods save_todos, load_todos and initialize_todos don't have automatic grading \033[0m")

    def test_a_initialize(self):
        self.assertEqual(len(get_todos()), 0, 'The todo list needs to start with cero todos')

    def test_b_add(self):
        add_one_task("Make the bed")
        add_one_task("Make lunch")
        add_one_task("Clean kitchen")
        self.assertEqual(len(get_todos()), 3, 'After adding three tasks, the todo list length must be three')

    def test_c_delete(self):
        delete_task(2)
        self.assertEqual(len(get_todos()), 2, 'After deleting one tasks, the todo list length must be two')
        self.assertEqual(get_todos()[0], "Make the bed", 'After deleting position 2 the first position must still be Make the bed')
        self.assertEqual(get_todos()[1], "Clean kitchen", 'After deleting position 2 the second position must be now Clean kitchen')
    
if __name__ == '__main__':
    unittest.main()