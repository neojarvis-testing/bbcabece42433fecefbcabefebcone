rm -f /home/coder/project/workspace/pytest-selenium/test/*;
cp /home/coder/project/workspace/pytest-test/tests/* /home/coder/project/workspace/pytest-selenium/test;
cd /home/coder/project/workspace/pytest-selenium/test;
pytest-3 --verbose test.py

