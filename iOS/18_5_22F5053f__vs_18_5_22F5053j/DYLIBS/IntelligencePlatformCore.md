## IntelligencePlatformCore

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore`

```diff

-124.17.0.1.0
-  __TEXT.__text: 0xa156e8
+124.18.0.0.0
+  __TEXT.__text: 0xa159b8
   __TEXT.__auth_stubs: 0xa010
   __TEXT.__objc_methlist: 0x2d04
   __TEXT.__const: 0x6a001
   __TEXT.__dlopen_cstrs: 0xc0
-  __TEXT.__cstring: 0x42603
+  __TEXT.__cstring: 0x42693
   __TEXT.__swift5_typeref: 0x1c888
   __TEXT.__constg_swiftt: 0x215fc
-  __TEXT.__swift5_reflstr: 0x238ef
+  __TEXT.__swift5_reflstr: 0x238df
   __TEXT.__swift5_fieldmd: 0x24624
   __TEXT.__swift5_builtin: 0x4b0
   __TEXT.__swift5_mpenum: 0x128

   __TEXT.__swift5_protos: 0x360
   __TEXT.__swift_as_entry: 0x10dc
   __TEXT.__swift_as_ret: 0xeb8
-  __TEXT.__oslogstring: 0x1ef83
+  __TEXT.__oslogstring: 0x1f013
   __TEXT.__swift5_capture: 0x39c0
   __TEXT.__gcc_except_tab: 0x148
-  __TEXT.__unwind_info: 0x26b48
-  __TEXT.__eh_frame: 0x5cfe4
+  __TEXT.__unwind_info: 0x26b70
+  __TEXT.__eh_frame: 0x5d07c
   __TEXT.__objc_classname: 0x4a5
   __TEXT.__objc_methname: 0x983b
   __TEXT.__objc_methtype: 0x259d

   __DATA_CONST.__objc_protorefs: 0x118
   __DATA_CONST.__objc_superrefs: 0x80
   __AUTH_CONST.__auth_got: 0x5018
-  __AUTH_CONST.__auth_ptr: 0x52f0
+  __AUTH_CONST.__auth_ptr: 0x4ba0
   __AUTH_CONST.__const: 0x3f848
   __AUTH_CONST.__cfstring: 0x360
   __AUTH_CONST.__objc_const: 0x2b278

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 56277
+  Functions: 56324
   Symbols:   877
-  CStrings:  9603
+  CStrings:  9606
 
CStrings:
+ "DELETE FROM interactionEntities WHERE interactionRowid IN (SELECT rowid FROM interactions WHERE sourceStreams = '')"
+ "SiriRemembersViewGenerator: deleteOrphanedInteractions completed"
+ "SiriRemembersViewGenerator: deleteOrphanedInteractions started"

```
