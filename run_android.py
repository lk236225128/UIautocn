import pytest
import os

PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
)

if __name__=='__main__':
    # pytest.main(['-v','--maxfail=3','./tests/test_case/','--alluredir','/tmp/my_allure_results','--clean'])
    pytest.main(['-v','--maxfail=3','./tests/android_test_case/','--alluredir','/Users/kevin/Project/UIautocn/tmp/my_allure_results'])
