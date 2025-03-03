## GSS

> `/System/Library/Frameworks/GSS.framework/GSS`

```diff

-693.60.3.0.0
-  __TEXT.__text: 0x2819c
+693.100.10.0.0
+  __TEXT.__text: 0x27f38
   __TEXT.__auth_stubs: 0x1ef0
   __TEXT.__const: 0x44a
   __TEXT.__cstring: 0x3b55
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x720
+  __TEXT.__unwind_info: 0x728
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0x1378
   __AUTH_CONST.__auth_got: 0xf78

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libheimdal-asn1.dylib
   - /usr/lib/libresolv.9.dylib
-  Functions: 642
-  Symbols:   1340
+  Functions: 673
+  Symbols:   1381
   CStrings:  673
 
CStrings:
+ "cfxunwrap token too short: %lu"
+ "cfxunwrap-iov token too short: %lu"
+ "cfxverifymic token too short: %lu"
+ "gss-asc: rd_req (server: %s) failed with: %u: %s"
+ "have no subkey of type %u"
- "cfxunwrap token too short: %ld"
- "cfxunwrap-iov token too short: %ld"
- "cfxverifymic token too short: %ld"
- "gss-asc: rd_req (server: %s) failed with: %d: %s"
- "have no subkey of type %d"

```
