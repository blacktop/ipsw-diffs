## com.apple.weather.appremoval

> `/System/Library/AppRemovalServices/com.apple.weather.appremoval.xpc/com.apple.weather.appremoval`

```diff

-787.0.0.0.0
+789.3.0.0.0
   __TEXT.__text: 0x1a68
   __TEXT.__auth_stubs: 0x390
   __TEXT.__objc_stubs: 0x4c0

   __DATA_CONST.__auth_got: 0x1d0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1e0
+  __DATA_CONST.__const: 0x1e8
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 35
-  Symbols:   111
+  Symbols:   112
   CStrings:  131
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
