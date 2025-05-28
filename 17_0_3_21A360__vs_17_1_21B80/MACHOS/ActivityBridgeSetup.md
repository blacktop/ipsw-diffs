## ActivityBridgeSetup

> `/System/Library/NanoPreferenceBundles/SetupBundles/ActivityBridgeSetup.bundle/ActivityBridgeSetup`

```diff

-1515.0.0.0.0
+1519.11.0.0.0
   __TEXT.__text: 0xb5cc
   __TEXT.__auth_stubs: 0x880
   __TEXT.__objc_stubs: 0x24c0

   __DATA_CONST.__auth_got: 0x450
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x510
+  __DATA_CONST.__const: 0x518
   __DATA_CONST.__cfstring: 0x7c0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreML.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 256
-  Symbols:   259
+  Symbols:   260
   CStrings:  848
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreML

```
