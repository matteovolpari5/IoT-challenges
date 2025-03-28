import pyshark
import sys
import re

# CQ1) How many different Confirmable PUT requests obtained an
# unsuccessful response from the local CoAP server?

def answer_cq1(capture):
    requests = {}
    responses = {}
    for pkt in capture:
        try:
            if 'IP' not in pkt or pkt.ip.src != pkt.ip.dst:
                continue

            # check CoAP layer
            if 'COAP' in pkt:
                coap = pkt.coap
                
                # get fields 
                coap_type = int(coap.get_field('type')) if hasattr(coap, 'type') else None
                coap_code = int(coap.get_field('code')) if hasattr(coap, 'code') else None
                token = coap.get_field('token') if hasattr(coap, 'token') else None
                if coap_type is None or coap_code is None or token is None:
                    continue
                if coap_type == 0 and coap_code == 3:
                    requests[token] = pkt
                elif coap_code >= 128:
                    responses[token] = pkt
        except Exception:
            continue
    
    count = sum(1 for token in requests if token in responses)
    return count

def main():
    if len(sys.argv) != 2:
        print("pcap file not provided")
        sys.exit(1)
    pcap_file = sys.argv[1]
    print("loading pcap file")
    capture = pyshark.FileCapture(pcap_file, keep_packets=False)    
    print(answer_cq1(capture))
    capture.close()

if __name__ == "__main__":
    main()