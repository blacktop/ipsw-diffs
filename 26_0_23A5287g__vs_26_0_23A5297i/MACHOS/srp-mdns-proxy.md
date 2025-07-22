## srp-mdns-proxy

> `/usr/libexec/srp-mdns-proxy`

```diff

-2881.0.7.0.0
-  __TEXT.__text: 0x83c20
+2881.0.15.0.0
+  __TEXT.__text: 0x842ec
   __TEXT.__auth_stubs: 0x1360
   __TEXT.__objc_stubs: 0x180
   __TEXT.__objc_methlist: 0x21c
   __TEXT.__const: 0x282
-  __TEXT.__cstring: 0x7671
-  __TEXT.__oslogstring: 0x11eb8
+  __TEXT.__cstring: 0x7685
+  __TEXT.__oslogstring: 0x11f81
   __TEXT.__objc_classname: 0x38
   __TEXT.__objc_methname: 0x4e6
   __TEXT.__objc_methtype: 0x237
-  __TEXT.__unwind_info: 0x580
+  __TEXT.__unwind_info: 0x588
   __DATA_CONST.__auth_got: 0x9b8
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__auth_ptr: 0x10

   - /usr/lib/libmdns.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8FE6A589-F3E4-3E55-A3C8-2F4D683CEAA9
+  UUID: E6DE7121-1CD6-3EDB-97AA-5B8268775664
   Functions: 453
   Symbols:   1137
-  CStrings:  2459
+  CStrings:  2466
 
Symbols:
+ __block_descriptor_tmp.1353
+ __block_descriptor_tmp.17.1443
+ __block_descriptor_tmp.18.1537
+ __block_descriptor_tmp.2546
+ __block_descriptor_tmp.8.1400
+ __block_literal_global.1444
- __block_descriptor_tmp.1348
- __block_descriptor_tmp.17.1438
- __block_descriptor_tmp.18.1532
- __block_descriptor_tmp.2541
- __block_descriptor_tmp.8.1395
- __block_literal_global.1439
Functions:
~ _deliver_request : 1000 -> 1020
~ _srpk_label_from_wire_ : 1988 -> 2940
~ _omr_watcher_onmesh_prefix_list_callback : 1100 -> 1104
~ _omr_watcher_netdata_callback : 1236 -> 1240
~ _dp_query_add_data_to_response : 5016 -> 5040
~ _srp_dns_evaluate : 18964 -> 19700
CStrings:
+ "%02X"
+ "%{public}s: %s:%d: %03lx: %{public}s"
+ "%{public}s: bogus underline-char-ptr offset %llu"
+ "%{public}s: generative pattern inlen %d len %d"
+ "%{public}s: underline char hex %x"
+ "%{public}s: underline char ptr %x"
+ "03:35:35"
+ "Jul 11 2025"
+ "srpk_hex_dump_"
- "02:53:58"
- "Jun 27 2025"

```
