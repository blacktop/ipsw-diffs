## WeatherDiagnosticExtension

> `/private/var/staged_system_apps/Weather.app/PlugIns/WeatherDiagnosticExtension.appex/WeatherDiagnosticExtension`

```diff

-787.0.0.0.0
+789.3.0.0.0
   __TEXT.__text: 0x3024
   __TEXT.__auth_stubs: 0x730
   __TEXT.__objc_stubs: 0x1a0

   __DATA_CONST.__auth_got: 0x3a0
   __DATA_CONST.__got: 0x88
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftFileProvider.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 56
-  Symbols:   110
+  Symbols:   111
   CStrings:  60
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
