## AskToExtension

> `/Applications/AskToMessagesHost.app/Extensions/AskToExtension.appex/AskToExtension`

```diff

-41.200.1.0.0
+41.225.0.0.0
   __TEXT.__text: 0x1610
   __TEXT.__auth_stubs: 0x410
   __TEXT.__const: 0x1ae

   __DATA_CONST.__auth_got: 0x208
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0xc8
-  __DATA_CONST.__const: 0x1b8
+  __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x60
   __DATA.__data: 0x40

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 44
-  Symbols:   77
+  Symbols:   78
   CStrings:  29
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAppleArchive

```
