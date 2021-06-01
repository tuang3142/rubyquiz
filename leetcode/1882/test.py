import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.assignTasks = Solution().assignTasks

    def test_general(self):
        servers = [3,3,2]
        tasks = [1,2,3,2,1,2]
        self.assertEqual(self.assignTasks(servers, tasks), [2,2,0,2,1,2])

    def test_1_server(self):
        servers = [100]
        tasks = [1, 2, 3, 4, 5]
        self.assertEqual(self.assignTasks(servers, tasks), [0, 0, 0, 0, 0])

    def test_time_consuming_task(self):
        servers = [3, 3, 2]
        tasks = [10, 10, 10, 10, 10]
        self.assertEqual(self.assignTasks(servers, tasks), [2, 0, 1, 2, 0])


if __name__ == '__main__':
    unittest.main()
