## MediaPicker

> `/private/var/staged_system_apps/Music.app/PlugIns/MediaPicker.appex/MediaPicker`

```diff

-4024.200.25.0.0
+4024.210.3.0.0
   __TEXT.__text: 0x2c20
   __TEXT.__auth_stubs: 0x600
   __TEXT.__objc_methlist: 0x70

   __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0xe0
   __DATA_CONST.__auth_ptr: 0x28
-  __DATA_CONST.__const: 0x170
+  __DATA_CONST.__const: 0x178
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftunistd.dylib
   - @rpath/MusicApplication.framework/MusicApplication
   Functions: 44
-  Symbols:   125
+  Symbols:   126
   CStrings:  120
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
