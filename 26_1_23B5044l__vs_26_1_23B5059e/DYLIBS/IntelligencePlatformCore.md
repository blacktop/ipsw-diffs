## IntelligencePlatformCore

> `/System/Library/PrivateFrameworks/IntelligencePlatformCore.framework/IntelligencePlatformCore`

```diff

-155.6.0.2.0
-  __TEXT.__text: 0xab479c
-  __TEXT.__auth_stubs: 0xae00
+155.8.1.0.0
+  __TEXT.__text: 0xab7360
+  __TEXT.__auth_stubs: 0xade0
   __TEXT.__objc_methlist: 0x2e9c
-  __TEXT.__const: 0x74991
+  __TEXT.__const: 0x74c81
   __TEXT.__dlopen_cstrs: 0xc0
-  __TEXT.__cstring: 0x46b8c
+  __TEXT.__cstring: 0x46c8c
   __TEXT.__swift5_typeref: 0x1e74e
   __TEXT.__constg_swiftt: 0x233e4
   __TEXT.__swift5_reflstr: 0x263cf
-  __TEXT.__swift5_fieldmd: 0x29e98
+  __TEXT.__swift5_fieldmd: 0x29ec8
   __TEXT.__swift5_builtin: 0x4d8
-  __TEXT.__swift5_mpenum: 0x16c
+  __TEXT.__swift5_mpenum: 0x170
   __TEXT.__swift5_assocty: 0x2f20
   __TEXT.__swift5_proto: 0x6534
   __TEXT.__swift5_types: 0x21f0
   __TEXT.__swift5_protos: 0x378
   __TEXT.__swift_as_entry: 0x1214
   __TEXT.__swift_as_ret: 0xfb4
-  __TEXT.__oslogstring: 0x1ea33
+  __TEXT.__oslogstring: 0x1e9f3
   __TEXT.__swift5_capture: 0x4520
-  __TEXT.__gcc_except_tab: 0x1c8
-  __TEXT.__unwind_info: 0x28010
-  __TEXT.__eh_frame: 0x61208
+  __TEXT.__gcc_except_tab: 0x1bc
+  __TEXT.__unwind_info: 0x28088
+  __TEXT.__eh_frame: 0x612e0
   __TEXT.__objc_classname: 0x4b3
   __TEXT.__objc_methname: 0xa081
   __TEXT.__objc_methtype: 0x2729
   __TEXT.__objc_stubs: 0x1160
-  __DATA_CONST.__got: 0x43d8
+  __DATA_CONST.__got: 0x43d0
   __DATA_CONST.__const: 0xa60
   __DATA_CONST.__objc_classlist: 0x1210
   __DATA_CONST.__objc_protolist: 0x250

   __DATA_CONST.__objc_selrefs: 0x2d08
   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x80
-  __AUTH_CONST.__auth_got: 0x5710
-  __AUTH_CONST.__const: 0x451a0
+  __AUTH_CONST.__auth_got: 0x5700
+  __AUTH_CONST.__const: 0x451b8
   __AUTH_CONST.__cfstring: 0x360
   __AUTH_CONST.__objc_const: 0x2c588
   __AUTH.__objc_data: 0x36a8
-  __AUTH.__data: 0x18228
+  __AUTH.__data: 0x18188
   __DATA.__objc_ivar: 0xc4
-  __DATA.__data: 0x11368
-  __DATA.__bss: 0x86dd0
+  __DATA.__data: 0x11378
+  __DATA.__bss: 0x86d50
   __DATA.__common: 0x1a40
   __DATA_DIRTY.__objc_data: 0x41e0
-  __DATA_DIRTY.__data: 0x27b70
-  __DATA_DIRTY.__bss: 0x2cc90
+  __DATA_DIRTY.__data: 0x27c00
+  __DATA_DIRTY.__bss: 0x2cd10
   __DATA_DIRTY.__common: 0x17c0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6A536145-EDDA-33AB-9669-129DB304BBE5
-  Functions: 60945
-  Symbols:   889
-  CStrings:  10150
+  UUID: BBB39936-7828-36A2-A303-5D5B5559CF9E
+  Functions: 60978
+  Symbols:   888
+  CStrings:  10152
 
Symbols:
- _objc_alloc_init
CStrings:
+ "    SELECT\n        sourceId,\n        available,\n        lastQueriedSourceData IS NOT NULL\n    FROM\n        sourceState\n    WHERE\n        sourceType = ?\n    AND\n        sourceIdentifier = ?\n    AND\n        updateType = ?"
+ "    UPDATE\n        sourceState\n    SET\n        lastQueriedSourceData = ?\n    WHERE\n        sourceId = ?"
+ "    UPDATE\n        sourceState\n    SET\n        modifiedTimestamp = ?,\n        available = ?,\n        lastQueriedSourceData = NULL\n    WHERE\n        sourceId = ?"
+ "005: cache source state"
+ "lastQueriedSourceData"
- "    SELECT\n        sourceId,\n        available\n    FROM\n        sourceState\n    WHERE\n        sourceType = ?\n    AND\n        sourceIdentifier = ?\n    AND\n        updateType = ?"
- "    UPDATE\n        sourceState\n    SET\n        modifiedTimestamp = ?,\n        available = ?\n    WHERE\n        sourceId = ?"
- "ViewUpdate: Clearing resources for manager for: %s"

```
