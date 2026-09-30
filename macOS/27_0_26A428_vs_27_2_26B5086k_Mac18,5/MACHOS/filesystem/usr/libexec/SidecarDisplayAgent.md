## SidecarDisplayAgent

> `/usr/libexec/SidecarDisplayAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`

```diff

-400.42.0.0.0
-  __TEXT.__text: 0x906bc
-  __TEXT.__auth_stubs: 0x3120
-  __TEXT.__objc_stubs: 0x22c0
+412.2.0.0.0
+  __TEXT.__text: 0x90814
+  __TEXT.__auth_stubs: 0x3150
+  __TEXT.__objc_stubs: 0x2320
   __TEXT.__objc_methlist: 0x7bc
-  __TEXT.__const: 0x5b2a
+  __TEXT.__const: 0x5b39
   __TEXT.__objc_methtype: 0x89e
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x3470
-  __TEXT.__swift5_typeref: 0x1b04
+  __TEXT.__constg_swiftt: 0x3488
+  __TEXT.__swift5_typeref: 0x1b20
   __TEXT.__swift5_builtin: 0x12c
-  __TEXT.__swift5_reflstr: 0x165a
-  __TEXT.__swift5_fieldmd: 0x1e30
+  __TEXT.__swift5_reflstr: 0x168a
+  __TEXT.__swift5_fieldmd: 0x1e3c
   __TEXT.__swift5_assocty: 0x5c0
   __TEXT.__swift5_proto: 0x370
   __TEXT.__swift5_types: 0x270

   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x18
   __TEXT.__swift_as_cont: 0x20
-  __TEXT.__objc_methname: 0x2a29
-  __TEXT.__cstring: 0x17ff
+  __TEXT.__objc_methname: 0x2a79
+  __TEXT.__cstring: 0x17cf
   __TEXT.__oslogstring: 0x2bca
   __TEXT.__swift5_protos: 0x30
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__gcc_except_tab: 0xe0
-  __TEXT.__unwind_info: 0x3490
+  __TEXT.__unwind_info: 0x3498
   __TEXT.__eh_frame: 0x1aa4
   __DATA_CONST.__const: 0x9700
   __DATA_CONST.__cfstring: 0x140

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x18a0
-  __DATA_CONST.__got: 0x710
+  __DATA_CONST.__auth_got: 0x18b8
+  __DATA_CONST.__got: 0x718
   __DATA_CONST.__auth_ptr: 0xb18
-  __DATA.__objc_const: 0x3e88
-  __DATA.__objc_selrefs: 0xab8
+  __DATA.__objc_const: 0x3ea8
+  __DATA.__objc_selrefs: 0xad0
   __DATA.__objc_ivar: 0x14
-  __DATA.__objc_data: 0xe60
-  __DATA.__data: 0x4a00
+  __DATA.__objc_data: 0xe80
+  __DATA.__data: 0x4a30
   __DATA.__common: 0x218
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/Versions/A/CoreGraphics
+  - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore

   - /System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS
   - /System/Library/PrivateFrameworks/Mangrove.framework/Versions/A/Mangrove
   - /System/Library/PrivateFrameworks/MediaContinuityKit.framework/Versions/A/MediaContinuityKit
+  - /System/Library/PrivateFrameworks/MenuBarClientCore.framework/Versions/A/MenuBarClientCore
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 5355
-  Symbols:   1268
-  CStrings:  1092
+  Symbols:   1272
+  CStrings:  1095
 
Symbols:
+ _OBJC_CLASS_$_MBMenuBarItemManager
+ __LSApplicationCheckIn
+ __LSCopyCurrentApplicationASN
+ __LSSignalApplicationReady
CStrings:
+ "$__lazy_storage_$_menuBarItemManager"
+ "412.2"
+ "infoDictionary"
+ "mainBundle"
+ "requestMenuBarVisibility:lockToken:completionHandler:"
- "400.42"
- "SLSSetMenuBarVisibilityOverrideOnDisplay"
```
