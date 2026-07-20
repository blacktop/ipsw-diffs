## tcpdump

> `/usr/sbin/tcpdump`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`
- `__DATA.__bss`

```diff

 161.0.0.0.0
-  __TEXT.__text: 0x97758
+  __TEXT.__text: 0x97858
   __TEXT.__auth_stubs: 0xce0
   __TEXT.__const: 0xc75
-  __TEXT.__cstring: 0x383d1
+  __TEXT.__cstring: 0x384ca
   __TEXT.__oslogstring: 0xb0
   __TEXT.__unwind_info: 0xb40
   __DATA_CONST.__const: 0x22910

   - /usr/lib/libssl.48.dylib
   Functions: 909
   Symbols:   2261
-  CStrings:  12395
+  CStrings:  12403
 
Functions:
~ _print_pktap_header : 4832 -> 4928
~ sub_10008ccf4 -> sub_10008cd54 : 104 -> 136
~ _print_pcap_ng_block : 8360 -> 8456
~ sub_100095e70 -> sub_100095f50 : 104 -> 136
CStrings:
+ "DROP_REASON_IPSEC_IN_AUTH_FAILED"
+ "DROP_REASON_IPSEC_IN_BAD_SPI"
+ "DROP_REASON_IPSEC_IN_DECRYPT_FAILED"
+ "DROP_REASON_IPSEC_IN_INVALID"
+ "DROP_REASON_IPSEC_IN_MBUF_ALLOC_FAILED"
+ "DROP_REASON_IPSEC_IN_NO_SA"
+ "DROP_REASON_IPSEC_IN_POLICY"
+ "DROP_REASON_IPSEC_IN_REPLAY"
```
