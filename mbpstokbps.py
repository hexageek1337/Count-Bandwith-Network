#! /usr/bin/python
import sys

try:
	print '''
 -----------------------------------------------------------
|                                    ( Mbps to kB/s )      |____
|      #     #  #####                                           |
|      #     # #     # #    #   ##    ####   ####  #    #       |
|      #     #       #  #  #   #  #  #    # #    # ##   #       |
|      #######  #####    ##   #    # #      #    # # #  #       |
|      #     #       #   ##   ###### #  ### #    # #  # #       |
|      #     # #     #  #  #  #    # #    # #    # #   ##       |
|      #     #  #####  #    # #    #  ####   ####  #    #       |
|                                                               |
|                            Powered by Cyber Merah Putih       |
|                                  ( Denny Septian )            |
|                                                               |
 ----------------------------------------------------------------'''
 	# Awal
 	triplezero = "000"
 	bandwith = str(raw_input("| Input your bandwith (example : 2) : "))
 	bandwith += str(triplezero)
 	kBps = int(bandwith) / int(8)

 	# print output
 	print("-----------------------------------------------------------------")
 	print("| Output : "+str(kBps)+" kB/s")
 	print("-----------------------------------------------------------------")
except KeyboardInterrupt:
	print("Exit now ...")
	sys.exit()