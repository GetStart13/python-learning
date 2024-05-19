import logging


class SensitiveFilter(logging.Filter):
    def filter(self, record):
        # 为 True 时，信息才会被输出
        return record.getMessage().__contains__("sensitive")


class WarningFilter(logging.Filter):
    def filter(self, record):
        return record.getMessage().__contains__("warning")
