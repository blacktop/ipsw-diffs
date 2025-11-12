## NewDeviceOutreachIntents_iOS

> `/System/Library/ExtensionKit/Extensions/NewDeviceOutreachIntents_iOS.appex/NewDeviceOutreachIntents_iOS`

```diff

-517.60.6.0.0
+517.60.7.0.0
   __TEXT.__text: 0x2354
   __TEXT.__auth_stubs: 0x370
   __TEXT.__cstring: 0xea

   __DATA_CONST.__auth_got: 0x1b8
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x338
-  __DATA_CONST.__const: 0x1e0
+  __DATA_CONST.__const: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x160
   __DATA.__bss: 0xb00

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E0005079-A7B3-3DAD-BC2A-BA4694CDBAB4
+  UUID: 4F12E433-E151-36AA-9050-027EA2388AB1
   Functions: 110
-  Symbols:   42
+  Symbols:   47
   CStrings:  6
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia

```
