import os
import shutil


def rmdirs(top, deldirs):
    """
    删除指定目录下，部分子目录（可以嵌套在层次很深的子目录下）
    top: 根目录
    deldirs: 需要删除的目录列表
    """
    for root, dirs, files in os.walk(top, topdown=False):
        for name in dirs:
            if name in deldirs:
                print(root, "/", name)
                shutil.rmtree(os.path.join(root, name), ignore_errors=True)


def main():
    rmdirs(
        "/run/media/znw/Ventoy/刻盘/移动平台应用开发-2023计算机科学与及技术（专升本）2班-卓能文/7.实验报告资料/",
        [".git", ".idea", ".gradle", "build"],
    )


if __name__ == "__main__":
    main()
