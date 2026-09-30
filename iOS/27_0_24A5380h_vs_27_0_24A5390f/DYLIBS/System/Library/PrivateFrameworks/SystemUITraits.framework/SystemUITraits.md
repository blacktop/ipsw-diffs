## SystemUITraits

> `/System/Library/PrivateFrameworks/SystemUITraits.framework/SystemUITraits`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`

```diff

-8.0.0.0.0
+9.0.0.0.0
   __TEXT.__text: 0x947c
   __TEXT.__objc_methlist: 0x768
   __TEXT.__const: 0x8a8

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf0
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__cfstring: 0x60
   __AUTH_CONST.__objc_const: 0x19b8
   __AUTH_CONST.__auth_got: 0x510
-  __AUTH.__objc_data: 0xa90
-  __AUTH.__data: 0x278
-  __DATA.__data: 0x5c8
-  __DATA.__bss: 0x480
+  __AUTH.__objc_data: 0x3f0
+  __DATA.__data: 0x588
+  __DATA.__bss: 0x380
+  __DATA_DIRTY.__objc_data: 0x6a0
+  __DATA_DIRTY.__data: 0x2d0
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 327
-  Symbols:   468
+  Symbols:   466
   CStrings:  16
 
Symbols:
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_SystemUITraits
```
