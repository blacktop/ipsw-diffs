## Diagnostic-0001

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-0001.appex/Diagnostic-0001`

```diff

-677.3.6.0.0
+677.4.10.0.0
   __TEXT.__text: 0x640
   __TEXT.__auth_stubs: 0x160
   __TEXT.__objc_methlist: 0x38

   __TEXT.__swift5_typeref: 0x4e
   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x84
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__auth_got: 0xb0
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x88
+  __DATA_CONST.__const: 0x98
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x8
   __DATA.__objc_const: 0x48
   __DATA.__objc_selrefs: 0x48
-  __DATA.__objc_classrefs: 0x8
   __DATA.__objc_data: 0xb0
   __DATA.__data: 0x48
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
   Functions: 16
-  Symbols:   38
+  Symbols:   40
   CStrings:  12
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftsimd
+ _objc_retain
- _objc_retain_x20

```
