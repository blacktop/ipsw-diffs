## tcpdump

> `/usr/sbin/tcpdump`

```diff

 156.0.0.0.0
-  __TEXT.__text: 0x98ef8
+  __TEXT.__text: 0x98f18
   __TEXT.__auth_stubs: 0xcf0
   __TEXT.__const: 0xc89
-  __TEXT.__cstring: 0x37eb2
+  __TEXT.__cstring: 0x37ed8
   __TEXT.__oslogstring: 0xa8
   __TEXT.__unwind_info: 0xaa0
   __DATA_CONST.__auth_got: 0x678

   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libpcap.A.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: A8745528-04D6-3A7C-849D-9428D98A1231
+  UUID: 4E153418-9CA2-3308-81A1-65A0C6B0194E
   Functions: 881
   Symbols:   2286
-  CStrings:  12359
+  CStrings:  12360
 
Functions:
~ _print_pktap_header : 4856 -> 4868
~ sub_10008e370 -> sub_10008e37c : 80 -> 84
~ _print_pcap_ng_block : 8828 -> 8840
~ sub_1000974e8 -> sub_100097504 : 80 -> 84
CStrings:
+ "DROP_REASON_FSW_DEMUX_L2_MULTI_L3_UNI"

```
