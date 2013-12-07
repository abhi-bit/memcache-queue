from memqueue import MemQueue 
import sys, time
import memcache
from optparse import OptionParser

client = ['127.0.0.1:11211']
queue = MemQueue('benchmark', memcache.Client(client))

start = time.time()

if __name__ == '__main__':
    parser = OptionParser(usage="usage: %prog [options] filename",
        version="%prog 0.1")
    parser.add_option("-a", "--add", dest="add", default='notAdd', help="add keys to queue")
    parser.add_option("-r", "--read", dest="read", default='notRead', help="read from queue")
    parser.add_option("-c", "--count", dest="count", default='1000', type='int', help="no. of keys to read/add")
    (options, args) = parser.parse_args()

    add = options.add
    read = options.read
    count = options.count

    if add != 'notAdd':
        for index in xrange(count):
            queue.add('data %s' % index)
        print ('Added %d keys' % count)

    if read != 'notRead':
        for index in xrange(count):
            queue.get()
        print ('Read %s keys' % count)

    print ('Time elapsed: %s seconds' % (time.time() - start))
