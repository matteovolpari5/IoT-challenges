import pyshark
import re
import socket
import sys

# CQ2) How many CoAP resources in the coap.me public server received the
# same number of unique Confirmable and Non Confirmable GET requests?
# Assuming a resource receives X different CONFIRMABLE requests and Y different
# NONCONFIRMABLE GET requests, how many resources have X=Y, with X>0?

def answer_cq2(capture):

    try:
        coap_me_ip = socket.gethostbyname("coap.me")
    except Exception as e:
        print("Errore nella risoluzione DNS:", e)
        return 0
    
    resource_stats = {}
    for pkt in capture:
        try:
            if 'IP' not in pkt or pkt.ip.dst != coap_me_ip:
                continue

            # check CoAP layer
            if 'COAP' in pkt:
                coap = pkt.coap
                
                # get fields 
                coap_code = int(coap.get_field('code')) if hasattr(coap, 'code') else None
                coap_type = int(coap.get_field('type')) if hasattr(coap, 'type') else None
                token = coap.get_field('token') if hasattr(coap, 'token') else None
                if not token:
                    continue
                resource = coap.get_field('opt_uri_path') if hasattr(coap, 'opt_uri_path') else None
                if not resource:
                    continue
                
                name = coap.get_field('uri_host') if hasattr(coap, 'opt_name') else None

                # check GET request 
                if coap_code != 1:
                    continue
                if resource not in resource_stats:
                    resource_stats[resource] = {'conf': set(), 'nonconf': set()}
                if coap_type == 0:
                    # CON
                    resource_stats[resource]['conf'].add(token)
                elif coap_type == 1:
                    # NON
                    resource_stats[resource]['nonconf'].add(token)
        except Exception:
            continue
    
    count = 0
    for stats in resource_stats.values():
        if len(stats['conf']) == len(stats['nonconf']) and len(stats['conf']) > 0:
            count += 1
    return count

def main():
    if len(sys.argv) != 2:
        print("pcap file not provided")
        sys.exit(1)
    pcap_file = sys.argv[1]
    print("loading pcap file")
    capture = pyshark.FileCapture(pcap_file, keep_packets=False)
    
    print(answer_cq2(capture))
    
    capture.close()


if __name__ == "__main__":
    main()