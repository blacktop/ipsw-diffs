## libxpc.dylib

> `/usr/lib/system/libxpc.dylib`

```diff

-3102.100.97.502.1
-  __TEXT.__text: 0x41944
+3102.100.101.502.1
+  __TEXT.__text: 0x418fc
   __TEXT.__auth_stubs: 0x1230
   __TEXT.__objc_methlist: 0x374
   __TEXT.__const: 0x600
-  __TEXT.__cstring: 0x7b6e
-  __TEXT.__oslogstring: 0x30c4
+  __TEXT.__cstring: 0x7b4d
+  __TEXT.__oslogstring: 0x30f0
   __TEXT.__dof_libxpc: 0xa5d
-  __TEXT.__unwind_info: 0x1288
+  __TEXT.__unwind_info: 0x1298
   __TEXT.__objc_classname: 0x243
   __TEXT.__objc_methname: 0x1e2
   __TEXT.__objc_methtype: 0xb5
   __TEXT.__objc_stubs: 0x100
   __DATA_CONST.__got: 0x1e0
-  __DATA_CONST.__const: 0x1c10
+  __DATA_CONST.__const: 0x1c20
   __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_nlclslist: 0xe8
   __DATA_CONST.__objc_protolist: 0xf8

   - /usr/lib/system/libsystem_sandbox.dylib
   - /usr/lib/system/libsystem_trace.dylib
   - /usr/lib/system/libunwind.dylib
-  UUID: 731970E2-842D-3CF9-BCA0-76AEE5CEAC6C
-  Functions: 1935
-  Symbols:   4630
-  CStrings:  1379
+  UUID: EE6E72F2-FFB9-38B6-99B8-0158FE26C221
+  Functions: 1937
+  Symbols:   4635
+  CStrings:  1378
 
Symbols:
+ ___block_descriptor_tmp.41
+ __cryptex_prefix_paths
+ __normalize_cryptex_path.cold.1
+ __trim_trailing_slashes
+ __xpc_resolve_real_path
- __copy_path_in_shared_cache
CStrings:
+ "The executable did not ship in the bundle"
+ "assertion failure: \"prefix_len > 0\" -> %llu"
+ "bundle %s missing from disk and dyld shared cache"
- "bundle %s missing from disk and dyld shared cache, error=%d"
- "failed to resolve executable"
- "linked resources"
- "missing executable"

```
