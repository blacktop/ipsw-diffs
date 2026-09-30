## HealthMedicationsWidgetExtension

> `/private/var/staged_system_apps/Health.app/PlugIns/HealthMedicationsWidgetExtension.appex/HealthMedicationsWidgetExtension`

```diff

-5200.1.9.1.2
+5200.1.15.1.2
   __TEXT.__text: 0x27c
   __TEXT.__auth_stubs: 0x90
   __TEXT.__swift5_entry: 0x8

   __DATA_CONST.__auth_got: 0x48
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0x140
+  __DATA_CONST.__const: 0x148
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
+  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 10
-  Symbols:   49
+  Symbols:   50
   CStrings:  1
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCryptoTokenKit

```
