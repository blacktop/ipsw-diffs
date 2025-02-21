## libmdns.dylib

> `/usr/lib/libmdns.dylib`

```diff

-2559.80.8.0.0
-  __TEXT.__text: 0x310dc
-  __TEXT.__auth_stubs: 0x1c40
-  __TEXT.__objc_methlist: 0x10c
+2600.100.139.502.3
+  __TEXT.__text: 0x3120c
+  __TEXT.__auth_stubs: 0x1c50
+  __TEXT.__objc_methlist: 0x2ec
+  __TEXT.__cstring: 0x1ffe
   __TEXT.__const: 0x1ad
   __TEXT.__gcc_except_tab: 0xf4
-  __TEXT.__cstring: 0x1ff1
   __TEXT.__oslogstring: 0x36f4
-  __TEXT.__unwind_info: 0x988
+  __TEXT.__unwind_info: 0x968
   __TEXT.__objc_classname: 0x56b
   __TEXT.__objc_methname: 0xd27
   __TEXT.__objc_methtype: 0x52d
   __TEXT.__objc_stubs: 0xce0
-  __DATA_CONST.__got: 0x230
+  __DATA_CONST.__got: 0x228
   __DATA_CONST.__const: 0x2a78
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x378
-  __AUTH_CONST.__auth_got: 0xe30
+  __DATA_CONST.__objc_selrefs: 0x468
+  __AUTH_CONST.__auth_got: 0xe38
+  __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x14e0
   __AUTH_CONST.__cfstring: 0x520
-  __AUTH_CONST.__objc_const: 0x37e8
+  __AUTH_CONST.__objc_const: 0x3478
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_classrefs: 0xd0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 814
-  Symbols:   1351
-  CStrings:  1103
+  Functions: 800
+  Symbols:   1353
+  CStrings:  1105
 
Symbols:
+ _mdns_fnv1a_32_hash
+ _objc_release_x9
CStrings:
+ " (%u)"
+ "TCP info get -- local: %{network:in_addr}u:%d, remote: %{network:in_addr}u:%d, error: %{mdns:err}ld"
+ "TYPE%d"
- "TCP info get -- local: %{network:in_addr}d:%d, remote: %{network:in_addr}d:%d, error: %{mdns:err}ld"

```
