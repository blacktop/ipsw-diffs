## AskToExtension

> `/System/Library/ExtensionKit/Extensions/AskToExtension.appex/AskToExtension`

```diff

-61.4.0.0.0
+62.0.0.0.0
   __TEXT.__text: 0x2870
   __TEXT.__auth_stubs: 0x510
   __TEXT.__const: 0x24c

   __DATA_CONST.__auth_got: 0x288
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0xf0
-  __DATA_CONST.__const: 0x2a8
+  __DATA_CONST.__const: 0x2b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x78
   __DATA.__data: 0x58

   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
+  - /usr/lib/swift/libswiftCallKit.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9D41CC13-F564-3ED7-B748-C24BDFCD96BE
+  UUID: 96099E71-06FA-3562-9F6C-FBCDE7999578
   Functions: 62
-  Symbols:   80
+  Symbols:   81
   CStrings:  25
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit

```
