from argparse import ArgumentParser
from logging import info
from os import mkdir
from queue import Queue
from shutil import rmtree
from time import time as now

from sounddevice import InputStream
from soundfile import SoundFile

parser = ArgumentParser()
parser.add_argument(
    '-s', '--split-after', type=int, default=30, help='split after this number of seconds')
args = parser.parse_args()


def make_temp_directory():
    try:
        mkdir('temp')
    except FileExistsError:
        info('Temp directory is already exists')


def setup():
    make_temp_directory()


def main():
    setup()

    queue = Queue()
    with InputStream(samplerate=44100, device=None,
                     channels=2, callback=lambda indata, frames, time, status: queue.put(indata.copy())):
        filename = 0
        while True:
            with SoundFile(f'temp/{str(filename)}.wav', mode='x', samplerate=44100,
                           channels=2) as file:
                start_time = now()
                while True:
                    if now() - start_time > args.split_after:
                        break
                    file.write(queue.get())
            filename += 1


if __name__ == '__main__':
    try:
        main()
    finally:
        rmtree('temp')
