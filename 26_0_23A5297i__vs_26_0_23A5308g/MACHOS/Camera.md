## Camera

> `/private/var/staged_system_apps/Camera.app/Camera`

```diff

-4093.0.0.122.3
+4096.0.0.0.2
   __TEXT.__text: 0x167c
   __TEXT.__auth_stubs: 0x3a0
   __TEXT.__objc_stubs: 0xa0

   __DATA_CONST.__auth_got: 0x1e0
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x100
-  __DATA_CONST.__const: 0x160
+  __DATA_CONST.__const: 0x168
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

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
-  UUID: EE624F59-370E-3A94-9FE5-0A6AF264E43B
+  UUID: 1A64DF54-5D2F-3044-B6F6-B7CF46FA240D
   Functions: 23
-  Symbols:   135
+  Symbols:   136
   CStrings:  23
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreAudio_Private

```
