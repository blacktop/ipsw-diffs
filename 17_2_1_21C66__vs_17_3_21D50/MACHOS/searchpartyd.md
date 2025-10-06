## searchpartyd

> `/usr/libexec/searchpartyd`

```diff

-356.7.0.0.0
-  __TEXT.__text: 0x1008464
+356.9.0.0.0
+  __TEXT.__text: 0x1009104
   __TEXT.__auth_stubs: 0x5de0
   __TEXT.__objc_stubs: 0x40
   __TEXT.__objc_methlist: 0x13e8

   __TEXT.__objc_classname: 0x519
   __TEXT.__objc_methname: 0xcbfc
   __TEXT.__objc_methtype: 0x3f9c
-  __TEXT.__cstring: 0x67b43
+  __TEXT.__cstring: 0x67c53
   __TEXT.__swift5_typeref: 0x1d518
   __TEXT.__const: 0x48d58
   __TEXT.__constg_swiftt: 0x1973c

   __TEXT.__swift5_protos: 0x284
   __TEXT.__swift5_mpenum: 0x3c4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x2ea3c
-  __TEXT.__eh_frame: 0x682f8
+  __TEXT.__unwind_info: 0x2eab4
+  __TEXT.__eh_frame: 0x68360
   __DATA_CONST.__auth_got: 0x2ef8
   __DATA_CONST.__got: 0x1b98
   __DATA_CONST.__auth_ptr: 0xd70

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 479CEB5D-2090-31F2-BA10-552C005F63C4
-  Functions: 64190
+  UUID: 94D86FAD-6395-3D72-9686-746384F39736
+  Functions: 64193
   Symbols:   2807
-  CStrings:  10841
+  CStrings:  10845
 
CStrings:
+ "Error gathering payloads for owned device %{private,mask.hash}s, error: %s."
+ "Error publishing owned devices count %ld, error: %s."
+ "No observations to publish for device %{private,mask.hash}s."
+ "No observations to publish for owned devices count %ld."
+ "No observations to publish for shared device %{private,mask.hash}s."
- "Error publishing owned device %{private,mask.hash}s, location %s."

```
