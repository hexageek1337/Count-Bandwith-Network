#! /usr/bin/python
import sys

try:
	print '''
 -----------------------------------------------------------
|                                    ( kB/s to Mbps )      |____
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
 	speed_download = int(raw_input("| Input your bandwith (example : 230 kBps) : "))
 	Mbps = int(speed_download) * int(8)

 	# print output
 	print("-----------------------------------------------------------------")
 	print("| Output : "+str(Mbps)+" kB")
 	print("-----------------------------------------------------------------")
except KeyboardInterrupt:
	print("Exit now ...")
	sys.exit()