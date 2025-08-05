## LockScreenCamera

> `/private/var/staged_system_apps/Camera.app/Extensions/LockScreenCamera.appex/LockScreenCamera`

```diff

-4093.0.0.122.3
+4096.0.0.0.2
   __TEXT.__text: 0x6a4
   __TEXT.__auth_stubs: 0x130
   __TEXT.__swift5_entry: 0x8

   __DATA_CONST.__auth_got: 0x98
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x98
-  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__const: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x8
   __DATA.__data: 0x60

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
+  - /usr/lib/swift/libswiftCoreAudio_Private.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 381F8587-9E0E-3B15-BB6A-EAB11A033907
+  UUID: 36384DB4-3797-34B8-963D-BDD1599DDFCF
   Functions: 19
-  Symbols:   45
+  Symbols:   46
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
