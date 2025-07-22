## libmdns.dylib

> `/usr/lib/libmdns.dylib`

```diff

-2881.0.7.0.0
-  __TEXT.__text: 0x32084
-  __TEXT.__auth_stubs: 0x1d20
+2881.0.15.0.0
+  __TEXT.__text: 0x320f4
+  __TEXT.__auth_stubs: 0x1d30
   __TEXT.__objc_methlist: 0x2ec
   __TEXT.__cstring: 0x21a3
   __TEXT.__const: 0x1ad

   __TEXT.__unwind_info: 0x990
   __TEXT.__eh_frame: 0x74
   __TEXT.__objc_classname: 0x57f
-  __TEXT.__objc_methname: 0xd33
+  __TEXT.__objc_methname: 0xd5a
   __TEXT.__objc_methtype: 0x52d
-  __TEXT.__objc_stubs: 0xce0
+  __TEXT.__objc_stubs: 0xd20
   __DATA_CONST.__got: 0x2d8
   __DATA_CONST.__const: 0x2b20
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x468
+  __DATA_CONST.__objc_selrefs: 0x478
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0xea0
+  __AUTH_CONST.__auth_got: 0xea8
   __AUTH_CONST.__const: 0x14c0
   __AUTH_CONST.__cfstring: 0x520
   __AUTH_CONST.__objc_const: 0x3580

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EB05C070-77FE-3514-92C6-DDA6479FC0D3
+  UUID: 040DD38B-646F-3490-9585-798B94CDEEAD
   Functions: 815
-  Symbols:   3032
-  CStrings:  1178
+  Symbols:   3035
+  CStrings:  1180
 
Symbols:
+ _nw_parameters_set_is_encrypted_dns_resolver_connection
+ _objc_msgSend$requestParameters
+ _objc_msgSend$setQualityOfService:
Functions:
~ +[DNSHeuristics updateHeuristicState:isTimeout:] : 1712 -> 1744
~ __mdns_https_resolver_get_stream_params : 396 -> 432
~ __mdns_tls_resolver_get_stream_params : 344 -> 388
CStrings:
+ "requestParameters"
+ "setQualityOfService:"

```
