import importlib.util
import sys
import re
import traceback
import os

failing_tests = []
passing_tests = []

file_pattern = re.compile(r"^test_.+[.]py$")
method_pattern = re.compile(r"^test_.+|^test$")

wd = os.getcwd()

files = os.listdir(os.path.abspath(os.path.join(__file__, os.pardir)))
for file in files:
    if file_pattern.match(file):
        try:
            spec = importlib.util.spec_from_file_location(
                file[:-3], os.path.abspath(os.path.join(__file__, os.pardir, file)))
            foo = importlib.util.module_from_spec(spec)
            sys.modules[file[:-3]] = foo
            spec.loader.exec_module(foo)
            attrs = dir(foo)
            for attr in attrs:
                if method_pattern.match(attr):
                    print("-----")
                    print(f"{file}/{attr}")
                    try:
                        getattr(foo, attr)()
                        passing_tests.append(attr)
                        print("PASS")
                    except Exception as e:
                        print("FAIL")
                        traceback.print_exc()
                        failing_tests.append(f"{file}/{attr}")
                    finally:
                        print("-----")
        except Exception as e:
            print("-----")
            print(f"{file}/*")
            print("FAIL - UNABLE TO WORK WITH FILE")
            traceback.print_exc()
            print("-----")
            failing_tests.append(f"{file}/*")
        finally:
            # in case a test changed the WD, change it back
            os.chdir(wd)

print("-----")
print(f"PASSED: {len(passing_tests)}")
print(f"FAILED: {len(failing_tests)}")
print("-----")
if len(failing_tests) != 0:
    print(f"TESTS FAILING:")
    for failing_test in failing_tests:
        print(f"- {failing_test}")
    exit(1)
exit(0)
