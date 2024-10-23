## DevicePropertiesExtension

> `/System/Library/ExtensionKit/Extensions/DevicePropertiesExtension.appex/DevicePropertiesExtension`

```diff

-3401.12.1.0.0
+3402.18.1.0.0
   __TEXT.__text: 0x46b8
   __TEXT.__auth_stubs: 0x640
   __TEXT.__const: 0x39e

   __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x1b0
-  __DATA_CONST.__const: 0x318
+  __DATA_CONST.__const: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x18
   __DATA.__data: 0x150

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
   Functions: 122
-  Symbols:   86
+  Symbols:   88
   CStrings:  29
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
