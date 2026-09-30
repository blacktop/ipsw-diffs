## libpcap.A.dylib

> `/usr/lib/libpcap.A.dylib`

```diff

-  __TEXT.__text: 0x20dd0
+  __TEXT.__text: 0x20e10
   __TEXT.__const: 0xc330
-  __TEXT.__cstring: 0x6c2e
+  __TEXT.__cstring: 0x6c4c
   __TEXT.__unwind_info: 0x590
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x14c0

   __DATA.__common: 0x8
   __DATA_DIRTY.__bss: 0x545
   - /usr/lib/libSystem.B.dylib
-  Functions: 524
-  Symbols:   939
-  CStrings:  1079
+  Functions: 525
+  Symbols:   941
+  CStrings:  1080
 
Sections:
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _pcap_nametoeproto : 84 -> 100
~ _pcap_nametollc : 80 -> 96
~ ___pcap_atoin : 120 -> 108
~ _bpf_optimize : 1540 -> 1516
~ _pcap_setup_pktap_interface : 1880 -> 1908
~ _pcap_datalink_val_to_description : 64 -> 72
~ _pcap_datalink_val_to_description_or_dlt : 132 -> 140
~ _pcap_tstamp_type_val_to_description : 68 -> 76
~ _str2tok : 112 -> 116
~ _pcap_lex : 3712 -> 3708
~ _pcap__create_buffer : 140 -> 136
~ _stou : 352 -> 336
~ _pcap__scan_buffer : 160 -> 152
~ _pcap__scan_bytes : 144 -> 156
~ _pcap_lex_init : 152 -> 156
~ _pcap_lex_init_extra : 164 -> 168
CStrings:
+ "bad length in yy_scan_bytes()"

```
