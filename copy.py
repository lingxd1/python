import os
import shutil

def copy_mp3_files(src_dir, dest_dir):
    # 遍历源目录下的所有文件和子目录
    for filename in os.listdir(src_dir):
        # 构造文件的完整路径
        filepath = os.path.join(src_dir, filename)
        # 如果是目录，则递归调用函数
        if os.path.isdir(filepath):
            copy_mp3_files(filepath, dest_dir)
        # 如果是 mp3 文件，则拷贝到目标目录
        elif os.path.isfile(filepath) and os.path.splitext(filename)[1] == '.mp3':
            shutil.copy2(filepath, dest_dir)

copy_mp3_files(r'E:\BaiduNetdiskDownload\2023【抖音热歌】', r'G:\\')
