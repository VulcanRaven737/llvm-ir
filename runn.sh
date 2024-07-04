#!/bin/bash
guile /home/vulcan/llama.lisp/src/backend/utils/sexp-json.scm < /home/vulcan/ssh-trial/fibonacci.sexp | python /home/vulcan/llama.lisp/src/backend/brilisp.py | python /home/vulcan/llama.lisp/src/backend/llvm.py > out.ll
clang out.ll runtime.c
./a.out
