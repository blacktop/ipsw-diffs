## MusicNotificationContentExtension

> `/private/var/staged_system_apps/Music.app/PlugIns/MusicNotificationContentExtension.appex/MusicNotificationContentExtension`

```diff

-4025.600.11.0.0
+4026.100.59.0.0
   __TEXT.__text: 0x16c
   __TEXT.__auth_stubs: 0xa0
   __TEXT.__objc_methlist: 0x20

   __TEXT.__swift5_fieldmd: 0x10
   __TEXT.__swift5_types: 0x4
   __TEXT.__unwind_info: 0x60
-  __DATA_CONST.__auth_got: 0x50
-  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x50
   __DATA.__objc_const: 0x48
   __DATA.__objc_selrefs: 0x18
   __DATA.__objc_data: 0xb0

   - /System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/AppleMediaServicesUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4761DF35-104C-313D-9719-07F98BADB3C4
+  UUID: 2FDA907C-1292-36F4-8E89-34558F7BA2D2
   Functions: 4
-  Symbols:   32
+  Symbols:   34
   CStrings:  6
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMedia

```
