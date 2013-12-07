memcache-queue
==============

Using memcache as queue

Benchmark
==============

On a VM running on 2.4GHz CPU, 4G RAM

$ python benchmark.py -a add -c 10000 -r read
Added 10000 keys
Read 10000 keys
Time elapsed: 4.97572588921 seconds

