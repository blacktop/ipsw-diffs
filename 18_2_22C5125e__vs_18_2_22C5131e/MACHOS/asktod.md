## asktod

> `/usr/libexec/asktod`

```diff

-41.200.1.0.0
+41.225.0.0.0
   __TEXT.__text: 0x35c
   __TEXT.__auth_stubs: 0x150
   __TEXT.__const: 0x32

   __TEXT.__unwind_info: 0x70
   __DATA_CONST.__auth_got: 0xa8
   __DATA_CONST.__got: 0x8
-  __DATA_CONST.__const: 0x110
+  __DATA_CONST.__const: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x10
   __DATA.__data: 0x28

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 5
-  Symbols:   58
+  Symbols:   59
   CStrings:  4
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAppleArchive

```
