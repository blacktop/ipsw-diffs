## GMSSELFIngestor

> `/System/Library/ExtensionKit/Extensions/GMSSELFIngestor.appex/GMSSELFIngestor`

```diff

-3405.25.2.0.0
+3405.28.1.0.0
   __TEXT.__text: 0x1198c
   __TEXT.__auth_stubs: 0xae0
   __TEXT.__const: 0x238

   __DATA_CONST.__auth_got: 0x570
   __DATA_CONST.__got: 0x150
   __DATA_CONST.__auth_ptr: 0x130
-  __DATA_CONST.__const: 0x2a8
+  __DATA_CONST.__const: 0x2b8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x3a0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 121
-  Symbols:   126
+  Symbols:   128
   CStrings:  131
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
