## ClassKitAppIntents

> `/System/Library/ExtensionKit/Extensions/ClassKitAppIntents.appex/ClassKitAppIntents`

```diff

-151.1.1.0.0
+151.1.4.0.0
   __TEXT.__text: 0x2544
   __TEXT.__auth_stubs: 0x380
   __TEXT.__const: 0x640

   __DATA_CONST.__auth_got: 0x1c0
   __DATA_CONST.__got: 0x68
   __DATA_CONST.__auth_ptr: 0x358
-  __DATA_CONST.__const: 0x1d8
+  __DATA_CONST.__const: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__data: 0x160
   __DATA.__bss: 0xb80

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
-  UUID: 8A8E9DB4-BC7F-3338-B6D0-1D8FC642ACDB
+  UUID: 5C8559F8-ED55-32BB-8B1A-AC3384C59D1F
   Functions: 111
-  Symbols:   191
+  Symbols:   192
   CStrings:  18
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreImage

```
