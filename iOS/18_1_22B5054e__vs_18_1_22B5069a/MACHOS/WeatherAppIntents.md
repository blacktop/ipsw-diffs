## WeatherAppIntents

> `/private/var/staged_system_apps/Weather.app/Extensions/WeatherAppIntents.appex/WeatherAppIntents`

```diff

-787.0.0.0.0
+789.3.0.0.0
   __TEXT.__text: 0x2b54
   __TEXT.__auth_stubs: 0x5a0
   __TEXT.__const: 0x262

   __DATA_CONST.__auth_got: 0x2d0
   __DATA_CONST.__got: 0xe8
   __DATA_CONST.__auth_ptr: 0x180
-  __DATA_CONST.__const: 0x1e0
+  __DATA_CONST.__const: 0x1e8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x148

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 82
-  Symbols:   65
+  Symbols:   66
   CStrings:  5
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
