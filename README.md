wordpath.py
-------------

The problem is to find "word paths". What this means is that you find a path from one word to
another word, changing one letter each step, and each intermediate word must be in the
dictionary provided to the tool.


TL;DR
-----

  run:
    $ python wordpath.py -s rial -e foud -f ./tests/words

  no path:
    $ python wordpath.py -s aaaa -e zzzz -f ./tests/words


Project Structure
-----------------

  /wordpath           : source code
  /tests : unit tests
  wordpath.py    : main file


Command Line Interface
----------------------

 usage:  wordpath.py -s START_WORD -e END_WORD -f FILE

 optional arguments:
   -h, --help   show this help message and exit
   -d, --debug  enable debug mode (default: disabled)

Testing
-------

  $ python -m unittest -v tests.testwordpath

    test_build_graph (tests.testwordpath.TestUtils) ... ok
    test_build_graph_file (tests.testwordpath.TestUtils) ... ok
    test_diff_1_letter (tests.testwordpath.TestUtils) ... ok
    test_find_children (tests.testwordpath.TestUtils) ... ok
    test_find_path (tests.testwordpath.TestUtils) ... ok
    test_read_words (tests.testwordpath.TestUtils) ... ok
    test_process_real_file1 (tests.testwordpath.TestWordPath) ... ok
    test_process_real_file2 (tests.testwordpath.TestWordPath) ... ok
    test_process_real_file3 (tests.testwordpath.TestWordPath) ... ok

    ----------------------------------------------------------------------
    Ran 9 tests in 114.365s

    OK

Python version
--------------

  It was implemented and teste using Python 2.7:
    Python 2.7.13 (default, Dec 18 2016, 07:03:39)

Author
------
 Volmar Oliveira Junior
 volmar.oliveira.jr@gmail.com