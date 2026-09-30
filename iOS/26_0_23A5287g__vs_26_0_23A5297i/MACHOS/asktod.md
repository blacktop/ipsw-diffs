## asktod

> `/usr/libexec/asktod`

```diff

-61.4.0.0.0
+62.0.0.0.0
   __TEXT.__text: 0x424
   __TEXT.__auth_stubs: 0x130
   __TEXT.__const: 0x32

   __DATA_CONST.__auth_got: 0x98
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__const: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0x10

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
-  UUID: CE17F0AA-251F-3C24-8052-3F51EC804469
+  UUID: BC46E42A-CBE4-3DEE-90AF-4E4BAC2B4DAB
   Functions: 5
-  Symbols:   51
+  Symbols:   52
   CStrings:  4
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCallKit

```
