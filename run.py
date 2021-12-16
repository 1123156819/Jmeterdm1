import os

import pytest

from common.Allure_Report import allure_generate
from config import Conf

if __name__ == '__main__':
    report_path = Conf.get_report_path() + os.sep + "result"
    report_html_path = Conf.get_report_path() + os.sep + "html"

    pytest.main(["-s"])

    allure_generate(report_path, report_html_path)