## com.apple.weatherkit.authservice

> `/System/Library/Frameworks/WeatherKit.framework/XPCServices/com.apple.weatherkit.authservice.xpc/com.apple.weatherkit.authservice`

```diff

-787.0.0.0.0
+789.3.0.0.0
   __TEXT.__text: 0x984
   __TEXT.__auth_stubs: 0x260
   __TEXT.__const: 0x7e

   __DATA_CONST.__auth_got: 0x130
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 14
-  Symbols:   47
+  Symbols:   48
   CStrings:  9
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
