import argparse
import logging

from ..common import ConfigObject, Colors, notify
from .genRandomArg import FuncTest, UnitTest

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Unit Tests')
    parser.add_argument('--project_path',
                        metavar='project_path',
                        default='',
                        type=str,
                        help='the path to Python project')
    parser.add_argument('--module_name',
                        metavar='module_name',
                        default='',
                        type=str,
                        help='the module for test generation')
    parser.add_argument('-r', '--path_runtime',
                        metavar='path_runtime',
                        type=str,
                        default="",
                        help='the path to code to exercise the tool')
    parser.add_argument('-t', '--timeout',
                        metavar='timeout',
                        type=int,
                        default=20,
                        help='user defined time limit for the program to run in seconds')
    parser.add_argument('-c', '--coverage',
                        metavar='target',
                        type=int,
                        default=80,
                        choices=range(1, 101),
                        help='target coverage for the generated tests in percentage')
    args = parser.parse_args()
    project_path = args.project_path
    module_name = args.module_name
    timeout = args.timeout
    coverage = args.coverage

    notify("project_path: " + project_path, Colors.ColorCode.cyan)
    notify("module_name: " + module_name, Colors.ColorCode.cyan)
    notify("timeout: " + str(timeout), Colors.ColorCode.cyan)
    notify("coverage_target: " + str(coverage), Colors.ColorCode.cyan)

    if project_path == '' or module_name == '':
        print("Please enter a valid project path / module name.")
        exit(-1)

    config = ConfigObject(project_path, module_name)

    try:
        config.read_from_config()
        for module_name, temp in config.config.items():
            if module_name == config.module_name:
                for class_name, val in temp.items():
                    for func_name, _ in val.items():
                        func = FuncTest(config,
                                        [module_name, class_name, func_name])
                        print('----------')
                        test_info = func.generate_random_test()
                        print(test_info)
                        test = UnitTest(test_info, config)
                        try:
                            test.run()
                        except Exception as e:
                            test.exception = e
                            print("Exception found in {}: ".format(func_name) + str(e))


    except Exception as e:
        logging.exception(e)