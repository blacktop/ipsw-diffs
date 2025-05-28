## libpcap.A.dylib

> `/usr/lib/libpcap.A.dylib`

```diff

-124.0.0.0.0
-  __TEXT.__text: 0x20d80
+126.42.1.0.0
+  __TEXT.__text: 0x213ec
   __TEXT.__auth_stubs: 0x620
   __TEXT.__const: 0xc340
-  __TEXT.__cstring: 0x68cb
-  __TEXT.__unwind_info: 0x600
+  __TEXT.__cstring: 0x6b28
+  __TEXT.__unwind_info: 0x604
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x1418
   __AUTH_CONST.__auth_ptr: 0x10

   __DATA_DIRTY.__const: 0x40
   __DATA_DIRTY.__bss: 0x545
   - /usr/lib/libSystem.B.dylib
-  Functions: 540
-  Symbols:   938
-  CStrings:  1045
+  Functions: 546
+  Symbols:   945
+  CStrings:  1060
 
Symbols:
+ _pcap_darwin_cleanup
+ _pcap_get_max_write_size
+ _pcap_get_send_multiple
+ _pcap_sendpacket_multiple
+ _pcap_set_max_write_size
+ _pcap_set_send_multiple
CStrings:
+ "%s: BIOCGBATCHWRITE errno %d"
+ "%s: BIOCGWRITEMAX errno %d"
+ "%s: BIOCSBATCHWRITE errno %d"
+ "%s: BIOCSWRITEMAX errno %d"
+ "pcap_get_max_write_size"
+ "pcap_get_send_multiple"
+ "pcap_sendpacket_multiple: calloc bpf_hdr array errno %d"
+ "pcap_sendpacket_multiple: calloc iovec array errno %d"
+ "pcap_sendpacket_multiple: count %u greater than max %d"
+ "pcap_sendpacket_multiple: pcap_priv_iov_count %u greater than max %d"
+ "pcap_sendpacket_multiple: pcap_priv_iov_count %u greater that max %d"
+ "pcap_sendpacket_multiple: writev %d failed: %s"
+ "pcap_sendpacket_multiple: writev failed errno %d"
+ "pcap_set_max_write_size"
+ "pcap_set_send_multiple"

```
