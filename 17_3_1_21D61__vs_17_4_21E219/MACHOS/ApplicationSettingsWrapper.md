## ApplicationSettingsWrapper

> `/System/Library/PreferenceBundles/ApplicationSettingsWrapper.bundle/ApplicationSettingsWrapper`

```diff

-1250.3.17.0.0
-  __TEXT.__text: 0x700
-  __TEXT.__auth_stubs: 0x1b0
+1250.5.10.0.0
+  __TEXT.__text: 0x6fc
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x52
   __TEXT.__objc_methname: 0xb5
   __TEXT.__swift5_typeref: 0x13
   __TEXT.__cstring: 0x3c
   __TEXT.__unwind_info: 0x64
-  __DATA_CONST.__auth_got: 0xd8
+  __DATA_CONST.__auth_got: 0xd0
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x8
   __DATA.__objc_const: 0x48
   __DATA.__objc_selrefs: 0x68
-  __DATA.__objc_classrefs: 0x8
   __DATA.__objc_data: 0x70
   __DATA.__data: 0x38
   __DATA.__bss: 0x8

   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 22315EA5-B00B-3712-B21A-1CB2DA15AE82
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: DCB3FF9A-D68D-36EA-859E-541CC251005A
   Functions: 12
-  Symbols:   46
+  Symbols:   47
   CStrings:  17
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftsimd
+ _objc_retain
- _objc_release_x22
- _objc_retain_x20

```
