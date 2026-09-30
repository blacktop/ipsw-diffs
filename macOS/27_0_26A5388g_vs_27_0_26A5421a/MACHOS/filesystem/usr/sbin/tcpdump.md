## tcpdump

> `/usr/sbin/tcpdump`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

 161.0.0.0.0
-  __TEXT.__text: 0x97858
+  __TEXT.__text: 0x978b8
   __TEXT.__auth_stubs: 0xce0
   __TEXT.__const: 0xc75
-  __TEXT.__cstring: 0x384ca
+  __TEXT.__cstring: 0x3852a
   __TEXT.__oslogstring: 0xb0
   __TEXT.__unwind_info: 0xb40
   __DATA_CONST.__const: 0x22910

   - /usr/lib/libssl.48.dylib
   Functions: 909
   Symbols:   2261
-  CStrings:  12403
+  CStrings:  12406
 
Functions:
~ _print_pktap_header : 4928 -> 4964
~ sub_10008cddc -> sub_10008ce00 : 172 -> 184
~ _print_pcap_ng_block : 8456 -> 8492
~ sub_100095fd8 -> sub_10009602c : 172 -> 184
CStrings:
+ "DROP_REASON_IP6_ND_CACHE_TEARDOWN"
+ "DROP_REASON_IP6_ND_HOLD_EVICTED"
+ "DROP_REASON_IP6_RA_BAD_ND_OPT"
```
