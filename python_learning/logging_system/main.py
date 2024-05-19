import logging

from python_learning.logging_system.config import logging_config_setup

"""日志配置逻辑关系图：
[ Logger ] (父级)
    |-------[ Logger ] 
    |           |
    |           |----[ Handler ]--->[ Formatter ]
    |           |
    |           |----[ Handler ]--->[ Formatter ]
    |                   |
    |                   |--[ Filter ]
    |
    |-------[ Logger ] 
                |
                |----[ Handler ]--->[ Formatter ]

[ Logger ] (root logger)
    |
    |----[ Handler ]--->[ Formatter ]
"""
# ---------------------------------------------------------------------------------- #
"""日志记录流程图：
                                                                                                                    
                                                                        ┌──────────────────────────────────────────┐
  Logger flow                                                           │ Handler flow                             │
                               │                                        │                │                         │
                               │                                        │                │                         │
                               ▼                                        │                │                         │
                      [User get a Logger]                               │                ▼                         │
                      (e.g. logger =                                    │    [LogRecord passed to handler]         │
                         logging.getLogger(<LoggerName>))               │                │                         │
                               │                                        │                │                         │
                               │                                        │                ▼                         │
                               ▼                                        │    <Handler enabled for        No        │
                      [Logging call in user code]                       │         level of call?> ─────────►(stop) │
                      (e.g. logger.info(...))                           │                │                    ▲    │
                               │                                        │                │ Yes                │    │
                               │                                        │                ▼                    │    │
                               ▼                            No          │    <Does a filter attached to    Yes│    │
                      <Logger enabled for level of call?> ─────┐        │       logger reject the record?> ───┘    │
                               │                               │        │                │                         │
                               │ Yes                           │        │                │ No                      │
                               ▼                               ▼        │                ▼                         │
                      [Create LogRecord]                     (stop)     │    (Emit (includes formatting))          │
                               │                               ▲        │                                          │
                               │                               │        └──────────────────────────────────────────┘
                               ▼                               │                             ▲                      
                      <Does a filter attached to logger    Yes │                             │                      
                                      reject the record?> ─────┤                             │                      
                               │                               │                             │                      
                               │ No                            │                             │                      
                               ▼                               │                             │                      
      ┌─────────────► [Pass to handlers of current logger]─ ─ ─┼ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘                      
      │                        │                               │                                                    
      │                        │                               │                                                    
      │                        ▼                               │                                                    
[Set current logger   <Is propagate true for current       No  │                                                    
          to parent]                             logger?> ─────┤                                                    
      ▲                        │                               │                                                    
      │                        │ Yes                           │                                                    
      │         Yes            ▼                           No  │                                                    
      └────────────── <Is there a parent logger?>         ─────┘                                                    
                                                                                                                                                        
"""

logging_config_setup.setup_logging()

logger_inherit = logging.getLogger("base_logger.child")
logger_level_match = logging.getLogger(__name__)

"""
    注意！日志模块会自动创建需要生成的日志文件，但并不会自动创建文件夹。
    指定的日志文件的生成位置，要确保它的路径确实存在。
    这其实很好，因为我也不想我的电脑里莫名其妙多出一些莫名其妙的文件夹。
"""


def test():
    logger_inherit.warning("警告信息（warning）在控制台和 info 文件中将出现 2 次")

    logger_level_match.debug("日志级别指能处理的最低级别，记录器和处理器会处理高于或等于其设置级别的日志信息")
    logger_level_match.info("INFO 级别的信息高于 DEBUG，低于 WARN，因此 WARN 级别的 handler 和 logger 不会处理 INFO 信息")

    try:
        raise Exception("这是故意抛出的异常，用于测试过滤器。")
    except Exception as e:
        # 带“sensitive”字符串的信息能够被输出
        logger_level_match.critical('This is sensitive message.', exc_info=e)
        logger_level_match.critical('This is usual message.', exc_info=e)
        logger_inherit.warning(
            "警告信息没有出现，因为父级记录器的过滤器不会作用于子级记录器，即使正确匹配过滤器关键字（sensitive）")


if __name__ == '__main__':
    test()
