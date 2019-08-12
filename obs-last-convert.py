from os import listdir, makedirs
from os.path import isfile, join, exists
from sys import argv
from pprint import pprint as pp
from pprint import pformat
from time import time
from subprocess import run, PIPE
from traceback import print_exc
import platform


if not exists('./logs'):
    makedirs('./logs')

logfile = open("./logs/"+str(time())+".log",'w')

def log(msg):
    logfile.write(msg+"\n")

def usage():
    return "Usage: obs-last-convert.py <path to OBS clips directory>"

def main():
    try:
        files = [f for f in listdir(argv[1]) if isfile(join(argv[1], f)) and f.endswith("flv")]
        last = sorted(files, reverse=True)[0]
        log("Converting "+last)
        ffmpeg_cmd = "ffmpeg"
        if platform.system() == "Windows":
            ffmpeg_cmd = "./ffmpeg/bin/ffmpeg"
        result = run([ffmpeg_cmd,"-y","-i",argv[1]+"/"+last, argv[1]+"/last."+argv[2]],
            stdout=PIPE,
            stderr=PIPE
            )
        log(pformat(result))
    except Exception as e:
        log("Error: \n")
        print_exc(file=logfile)
        raise e



def cleanup():
    logfile.close()

def cleanup_and_exit():
    cleanup()
    exit()

if __name__ == '__main__':
    if len(argv) != 3:
        print("\n"+usage()+"\n")
        log("Invalid Usage: "+usage())
        cleanup_and_exit()

    main()
    cleanup()
