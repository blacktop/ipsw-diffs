## HealthStandaloneIntents

> `/System/Library/ExtensionKit/Extensions/HealthStandaloneIntents.appex/HealthStandaloneIntents`

```diff

-6200.2.7.2.1
+6200.2.11.2.0
   __TEXT.__text: 0x85bc
   __TEXT.__auth_stubs: 0x840
   __TEXT.__const: 0x948

   __DATA_CONST.__auth_got: 0x420
   __DATA_CONST.__got: 0x170
   __DATA_CONST.__auth_ptr: 0x450
-  __DATA_CONST.__const: 0x3c0
+  __DATA_CONST.__const: 0x3c8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_selrefs: 0x28
   __DATA.__data: 0x208

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 405FF13C-A2B4-3B53-B738-8BBDF7D5B699
+  UUID: D11A8919-78B6-39B5-A0E9-3CC50D647C61
   Functions: 210
-  Symbols:   74
+  Symbols:   75
   CStrings:  37
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage

```
