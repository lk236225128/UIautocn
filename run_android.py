import pytest
import os
import subprocess
import time

PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
)

def kill_adb():
    os.popen("killall adb")
    os.system("adb start-server")

if __name__=='__main__':
    cmd = "appium --session-override -p 4700 -bp 4701 -U emulator-5554"
    subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1,close_fds=True)
    time.sleep(10)
    pytest.main(['-v','--maxfail=3','./tests/android_test_case/test_android_ad.py','--html=./report/html/report.html'])