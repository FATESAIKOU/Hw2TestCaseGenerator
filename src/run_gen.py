#!/usr/bin/env python

import sys
import json

import factory
import q1fac, q2fac, q3fac

def main():
    q_name = sys.argv[1]
    q_ifile = sys.argv[2]
    q_ofile = sys.argv[3]
    
    q_cfg_src = open(sys.argv[4], 'r')
    q_cfg = json.loads(q_cfg_src.read())
    q_cfg_src.close()
    
    
    if q_name == 'q1':
        inputs, outputs = factory.makeTestCases(q1fac, q_cfg)
    elif q_name == 'q2':
        inputs, outputs = factory.makeTestCases(q2fac, q_cfg)
    elif q_name == 'q3':
        inputs, outputs = factory.makeTestCases(q3fac, q_cfg)
    else:
        print "<Black Man>???"
        return 1
    
    
    q_ifile_src = open(q_ifile, 'w')
    q_ifile_src.write('\n'.join([str(ip) for ip in inputs if ip != None]) + '\n')
    q_ifile_src.close()
    
    q_ofile_src = open(q_ofile, 'w')
    q_ofile_src.write('\n'.join([str(op) for op in outputs if op != None]) + '\n')
    q_ofile_src.close()


if __name__ == '__main__':
    main()
