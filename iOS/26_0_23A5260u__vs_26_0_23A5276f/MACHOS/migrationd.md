## migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

```diff

-701.0.0.0.0
-  __TEXT.__text: 0x12020
-  __TEXT.__auth_stubs: 0xbf0
+765.0.0.0.0
+  __TEXT.__text: 0x121a8
+  __TEXT.__auth_stubs: 0xc20
   __TEXT.__objc_methlist: 0x2f0
-  __TEXT.__cstring: 0x51c
-  __TEXT.__objc_methname: 0x4cb
+  __TEXT.__cstring: 0x52c
+  __TEXT.__objc_methname: 0x4d2
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x31
   __TEXT.__objc_methtype: 0xe9

   __TEXT.__oslogstring: 0x2bd
   __TEXT.__unwind_info: 0x6a8
   __TEXT.__eh_frame: 0x11a0
-  __DATA_CONST.__auth_got: 0x5f8
-  __DATA_CONST.__got: 0x270
+  __DATA_CONST.__auth_got: 0x610
+  __DATA_CONST.__got: 0x268
   __DATA_CONST.__auth_ptr: 0x1f0
-  __DATA_CONST.__const: 0x900
+  __DATA_CONST.__const: 0x8e0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 18EA3AF5-28C7-3BFA-8622-94E3D42985DB
+  UUID: 4F20B5FD-4EEC-3B82-BBD9-0AC188D5361B
   Functions: 387
-  Symbols:   358
+  Symbols:   356
   CStrings:  157
 
Symbols:
+ _$s12MigrationKit15MigratorContextV6ResultO8rawValues5UInt8Vvg
+ _$s12MigrationKit15MigratorContextV6ResultOMa
+ _$s12MigrationKit15MigratorContextV6resultAC6ResultOvg
- _$s12MigrationKit6ServerC5StateO11progressingyAESd_SdSgtcAEmFWC
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
Functions:
~ sub_10000a758 -> sub_10000a628 : 2424 -> 2624
~ sub_10000b144 -> sub_10000b0dc : 1992 -> 2184
CStrings:
+ "didTransferWithSelection:result:bytes:items:errors:"
+ "v48@0:8C16C20Q24Q32Q40"
- "didTransferWithSelection:bytes:items:errors:"
- "v44@0:8C16Q20Q28Q36"

```
