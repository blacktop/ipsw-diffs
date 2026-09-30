## tcpdump

> `/usr/sbin/tcpdump`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

 161.0.0.0.0
-  __TEXT.__text: 0x95df8
+  __TEXT.__text: 0x960bc
   __TEXT.__auth_stubs: 0xce0
   __TEXT.__const: 0xc75
-  __TEXT.__cstring: 0x3852a
+  __TEXT.__cstring: 0x387a7
   __TEXT.__oslogstring: 0xb0
   __TEXT.__unwind_info: 0xee0
   __DATA_CONST.__const: 0x22910

   - /usr/lib/libssl.48.dylib
   Functions: 909
   Symbols:   2261
-  CStrings:  12406
+  CStrings:  12428
 
Functions:
~ _print_pktap_header : 4964 -> 5224
~ sub_10008b428 -> sub_10008b52c : 184 -> 212
~ sub_10008b4e0 -> sub_10008b600 : 40 -> 100
~ _print_pcap_ng_block : 8492 -> 8764
~ sub_1000945cc -> sub_100094838 : 184 -> 212
~ sub_100094684 -> sub_10009490c : 40 -> 100
CStrings:
+ "DROP_REASON_IP6_EXTHDR_TOO_LONG"
+ "DROP_REASON_IP6_EXTHDR_TOO_SHORT"
+ "DROP_REASON_IP6_MCAST_NOT_TRANSMITTED"
+ "DROP_REASON_IP6_NA_EHSRC_MISMATCH"
+ "DROP_REASON_IP6_NS_DAD_IN_PROGRESS"
+ "DROP_REASON_IP6_RS_BAD_ND_OPT"
+ "DROP_REASON_IP6_RS_FROM_NON_NEIGHBOR"
+ "DROP_REASON_PF_BAD_OFFSET"
+ "DROP_REASON_PF_BAD_TIMESTAMP"
+ "DROP_REASON_PF_CONGESTION"
+ "DROP_REASON_PF_DUMMYNET"
+ "DROP_REASON_PF_INVALID_PORT"
+ "DROP_REASON_PF_IP_OPTION"
+ "DROP_REASON_PF_NORMALIZE"
+ "DROP_REASON_PF_PROTO_CKSUM"
+ "DROP_REASON_PF_ROUTE_LOOP"
+ "DROP_REASON_PF_ROUTE_OUTPUT"
+ "DROP_REASON_PF_SRC_LIMIT"
+ "DROP_REASON_PF_STATE_INSERT"
+ "DROP_REASON_PF_STATE_LIMIT"
+ "DROP_REASON_PF_STATE_MISMATCH"
+ "DROP_REASON_PF_SYNPROXY"
```
