## ShortcutsActions

> `/System/Library/CoreServices/ShortcutsActions.app/ShortcutsActions`

```diff

-2302.0.5.0.0
-  __TEXT.__text: 0x2b0
+2510.5.1.0.0
+  __TEXT.__text: 0x2b4
   __TEXT.__auth_stubs: 0x70
   __TEXT.__swift5_entry: 0x8
   __TEXT.__const: 0x76

   __DATA_CONST.__auth_got: 0x38
   __DATA_CONST.__got: 0x18
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x18
   __DATA.__bss: 0x80

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
+  - /usr/lib/swift/libswiftsimd.dylib
   Functions: 11
-  Symbols:   38
+  Symbols:   40
   CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftsimd

```
