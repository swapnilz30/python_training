#!/usr/bin/env python3


def arbitrary_fn(**args):
     for a in args.items():
         print (a)

     for key, value in args.items():
        print("%s == %s" % (key, value))

     print ("Convert to dictionay dict(args): ", dict(args))


arbitrary_fn(srno = 1, name = 'abc', state = 'Maharashtra')

