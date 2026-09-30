## HealthFeaturesBridgeSetupPlugin

> `/System/Library/NanoPreferenceBundles/SetupBundles/HealthFeaturesBridgeSetupPlugin.bundle/HealthFeaturesBridgeSetupPlugin`

```diff

-5200.1.9.1.2
+5200.1.15.1.2
   __TEXT.__text: 0x9e8c
   __TEXT.__auth_stubs: 0x9d0
   __TEXT.__objc_methlist: 0x88

   __TEXT.__unwind_info: 0x248
   __DATA_CONST.__auth_got: 0x4e8
   __DATA_CONST.__got: 0x178
-  __DATA_CONST.__auth_ptr: 0xa8
-  __DATA_CONST.__const: 0x558
+  __DATA_CONST.__auth_ptr: 0xa0
+  __DATA_CONST.__const: 0x560
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

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 190
-  Symbols:   141
+  Symbols:   142
   CStrings:  156
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
