## migrationd

> `/System/Library/PrivateFrameworks/MigrationKit.framework/migrationd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_capture`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`

```diff

-1421.0.0.0.0
-  __TEXT.__text: 0x185f4
+1426.0.0.0.0
+  __TEXT.__text: 0x18838
   __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x370
-  __TEXT.__cstring: 0x31c
+  __TEXT.__objc_stubs: 0x3e0
+  __TEXT.__objc_methlist: 0x38c
+  __TEXT.__cstring: 0x34c
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__oslogstring: 0x6b4
+  __TEXT.__oslogstring: 0x704
   __TEXT.__const: 0x5da
   __TEXT.__constg_swiftt: 0x1c0
   __TEXT.__swift5_typeref: 0x44f
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0x10d
+  __TEXT.__swift5_reflstr: 0x107
   __TEXT.__swift5_fieldmd: 0x148
   __TEXT.__swift5_types: 0x10
   __TEXT.__objc_classname: 0xb0
   __TEXT.__objc_methtype: 0x43a
-  __TEXT.__objc_methname: 0x8eb
-  __TEXT.__swift5_assocty: 0x48
-  __TEXT.__swift5_proto: 0xc
+  __TEXT.__objc_methname: 0x94b
+  __TEXT.__swift5_capture: 0x3c8
   __TEXT.__swift_as_entry: 0x94
   __TEXT.__swift_as_ret: 0x90
   __TEXT.__swift_as_cont: 0x19c
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__swift5_capture: 0x3c8
-  __TEXT.__unwind_info: 0x6f8
+  __TEXT.__unwind_info: 0x700
   __TEXT.__eh_frame: 0x12c0
-  __DATA_CONST.__const: 0x7a8
+  __DATA_CONST.__const: 0x7b0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__auth_got: 0x808
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__auth_ptr: 0x180
-  __DATA.__objc_const: 0x5f8
-  __DATA.__objc_selrefs: 0x228
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__auth_ptr: 0x188
+  __DATA.__objc_const: 0x600
+  __DATA.__objc_selrefs: 0x240
   __DATA.__objc_data: 0xc8
-  __DATA.__data: 0x480
+  __DATA.__data: 0x490
   __DATA.__bss: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
+  - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MigrationKit.framework/MigrationKit
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 411
-  Symbols:   432
-  CStrings:  204
+  Functions: 414
+  Symbols:   434
+  CStrings:  209
 
Symbols:
+ _OBJC_CLASS_$_IDSIDQueryController
+ __swift_FORCE_LOAD_$_swiftCompression
CStrings:
+ "flushDeviceQueryForCachedPeers"
+ "invalidateIMessageRegistration"
+ "invalidating stale iMessage registration after the exported line went cold"
+ "migrationd/IMessageRegistration.swift"
+ "sharedInstance"
```
