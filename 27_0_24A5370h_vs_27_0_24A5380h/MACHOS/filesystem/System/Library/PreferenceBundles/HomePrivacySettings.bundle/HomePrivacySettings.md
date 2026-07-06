## HomePrivacySettings

> `/System/Library/PreferenceBundles/HomePrivacySettings.bundle/HomePrivacySettings`

```diff

-  __TEXT.__text: 0xc1ec
-  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__text: 0xd4b4
+  __TEXT.__auth_stubs: 0xd90
   __TEXT.__objc_stubs: 0xe0
-  __TEXT.__const: 0x7d0
-  __TEXT.__constg_swiftt: 0x454
-  __TEXT.__swift5_typeref: 0xac7
-  __TEXT.__cstring: 0x7fc
+  __TEXT.__const: 0x848
+  __TEXT.__constg_swiftt: 0x49c
+  __TEXT.__swift5_typeref: 0x94f
+  __TEXT.__cstring: 0x7d8
   __TEXT.__swift5_types: 0x28
-  __TEXT.__objc_classname: 0xd7
-  __TEXT.__objc_methname: 0x1a2
-  __TEXT.__objc_methtype: 0x1
-  __TEXT.__swift5_reflstr: 0x10c
-  __TEXT.__swift5_fieldmd: 0x178
-  __TEXT.__swift5_proto: 0x2c
-  __TEXT.__swift_as_entry: 0x18
-  __TEXT.__swift_as_ret: 0x10
-  __TEXT.__swift_as_cont: 0x1c
-  __TEXT.__swift5_protos: 0x8
+  __TEXT.__objc_classname: 0xdd
+  __TEXT.__swift5_fieldmd: 0x184
+  __TEXT.__swift5_reflstr: 0x12c
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_capture: 0x100
-  __TEXT.__unwind_info: 0x3a0
-  __TEXT.__eh_frame: 0x52c
-  __DATA_CONST.__const: 0x468
+  __TEXT.__swift5_proto: 0x2c
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x20
+  __TEXT.__swift_as_cont: 0x34
+  __TEXT.__objc_methname: 0x1b2
+  __TEXT.__objc_methtype: 0x1
+  __TEXT.__oslogstring: 0x47
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__unwind_info: 0x3f8
+  __TEXT.__eh_frame: 0x624
+  __DATA_CONST.__const: 0x470
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x680
-  __DATA_CONST.__got: 0x210
-  __DATA_CONST.__auth_ptr: 0x278
-  __DATA.__objc_const: 0x340
+  __DATA_CONST.__auth_got: 0x6d0
+  __DATA_CONST.__got: 0x218
+  __DATA_CONST.__auth_ptr: 0x280
+  __DATA.__objc_const: 0x360
   __DATA.__objc_selrefs: 0x40
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x818
-  __DATA.__common: 0xc8
-  __DATA.__bss: 0x508
+  __DATA.__data: 0x860
+  __DATA.__common: 0xe0
+  __DATA.__bss: 0x518
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/EnergyKitFoundation.framework/EnergyKitFoundation
   - /System/Library/PrivateFrameworks/EnergyKitInternal.framework/EnergyKitInternal
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/Settings.framework/Settings

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 271
-  Symbols:   147
-  CStrings:  64
+  Functions: 298
+  Symbols:   152
+  CStrings:  66
 
Sections:
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_capture : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ __os_log_impl
+ __swift_stdlib_bridgeErrorToNSError
+ _objc_retain_x19
+ _os_log_type_enabled
+ _swift_errorRetain
+ _swift_slowAlloc
+ _swift_slowDealloc
- _objc_release_x22
- _swift_getErrorValue
CStrings:
+ "Delete data failed: %@"
+ "Failure checking energy data status: %@"
+ "_canDeleteEnergyData"
- "Delete data failed: "

```
