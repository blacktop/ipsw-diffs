## ScreenTimeWebExtension

> `/System/Library/Frameworks/ScreenTime.framework/PlugIns/ScreenTimeWebExtension.appex/ScreenTimeWebExtension`

```diff

-605.1.8.0.0
+605.1.15.100.0
   __TEXT.__text: 0x49cc
   __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_stubs: 0x960
   __TEXT.__objc_methlist: 0x390
-  __TEXT.__const: 0x18a
+  __TEXT.__const: 0x19a
   __TEXT.__cstring: 0x2c4
   __TEXT.__objc_methname: 0xd2e
   __TEXT.__oslogstring: 0x10b

   __DATA_CONST.__auth_got: 0x328
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__const: 0x3b8
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 6248AD04-E8DA-3BE0-B4AB-7571D356C304
+  UUID: 421B18A9-CCAC-3B98-B79E-6AA55E41B91C
   Functions: 116
-  Symbols:   145
+  Symbols:   146
   CStrings:  218
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage

```
