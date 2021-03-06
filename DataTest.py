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
# SG 2 #
sub_group2.create_dataset("Source",data=tcp_b[["Source"]].to_numpy())
sub_group2.create_dataset("Destination",data=tcp_b[["Destination"]].to_numpy())
sub_group2.create_dataset("Protocol",data=tcp_b[["Protocol"]].to_numpy())
sub_group2.create_dataset("Length",data=tcp_b[["Length"]].to_numpy())
sub_group2.create_dataset("Payload Length",data=tcp_b[["Payload Length"]].to_numpy())
sub_group2.create_dataset("Window",data=tcp_b[["Window"]].to_numpy())
sub_group2.create_dataset("Flags",data=tcp_b[["Flags"]].to_numpy())
sub_group2.create_dataset("Detection",data=tcp_b[["Detection"]].to_numpy())
# SG 3 #
sub_group3.create_dataset("Source",data=tcp_c[["Source"]].to_numpy())
sub_group3.create_dataset("Destination",data=tcp_c[["Destination"]].to_numpy())
sub_group3.create_dataset("Protocol",data=tcp_c[["Protocol"]].to_numpy())
sub_group3.create_dataset("Length",data=tcp_c[["Length"]].to_numpy())
sub_group3.create_dataset("Payload Length",data=tcp_c[["Payload Length"]].to_numpy())
sub_group3.create_dataset("Window",data=tcp_c[["Window"]].to_numpy())
sub_group3.create_dataset("Flags",data=tcp_c[["Flags"]].to_numpy())
sub_group3.create_dataset("Detection",data=tcp_c[["Detection"]].to_numpy())
# SG 4 #
sub_group4.create_dataset("Source",data=tcp_d[["Source"]].to_numpy())
sub_group4.create_dataset("Destination",data=tcp_d[["Destination"]].to_numpy())
sub_group4.create_dataset("Protocol",data=tcp_d[["Protocol"]].to_numpy())
sub_group4.create_dataset("Length",data=tcp_d[["Length"]].to_numpy())
sub_group4.create_dataset("Payload Length",data=tcp_d[["Payload Length"]].to_numpy())
sub_group4.create_dataset("Window",data=tcp_d[["Window"]].to_numpy())
sub_group4.create_dataset("Flags",data=tcp_d[["Flags"]].to_numpy())
sub_group4.create_dataset("Detection",data=tcp_d[["Detection"]].to_numpy())
# SG 5 #
sub_group5.create_dataset("Source",data=tcp_e[["Source"]].to_numpy())
sub_group5.create_dataset("Destination",data=tcp_e[["Destination"]].to_numpy())
sub_group5.create_dataset("Protocol",data=tcp_e[["Protocol"]].to_numpy())
sub_group5.create_dataset("Length",data=tcp_e[["Length"]].to_numpy())
sub_group5.create_dataset("Payload Length",data=tcp_e[["Payload Length"]].to_numpy())
sub_group5.create_dataset("Window",data=tcp_e[["Window"]].to_numpy())
sub_group5.create_dataset("Flags",data=tcp_e[["Flags"]].to_numpy())
sub_group5.create_dataset("Detection",data=tcp_e[["Detection"]].to_numpy())
# ICMPv6 - Source,Destination,Protocol,Length,Payload Length,Type,Data,Detection #
# SG 6 #
sub_group6.create_dataset("Source",data=icmpv6_a[["Source"]].to_numpy())
sub_group6.create_dataset("Destination",data=icmpv6_a[["Destination"]].to_numpy())
sub_group6.create_dataset("Protocol",data=icmpv6_a[["Protocol"]].to_numpy())
sub_group6.create_dataset("Length",data=icmpv6_a[["Length"]].to_numpy())
sub_group6.create_dataset("Payload Length",data=icmpv6_a[["Payload Length"]].to_numpy())
sub_group6.create_dataset("Type",data=icmpv6_a[["Type"]].to_numpy())
sub_group6.create_dataset("Data",data=icmpv6_a[["Data"]].to_numpy())
sub_group6.create_dataset("Detection",data=icmpv6_a[["Detection"]].to_numpy())
# SG 7 #
sub_group7.create_dataset("Source",data=icmpv6_b[["Source"]].to_numpy())
sub_group7.create_dataset("Destination",data=icmpv6_b[["Destination"]].to_numpy())
sub_group7.create_dataset("Protocol",data=icmpv6_b[["Protocol"]].to_numpy())
sub_group7.create_dataset("Length",data=icmpv6_b[["Length"]].to_numpy())
sub_group7.create_dataset("Payload Length",data=icmpv6_b[["Payload Length"]].to_numpy())
sub_group7.create_dataset("Type",data=icmpv6_b[["Type"]].to_numpy())
sub_group7.create_dataset("Data",data=icmpv6_b[["Data"]].to_numpy())
sub_group7.create_dataset("Detection",data=icmpv6_b[["Detection"]].to_numpy())
# SG 8 #
sub_group8.create_dataset("Source",data=icmpv6_c[["Source"]].to_numpy())
sub_group8.create_dataset("Destination",data=icmpv6_c[["Destination"]].to_numpy())
sub_group8.create_dataset("Protocol",data=icmpv6_c[["Protocol"]].to_numpy())
sub_group8.create_dataset("Length",data=icmpv6_c[["Length"]].to_numpy())
sub_group8.create_dataset("Payload Length",data=icmpv6_c[["Payload Length"]].to_numpy())
sub_group8.create_dataset("Type",data=icmpv6_c[["Type"]].to_numpy())
sub_group8.create_dataset("Data",data=icmpv6_c[["Data"]].to_numpy())
sub_group8.create_dataset("Detection",data=icmpv6_c[["Detection"]].to_numpy())
# SG 9 #
sub_group9.create_dataset("Source",data=icmpv6_d[["Source"]].to_numpy())
sub_group9.create_dataset("Destination",data=icmpv6_d[["Destination"]].to_numpy())
sub_group9.create_dataset("Protocol",data=icmpv6_d[["Protocol"]].to_numpy())
sub_group9.create_dataset("Length",data=icmpv6_d[["Length"]].to_numpy())
sub_group9.create_dataset("Payload Length",data=icmpv6_d[["Payload Length"]].to_numpy())
sub_group9.create_dataset("Type",data=icmpv6_d[["Type"]].to_numpy())
sub_group9.create_dataset("Data",data=icmpv6_d[["Data"]].to_numpy())
sub_group9.create_dataset("Detection",data=icmpv6_d[["Detection"]].to_numpy())
# SG 10 #
sub_group10.create_dataset("Source",data=icmpv6_e[["Source"]].to_numpy())
sub_group10.create_dataset("Destination",data=icmpv6_e[["Destination"]].to_numpy())
sub_group10.create_dataset("Protocol",data=icmpv6_e[["Protocol"]].to_numpy())
sub_group10.create_dataset("Length",data=icmpv6_e[["Length"]].to_numpy())
sub_group10.create_dataset("Payload Length",data=icmpv6_e[["Payload Length"]].to_numpy())
sub_group10.create_dataset("Type",data=icmpv6_e[["Type"]].to_numpy())
sub_group10.create_dataset("Data",data=icmpv6_e[["Data"]].to_numpy())
sub_group10.create_dataset("Detection",data=icmpv6_e[["Detection"]].to_numpy())
## Flush to Save File ##
print("Writing HDF5 File")
file.flush()
file.close()

## Reload for Testing ##
print("Reading HDF5 File")
file = h5py.File("Intrusion_Sample_IPv6.hdf5","r")
## Try Read ##
for group1 in file.keys():
    print(f" - {group1}")
    for group2 in file[group1].keys():
        print(f" --- {group2}")
        for group3 in file[group1][group2].keys():
            print(f" ----- {group3}")
            datasets = list(file[group1][group2][group3])
            print(f" ------- {datasets}")