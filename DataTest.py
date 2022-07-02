import pandas as pd
import hashlib
from sklearn.model_selection import train_test_split
from collections import Counter

## Start of Data Preparation Section ##
def dataPrep():
    ## Sampel Data TCP
    # Normal
    tcp_a = pd.read_csv("dataset/sample-tcp-nping-noopt.csv",delimiter=",")
    # Intrusion
    tcp_b = pd.read_csv("dataset/sample-tcp-thcsyn6-ack.csv",delimiter=",")[0:250]
    tcp_c = pd.read_csv("dataset/sample-tcp-thcsyn6-hopbyhop.csv",delimiter=",")[0:250]
    tcp_d = pd.read_csv("dataset/sample-tcp-thcsyn6-noopt.csv",delimiter=",")[0:250]
    tcp_e = pd.read_csv("dataset/sample-tcp-thcsyn6-synack.csv",delimiter=",")[0:250]

    # Merge TCP Set
    frame_tcp = [tcp_a,tcp_b,tcp_c,tcp_d,tcp_e]
    tcp_packets = pd.concat(frame_tcp)
    tcp_packets.fillna(0)

    ## Sampel Data ICMPv6
    # Normal
    icmpv6_a = pd.read_csv("dataset/sample-icmpv6-fping-noopt.csv",delimiter=",")
    # Intrusion
    icmpv6_b = pd.read_csv("dataset/sample-icmpv6-rsmurf6-noopt.csv",delimiter=",")[0:250]
    icmpv6_c = pd.read_csv("dataset/sample-icmpv6-denial6-testcase1.csv",delimiter=",")[0:250]
    icmpv6_d = pd.read_csv("dataset/sample-icmpv6-denial6-testcase2.csv",delimiter=",")[0:250]
    icmpv6_e = pd.read_csv("dataset/sample-icmpv6-flood_unreach6-fragment.csv",delimiter=",")[0:250]

    # Merge ICMPv6 Set and Drop Kolom
    frame_icmpv6 = [icmpv6_a,icmpv6_b,icmpv6_c,icmpv6_d,icmpv6_e]
    icmpv6_packets = pd.concat(frame_icmpv6)
    icmpv6_packets.fillna(0)

    # Rename kolom spesifik protokol ke umum feat1 feat2 feat3 feat4 feat5
    tcp_packets = tcp_packets.rename(columns={"Protocol":"Feat1","Length":"Feat2","Payload Length":"Feat3","Window":"Feat4","Flags":"Feat5"})
    icmpv6_packets = icmpv6_packets.rename(columns={"Protocol":"Feat1","Length":"Feat2","Payload Length":"Feat3","Type":"Feat4","Data":"Feat5"})

    # Merging Semua Data
    frame_packets = [tcp_packets,icmpv6_packets]
    packets = pd.concat(frame_packets)

    # Hashing ke Desimal
    packets["Feat1"] = packets["Feat1"].astype(str).apply(hashData)
    packets["Feat2"] = packets["Feat2"].astype(str).apply(hashData)
    packets["Feat3"] = packets["Feat3"].astype(str).apply(hashData)
    packets["Feat4"] = packets["Feat4"].astype(str).apply(hashData)
    packets["Feat5"] = packets["Feat5"].astype(str).apply(hashData)

    # Split Data Train Test
    packets = pd.DataFrame(packets)
    train, test = train_test_split(packets, test_size=0.3,stratify=packets[['Feat1','Feat2','Feat3','Feat4','Feat5','Detection']])
    tr_0 = train['Feat3'].value_counts()
    print(train.head())
    print(tr_0)

    # Convert to List
    train = train.values.tolist()
    test = test.values.tolist()
    num_train = len(train)
    num_test = len(test)
    return train,num_train,test,num_test
## End of Data Preparation Section ##

def hashData(rowData):
    return str(int(hashlib.sha1(str(rowData).encode("UTF-8")).hexdigest(),16))[:10]

def main():
    train,num_train,test,num_test = dataPrep()


if __name__ == '__main__':
    main()
