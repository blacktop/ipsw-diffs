## WeatherSettings

> `/System/Library/PreferenceBundles/WeatherSettings.bundle/WeatherSettings`

```diff

-484.1.0.0.0
+515.0.0.0.0
   __TEXT.__text: 0x15bc
   __TEXT.__auth_stubs: 0x2e0
   __TEXT.__objc_stubs: 0x580

   __DATA_CONST.__auth_got: 0x178
   __DATA_CONST.__got: 0x90
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x110
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__cfstring: 0x260
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/WeatherCore.framework/WeatherCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAppleArchive.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6D7DA11D-0609-3131-978A-B472787C7910
+  UUID: 674A7F53-B6F6-31A1-98A9-22188FA841CF
   Functions: 46
-  Symbols:   92
+  Symbols:   96
   CStrings:  129
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers

```
