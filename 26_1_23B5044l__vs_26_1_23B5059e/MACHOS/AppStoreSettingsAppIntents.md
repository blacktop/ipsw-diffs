## AppStoreSettingsAppIntents

> `/System/Library/ExtensionKit/Extensions/AppStoreSettingsAppIntents.appex/AppStoreSettingsAppIntents`

```diff

-12.1.6.0.0
+12.1.13.0.0
   __TEXT.__text: 0x3b98
   __TEXT.__auth_stubs: 0x480
   __TEXT.__cstring: 0x258

   __DATA_CONST.__auth_got: 0x240
   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x480
-  __DATA_CONST.__const: 0x2d0
+  __DATA_CONST.__const: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x230
   __DATA.__bss: 0x1100

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
-  UUID: 6DDC9062-5C4B-3AF2-8F1E-3138D6ACC4DD
+  UUID: A567E0A7-D74A-3E15-B6C8-F349A45DBDFE
   Functions: 164
-  Symbols:   53
+  Symbols:   54
   CStrings:  21
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage

```
