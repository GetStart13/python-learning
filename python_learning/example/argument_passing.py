import sys
import os


def main():
    print("命令行传入参数：`python -m argument_passing \"arguments\"`。sys:", sys.argv)
    print("=" * 100)
    # print("环境变量，os:", os.environ)
    print("环境变量 JAVA_HOME：", os.getenv("JAVA_HOME"))


if __name__ == '__main__':
    sys.exit(main())
