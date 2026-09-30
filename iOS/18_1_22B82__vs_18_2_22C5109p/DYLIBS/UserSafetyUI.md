## UserSafetyUI

> `/System/Library/PrivateFrameworks/UserSafetyUI.framework/UserSafetyUI`

```diff

-75.3.105.0.0
+84.5.0.0.0
   __TEXT.__text: 0x4118
   __TEXT.__auth_stubs: 0x480
   __TEXT.__objc_methlist: 0x3a4

   __TEXT.__objc_methtype: 0x101
   __TEXT.__objc_stubs: 0x7c0
   __DATA_CONST.__got: 0xf8
-  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__const: 0x1b0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   - /System/Library/PrivateFrameworks/UserSafety.framework/UserSafety
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 133
-  Symbols:   199
+  Symbols:   204
   CStrings:  195
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia

```
