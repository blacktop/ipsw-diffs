## PermissionKit

> `/System/Library/Frameworks/PermissionKit.framework/Versions/A/PermissionKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`

```diff

-92.0.0.0.0
+93.0.0.0.0
   __TEXT.__text: 0x1f230
   __TEXT.__objc_methlist: 0x2c
   __TEXT.__const: 0x2560

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__const: 0xfb8
   __AUTH_CONST.__objc_const: 0x3f8
   __AUTH_CONST.__auth_got: 0x8c8
-  __AUTH.__data: 0x260
-  __DATA.__data: 0x9b0
-  __DATA.__bss: 0x4200
-  __DATA.__common: 0x20
+  __AUTH.__data: 0x128
+  __DATA.__data: 0x780
+  __DATA.__bss: 0x3f80
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__data: 0x368
+  __DATA_DIRTY.__bss: 0x280
+  __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 739
-  Symbols:   423
+  Symbols:   425
   CStrings:  33
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreAudio_$_PermissionKit
```
