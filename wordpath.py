#!/usr/bin/env python
import argparse
from wordpath.wp_engine import WordPath
import logging
from logging.config import fileConfig
import sys
sys.setrecursionlimit(50000)

def main(args):
    logger = logging.getLogger()
    logger.setLevel(args.log_level)
    logging.debug("started")

    logger.debug('Input file is: '+args.file.name)
    logger.debug('Start word is: '+args.start_word)
    logger.debug('End word is: '+args.end_word)

    w_processor = WordPath(args.file.name, args.start_word, args.end_word)
    path = w_processor.process()
    logging.debug("Process finished")

    if not path:
        print "NO PATH FOUND"
    else:
        result=""
        for item in path[:-1]:
            result += item+" -> "
        result += path[-1]
        print result

if __name__ == "__main__":
    logging.config.fileConfig("wordpath/log.conf")
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start_word", type=str, required=True)
    parser.add_argument("-e", "--end_word", type=str, required=True)
    parser.add_argument("-f", "--file", type=file, required=True)
    parser.add_argument('-d', '--debug', action='store_const', dest='log_level', const=logging.DEBUG, default=logging.INFO)
    args = parser.parse_args()
    main(args)
