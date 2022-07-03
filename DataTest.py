## -- Interpreter Mode -- ##

import pandas as pd
import h5py
import numpy as np

## Sampel Data TCP ##
# Normal #
tcp_a = pd.read_csv("dataset/sample-tcp-nping-noopt.csv",delimiter=",")
# Intrusion #
tcp_b = pd.read_csv("dataset/sample-tcp-thcsyn6-ack.csv",delimiter=",")[0:250]
tcp_c = pd.read_csv("dataset/sample-tcp-thcsyn6-hopbyhop.csv",delimiter=",")[0:250]
tcp_d = pd.read_csv("dataset/sample-tcp-thcsyn6-noopt.csv",delimiter=",")[0:250]
tcp_e = pd.read_csv("dataset/sample-tcp-thcsyn6-synack.csv",delimiter=",")[0:250]

## Sampel Data ICMPv6 ##
# Normal #
icmpv6_a = pd.read_csv("dataset/sample-icmpv6-fping-noopt.csv",delimiter=",")
# Intrusion #
icmpv6_b = pd.read_csv("dataset/sample-icmpv6-rsmurf6-noopt.csv",delimiter=",")[0:250]
icmpv6_c = pd.read_csv("dataset/sample-icmpv6-denial6-testcase1.csv",delimiter=",")[0:250]
icmpv6_d = pd.read_csv("dataset/sample-icmpv6-denial6-testcase2.csv",delimiter=",")[0:250]
icmpv6_e = pd.read_csv("dataset/sample-icmpv6-flood_unreach6-fragment.csv",delimiter=",")[0:250]

## Create HDF5 File ##
file = h5py.File("Intrusion_Sample_IPv6.hdf5","w")
# Clear Contents #
file.clear()
## Create Main Group - Protocol ##
main_group1 = file.create_group("Normal")
main_group2 = file.create_group("Intrusion")
## Create Direct Sub Group for Each Dataset ##
# TCP #
sub_group1 = main_group1.create_group("TCP/TCP_Normal")
sub_group2 = main_group2.create_group("TCP/TCP_Intrusion1")
sub_group3 = main_group2.create_group("TCP/TCP_Intrusion2")
sub_group4 = main_group2.create_group("TCP/TCP_Intrusion3")
sub_group5 = main_group2.create_group("TCP/TCP_Intrusion4")
# ICMPv6 #
sub_group6 = main_group1.create_group("ICMPv6/ICMPv6_Normal")
sub_group7 = main_group2.create_group("ICMPv6/ICMPv6_Intrusion1")
sub_group8 = main_group2.create_group("ICMPv6/ICMPv6_Intrusion2")
sub_group9 = main_group2.create_group("ICMPv6/ICMPv6_Intrusion3")
sub_group10 = main_group2.create_group("ICMPv6/ICMPv6_Intrusion4")
## Create and Insert Dataset ##
# TCP - Source,Destination,Protocol,Length,Payload Length,Window,Flags,Detection #
# SG 1 #
sub_group1.create_dataset("Source",data=tcp_a[["Source"]].to_numpy())
sub_group1.create_dataset("Destination",data=tcp_a[["Destination"]].to_numpy())
sub_group1.create_dataset("Protocol",data=tcp_a[["Protocol"]].to_numpy())
sub_group1.create_dataset("Length",data=tcp_a[["Length"]].to_numpy())
sub_group1.create_dataset("Payload Length",data=tcp_a[["Payload Length"]].to_numpy())
sub_group1.create_dataset("Window",data=tcp_a[["Window"]].to_numpy())
sub_group1.create_dataset("Flags",data=tcp_a[["Flags"]].to_numpy())
sub_group1.create_dataset("Detection",data=tcp_a[["Detection"]].to_numpy())
# ICMPv6 - Source,Destination,Protocol,Length,Payload Length,Type,Data,Detection #