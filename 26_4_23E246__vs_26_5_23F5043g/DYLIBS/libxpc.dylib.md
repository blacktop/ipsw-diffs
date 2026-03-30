## libxpc.dylib

> `/usr/lib/system/libxpc.dylib`

```diff

-3102.102.1.0.0
-  __TEXT.__text: 0x418fc
+3102.120.11.0.0
+  __TEXT.__text: 0x41924
   __TEXT.__auth_stubs: 0x1230
   __TEXT.__objc_methlist: 0x374
   __TEXT.__const: 0x600
-  __TEXT.__cstring: 0x7b4d
+  __TEXT.__cstring: 0x7b7d
   __TEXT.__oslogstring: 0x30f0
   __TEXT.__dof_libxpc: 0xa5d
-  __TEXT.__unwind_info: 0x1298
+  __TEXT.__unwind_info: 0x1290
   __TEXT.__objc_classname: 0x243
   __TEXT.__objc_methname: 0x1e2
   __TEXT.__objc_methtype: 0xb5

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: A08D6F00-102F-31A3-92D5-E65AC7B776DF
-  Functions: 1937
-  Symbols:   4635
-  CStrings:  1378
+  UUID: 1E162D81-9A78-3EC0-98F5-0632A51CC314
+  Functions: 1936
+  Symbols:   4633
+  CStrings:  1379
 
Symbols:
+ ___block_descriptor_tmp.127
+ ___block_descriptor_tmp.135
+ ___block_literal_global.129
+ ___block_literal_global.137
- ___block_descriptor_tmp.126
- ___block_literal_global.128
- __xpc_connection_copy_attrs.cold.1
Functions:
~ __xpc_connection_copy_attrs : 472 -> 564
~ _xpc_copy_entitlement_for_token : 140 -> 212
- __xpc_connection_copy_attrs.cold.1
CStrings:
+ "Could not get attrs using %s for pid %d: %d: %s"

```
