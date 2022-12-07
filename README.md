# gym_pad_testing
TMS_diploma_project

test run sequence:
1) pytest -v -m registration --reruns 2 --alluredir reports
2) pytest -v -m login --reruns 2 --alluredir reports
3) pytest -v -m home --reruns 3 --alluredir reports
4) pytest -v -m exercises --reruns 2 --alluredir reports
5) pytest -v -m nutrition --reruns 2 --alluredir reports
6) pytest -v -m body_parameters --reruns 2 --alluredir reports
7) pytest -v -m notes --reruns 2 --alluredir reports
8) pytest -v -m profile_settings --reruns 2 --alluredir reports
9) pytest -v -m change_existing_password --reruns 2 --alluredir reports
10) pytest -v -m enter_with_a_new_password --reruns 2 --alluredir reports
11) pytest -v -m logout --reruns 2 --alluredir reports
12) allure serve reports