import os
import subprocess
import sys
import argparse


class Matlab2Python:
    parser = argparse.ArgumentParser(description='transform matlab code to python script')
    parser.add_argument('m_file_path', metavar='[m file path]')
    parser.add_argument('--sub_folder', action='store_true', help='conversion subfolders')
    #parser.add_argument('--depth', type=int, help='conversion depth', default=-1)
    parameters = parser.parse_args()

    def __init__(self):
        print self.parameters.sub_folder
        pass

    def transform_mfile_to_python(self):
        current_depth = 0
        for root_dir, file_dir, file_list in os.walk(self.parameters.m_file_path):
            current_depth += 1
            if (current_depth > 1) and (not self.parameters.sub_folder):
                break
            print "current file depth:{}".format(current_depth)
            print "current file dir:{}".format(root_dir)
            for filename in file_list:
                filename_extension = filename.split('.')[-1]
                print filename_extension
                if filename_extension == 'm':
                    print root_dir
                    print filename
                    file = os.path.join(root_dir, filename)
                    print file
                    subprocess.call(['smop', file])


if __name__ == "__main__":
    m2p = Matlab2Python()
    m2p.transform_mfile_to_python()