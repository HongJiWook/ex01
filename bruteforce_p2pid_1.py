# -*- encoding:utf-8 -*-

import sys
import os
import time

UPPER_ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DID_ALPHA_IDX = [0, 0, 0, 0, 0]

DID_FORMAT = "DEVUPUS-000029-"
INITSTRING_FORMAT = "EBGCFGBJKDJMGAJPECGEFGEJHMMJHHNOGDFFBJCKBGJOLDLBDNALCBOHGBLAJNLBAGMALHDDOAMHABCNJINBIEAO:devuplus19kn"
TEST_MODE = 0
PROGRAM_NAME = "ReadWriteTester64"

if __name__ == "__main__":
	MODE = TEST_MODE
	INITSTRING = INITSTRING_FORMAT
	
	start_time = time.time()
	while(True):
		for i in range(4, 0, -1):
			if DID_ALPHA_IDX[i] == 26:
				DID_ALPHA_IDX[i] = 0
				DID_ALPHA_IDX[i-1] += 1
		DID_ALPHA = "".join([UPPER_ALPHA[i] for i in DID_ALPHA_IDX])
		
		ret = os.system("./{} [} {} [}".format(PROGRAM_NAME, MODE, DID_FORMAT + DID_ALPHA, INITSTRING))
		
		DID_ALPHA_IDX[-1] += 1
		print("\n")
