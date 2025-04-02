import pyshark
import re
import socket
import sys

def answer_cq2(capture):
    # IP found with Wireshark filter
    coap_me_ip = "134.102.218.18"
    
    resource_stats = {}
    for pkt in capture:
        try:
            # check destination is coap.me
            if 'IP' not in pkt or pkt.ip.dst != coap_me_ip:
                continue

            # check CoAP layer
            if 'COAP' in pkt:
                coap = pkt.coap
                
                # get fields 
                coap_type = int(coap.get_field('type')) if hasattr(coap, 'type') else None
                coap_code = int(coap.get_field('code')) if hasattr(coap, 'code') else None
                token = coap.get_field('token') if hasattr(coap, 'token') else None
                resource = coap.get_field('opt_uri_path') if hasattr(coap, 'opt_uri_path') else None                
                if coap_type is None or coap_code is None or token is None or resource is None:
                    continue
                
                # check GET request 
                if coap_code != 1:
                    continue
                if resource not in resource_stats:
                    resource_stats[resource] = {'conf': set(), 'nonconf': set()}
                if coap_type == 0:
                    # Confirmable
                    resource_stats[resource]['conf'].add(token)
                elif coap_type == 1:
                    # Non Confirmable
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
    capture = pyshark.FileCapture(pcap_file, keep_packets=False)
    print(answer_cq2(capture))
    capture.close()


if __name__ == "__main__":
    main()