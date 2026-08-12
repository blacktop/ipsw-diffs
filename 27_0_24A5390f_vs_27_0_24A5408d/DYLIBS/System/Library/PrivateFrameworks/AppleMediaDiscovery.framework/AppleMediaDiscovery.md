## AppleMediaDiscovery

> `/System/Library/PrivateFrameworks/AppleMediaDiscovery.framework/AppleMediaDiscovery`

```diff

-1.5.4.0.0
-  __TEXT.__text: 0xf3928
+1.5.6.0.0
+  __TEXT.__text: 0xf3b94
   __TEXT.__objc_methlist: 0x3b60
   __TEXT.__const: 0xba8
-  __TEXT.__cstring: 0xac48
-  __TEXT.__oslogstring: 0x46d7
-  __TEXT.__gcc_except_tab: 0x28d8
+  __TEXT.__cstring: 0xac68
+  __TEXT.__oslogstring: 0x46f7
+  __TEXT.__gcc_except_tab: 0x28f0
   __TEXT.__dlopen_cstrs: 0xcc
   __TEXT.__swift5_typeref: 0x5a8
   __TEXT.__swift5_capture: 0x75c

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xda0
+  __DATA_CONST.__const: 0xda8
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x12c0
   __DATA_CONST.__got: 0x6d8
   __AUTH_CONST.__const: 0x13c0
-  __AUTH_CONST.__cfstring: 0xda80
+  __AUTH_CONST.__cfstring: 0xdaa0
   __AUTH_CONST.__objc_const: 0x62d0
   __AUTH_CONST.__objc_intobj: 0xcf0
   __AUTH_CONST.__objc_dictobj: 0x1068

   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 2037
-  Symbols:   3956
-  CStrings:  2390
+  Symbols:   3958
+  CStrings:  2394
 
Symbols:
+ ___block_descriptor_89_e8_32s40s48s56s64r72r_e5_v8?0ls32l8r64l8s40l8s48l8s56l8r72l8
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_AppleMediaDiscovery
- ___block_descriptor_80_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8s48l8r64l8
Functions:
~ +[AMDSQLite insertRowsInternal:usingSchema:error:] : 2364 -> 2712
~ -[AMDSQLite insertRows:usingSchema:skipValidation:error:] : 2780 -> 2932
~ ___57-[AMDSQLite insertRows:usingSchema:skipValidation:error:]_block_invoke : 2100 -> 2220
CStrings:
+ "BEGIN TRANSACTION"
+ "COMMIT"
+ "SQLITE Bulk insert: %s"
+ "bulkInsert"
```
